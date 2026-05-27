import os
import re
import json
from google import genai
from google.genai import types
from google.genai.errors import APIError
from pydantic import BaseModel, Field
from typing import List, Dict
from dotenv import load_dotenv

from jobs_db import JOBS

# Load environment variables
load_dotenv()

# Schema for Structured Output
class JobSemanticMatch(BaseModel):
    job_id: int = Field(description="The ID of the job from the jobs list.")
    semantic_similarity: int = Field(description="A contextual score from 0 to 100 representing how well the resume's experience and background match this job.")

class SkillCategory(BaseModel):
    category: str = Field(description="Logical category name for the skills (e.g. Programming Languages, Databases & Tools, Mechanical Engineering, Civil Engineering, Finance & Accounting, Soft Skills, etc.)")
    skills: List[str] = Field(description="List of skills belonging to this category extracted from the resume.")

class ResumeAnalysisResponse(BaseModel):
    extracted_skills: List[SkillCategory] = Field(description="List of skills extracted from the resume grouped by logical categories.")
    job_semantic_matches: List[JobSemanticMatch] = Field(description="Contextual semantic evaluation scores for each job listing.")

# Mock responses for testing and demo when no GEMINI_API_KEY is configured
MOCK_AIML_RESPONSE = {
    "extracted_skills": [
        {"category": "Programming Languages", "skills": ["Python", "SQL", "HTML", "CSS", "React"]},
        {"category": "Machine Learning & AI", "skills": ["BERT", "Generative AI", "LangChain", "Machine Learning", "NLP", "RAG", "Transformers", "Vector Databases"]},
        {"category": "Frameworks & Libraries", "skills": ["FastAPI", "NumPy", "Pandas", "PyTorch"]},
        {"category": "Databases & Tools", "skills": ["AWS", "Docker", "Git", "PostgreSQL"]},
        {"category": "Concepts & Methodologies", "skills": ["REST APIs"]}
    ],
    "job_semantic_matches": [
        {"job_id": 1, "semantic_similarity": 82},
        {"job_id": 2, "semantic_similarity": 75},
        {"job_id": 3, "semantic_similarity": 85},
        {"job_id": 4, "semantic_similarity": 88},
        {"job_id": 5, "semantic_similarity": 80},
        {"job_id": 6, "semantic_similarity": 72},
        {"job_id": 7, "semantic_similarity": 68},
        {"job_id": 8, "semantic_similarity": 76},
        {"job_id": 9, "semantic_similarity": 62},
        {"job_id": 10, "semantic_similarity": 74}
    ]
}

MOCK_MECH_RESPONSE = {
    "extracted_skills": [
        {"category": "Mechanical Engineering", "skills": ["CAD", "SolidWorks", "FEA", "ANSYS", "Thermodynamics", "Fluid Mechanics", "Robotics", "Pneumatics", "Hydraulics", "ROS"]}
    ],
    "job_semantic_matches": [
        {"job_id": 11, "semantic_similarity": 88},
        {"job_id": 15, "semantic_similarity": 82},
        {"job_id": 16, "semantic_similarity": 90}
    ]
}

MOCK_FINANCE_RESPONSE = {
    "extracted_skills": [
        {"category": "Finance & Accounting", "skills": ["Financial Analysis", "Financial Modeling", "Forecasting", "Budgeting", "Corporate Finance", "Excel", "Data Analysis"]}
    ],
    "job_semantic_matches": [
        {"job_id": 24, "semantic_similarity": 92},
        {"job_id": 23, "semantic_similarity": 48},
        {"job_id": 9, "semantic_similarity": 66}
    ]
}

class MockClient:
    class Models:
        def generate_content(self, model, contents, config):
            class MockResponse:
                def __init__(self, text):
                    self.text = text
            
            prompt_lower = contents.lower()
            if "john doe" in prompt_lower or "john.doe" in prompt_lower:
                return MockResponse(json.dumps(MOCK_AIML_RESPONSE))
            elif "jane smith" in prompt_lower or "jane.smith" in prompt_lower:
                return MockResponse(json.dumps(MOCK_MECH_RESPONSE))
            elif "robert johnson" in prompt_lower or "robert.j" in prompt_lower:
                return MockResponse(json.dumps(MOCK_FINANCE_RESPONSE))
            else:
                # Return standard fallback matching the profile type
                if "mechanical" in prompt_lower or "solidworks" in prompt_lower or "cad" in prompt_lower:
                    return MockResponse(json.dumps(MOCK_MECH_RESPONSE))
                elif "finance" in prompt_lower or "budget" in prompt_lower or "excel" in prompt_lower:
                    return MockResponse(json.dumps(MOCK_FINANCE_RESPONSE))
                return MockResponse(json.dumps(MOCK_AIML_RESPONSE))
                
    def __init__(self, api_key=None):
        self.models = self.Models()

def get_gemini_client():
    """
    Initializes and returns the GenAI Client.
    Falls back to a MockClient if GEMINI_API_KEY is not configured.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("WARNING: GEMINI_API_KEY not configured. Falling back to MockClient for demo/testing.")
        return MockClient()
    return genai.Client(api_key=api_key)

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

def is_skill_present(req_skill: str, extracted_skills: set) -> bool:
    """
    Checks if a required skill is present in the extracted skills set,
    handling slight variations and substring matching (case-insensitive).
    """
    req_lower = req_skill.lower()
    for ext in extracted_skills:
        ext_lower = ext.lower()
        if req_lower == ext_lower or req_lower in ext_lower or ext_lower in req_lower:
            return True
    return False

def match_resume(resume_text: str, extracted_skills: list = None) -> dict:
    """
    Performs full analysis of the resume using Google Gemini API.
    Extracts skills, performs formatting checks, and evaluates ATS matches.
    """
    # 1. Formatting audit
    formatting_analysis = assess_formatting(resume_text)
    formatting_score = formatting_analysis["score"]
    
    # 2. Get GenAI Client
    client = get_gemini_client()
    
    # 3. Create simplified jobs description for the LLM context
    jobs_summary = []
    for job in JOBS:
        jobs_summary.append({
            "id": job["id"],
            "title": job["title"],
            "department": job["department"],
            "description": job["description"],
            "skills_required": job["skills_required"]
        })
        
    prompt = f"""
You are an expert ATS (Applicant Tracking System) parser and Job Matcher.
Analyze the following resume and evaluate it against the list of available jobs.

--- RESUME TEXT ---
{resume_text}

--- JOBS DATABASE ---
{json.dumps(jobs_summary, indent=2)}

--- INSTRUCTIONS ---
1. Extract all professional skills from the resume and group them into logical categories (e.g. Programming Languages, Databases, Mechanical Engineering, Civil Engineering, Finance, Soft Skills, etc. as appropriate).
2. For each job in the database, evaluate the semantic similarity of the resume text to the job description and title. Provide a score from 0 to 100:
   - 90-100: Perfect match (candidate has directly relevant experience and roles).
   - 70-89: Good match (candidate has related experience and skills).
   - 40-69: Moderate match (candidate has transferrable skills but is in a different domain or less experienced).
   - 0-39: Poor match (mismatched field or lacks required experience entirely).
   Be fair and objective. Do not bias towards tech jobs if the resume is a mechanical or civil engineering resume.
"""

    # 4. Generate structured content
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ResumeAnalysisResponse,
                temperature=0.1
            )
        )
        
        # Parse output
        analysis_result = json.loads(response.text)
    except APIError as ae:
        raise RuntimeError(f"Gemini API error: {ae.message}")
    except Exception as e:
        raise RuntimeError(f"Failed to process resume analysis: {str(e)}")
        
    # 5. Format extracted skills for frontend
    extracted_skills_list = []
    by_category = {}
    for cat_data in analysis_result.get("extracted_skills", []):
        cat_name = cat_data.get("category", "")
        skills_in_cat = cat_data.get("skills", [])
        if skills_in_cat and cat_name:
            by_category[cat_name] = sorted(list(set(skills_in_cat)))
            extracted_skills_list.extend(skills_in_cat)
            
    matched_skills = sorted(list(set(extracted_skills_list)))
    resume_skills_set = {s.lower() for s in matched_skills}
    
    # 6. Map semantic match scores and calculate detailed scores
    semantic_scores_map = {m["job_id"]: m["semantic_similarity"] for m in analysis_result.get("job_semantic_matches", [])}
    
    results = []
    for job in JOBS:
        # Retrieve semantic similarity from Gemini (default to 10 if not returned)
        semantic_score = semantic_scores_map.get(job["id"], 10)
        
        # Calculate skills match mathematically
        job_skills = job["skills_required"]
        matched_skills_for_job = []
        missing_skills_for_job = []
        
        for req_skill in job_skills:
            if is_skill_present(req_skill, resume_skills_set):
                matched_skills_for_job.append(req_skill)
            else:
                missing_skills_for_job.append(req_skill)
                
        skills_match_ratio = len(matched_skills_for_job) / len(job_skills) if job_skills else 1.0
        skills_score = skills_match_ratio * 100.0
        
        # Calculate final combined ATS Score (50% Semantic, 40% Skills, 10% Formatting)
        ats_score = int((semantic_score * 0.50) + (skills_score * 0.40) + (formatting_score * 0.10))
        ats_score = max(0, min(100, ats_score))
        
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
        "formatting_analysis": formatting_analysis,
        "skills_extracted": {
            "matched_skills": matched_skills,
            "by_category": by_category
        }
    }
