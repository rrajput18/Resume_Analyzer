import re
from sentence_transformers import SentenceTransformer, util
from jobs_db import JOBS

model = None
job_embeddings = {}

def get_model():
    """
    Lazy loader for the SentenceTransformer model.
    """
    global model
    if model is None:
        print("Loading SentenceTransformer model 'all-MiniLM-L6-v2'...")
        model = SentenceTransformer('all-MiniLM-L6-v2')
        print("Model loaded successfully.")
    return model

def precalculate_job_embeddings():
    """
    Encodes all job listings in the database for faster similarity calculations.
    """
    global job_embeddings
    m = get_model()
    for job in JOBS:
        if job["id"] not in job_embeddings:
            # Create a rich text representation of the job
            text_to_encode = f"Job Title: {job['title']}\nDepartment: {job['department']}\nDescription: {job['description']}\nRequired Skills: {', '.join(job['skills_required'])}"
            job_embeddings[job["id"]] = m.encode(text_to_encode, convert_to_tensor=True)

def assess_formatting(text: str) -> dict:
    """
    Analyzes basic resume formatting details.
    Returns a score out of 100 and key observations.
    """
    score = 100
    observations = []
    
    # Check word count
    word_count = len(text.split())
    if word_count < 100:
        score -= 30
        observations.append("Resume is extremely short (under 100 words). Add more details about your experience.")
    elif word_count < 250:
        score -= 15
        observations.append("Resume is slightly short (under 250 words). Consider expanding on projects and achievements.")
    elif word_count > 1500:
        score -= 15
        observations.append("Resume is very long (over 1500 words). Aim for a concise 1-2 page format.")
        
    # Check for contact information (email)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    if not emails:
        score -= 20
        observations.append("No email address detected. Ensure your contact details are clearly listed.")
        
    # Check for phone number (simple pattern)
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phones = re.findall(phone_pattern, text)
    if not phones:
        score -= 15
        observations.append("No standard phone number detected. Add a phone number to help recruiters reach you.")
        
    # Check for standard sections (Experience, Education)
    sections = ["experience", "work history", "employment", "education", "projects", "skills"]
    found_sections = []
    for section in sections:
        if re.search(r'\b' + re.escape(section) + r'\b', text.lower()):
            found_sections.append(section)
            
    if len(found_sections) < 3:
        score -= 20
        observations.append("Missing standard resume sections. Structure your resume with clear headings (e.g., Experience, Education, Projects).")
        
    score = max(0, score)
    return {
        "score": score,
        "observations": observations
    }

def match_resume(resume_text: str, extracted_skills: list) -> list:
    """
    Matches the resume text against the job database.
    Calculates semantic similarity, skills match, formatting, and final ATS score.
    """
    # Ensure model and embeddings are loaded
    m = get_model()
    precalculate_job_embeddings()
    
    # Encode resume text
    resume_embedding = m.encode(resume_text, convert_to_tensor=True)
    
    # Analyze formatting
    formatting_analysis = assess_formatting(resume_text)
    formatting_score = formatting_analysis["score"]
    
    resume_skills_set = {skill.lower() for skill in extracted_skills}
    
    results = []
    
    for job in JOBS:
        # 1. Semantic Similarity (50% weight)
        job_emb = job_embeddings[job["id"]]
        cosine_sim = float(util.cos_sim(resume_embedding, job_emb)[0][0])
        # Map similarity from [-1, 1] to [0, 100]
        semantic_score = max(0.0, min(100.0, (cosine_sim + 0.2) * 83.3)) # Normalizing range
        
        # 2. Skills Match (40% weight)
        job_skills = job["skills_required"]
        matched_skills_for_job = []
        missing_skills_for_job = []
        
        for req_skill in job_skills:
            if req_skill.lower() in resume_skills_set:
                matched_skills_for_job.append(req_skill)
            else:
                missing_skills_for_job.append(req_skill)
                
        skills_match_ratio = len(matched_skills_for_job) / len(job_skills) if job_skills else 1.0
        skills_score = skills_match_ratio * 100.0
        
        # 3. Final ATS Score
        ats_score = int((semantic_score * 0.50) + (skills_score * 0.40) + (formatting_score * 0.10))
        ats_score = max(0, min(100, ats_score))
        
        # Calculate impact of missing skills for recommendation
        # Each missing skill contributes roughly to a portion of the skills score
        skill_impact = round((40.0 / len(job_skills)) if job_skills else 0, 1)
        
        results.append({
            "job_id": job["id"],
            "title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "department": job["department"],
            "salary_range": job["salary_range"],
            "description": job["description"],
            "match_scores": {
                "ats_score": ats_score,
                "semantic_similarity": int(semantic_score),
                "skills_match": int(skills_score),
                "formatting_check": int(formatting_score)
            },
            "skills_analysis": {
                "matched_skills": matched_skills_for_job,
                "missing_skills": missing_skills_for_job,
                "single_skill_value": skill_impact
            }
        })
        
    # Sort by ATS score in descending order
    results.sort(key=lambda x: x["match_scores"]["ats_score"], reverse=True)
    
    return {
        "job_matches": results,
        "formatting_analysis": formatting_analysis
    }
