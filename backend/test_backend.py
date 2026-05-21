# Test script for backend parsing and matching logic
from skills_extractor import extract_skills
from matcher import match_resume

def test_resume_analyzer():
    # 1. A mock resume text representing an AI/ML developer profile
    mock_resume = """
    John Doe
    Email: john.doe@email.com
    Phone: 123-456-7890
    Location: San Francisco, CA
    
    Professional Summary:
    Experienced Machine Learning Engineer with a passion for NLP and Generative AI. 
    Skilled in Python, PyTorch, and deploying cloud models using Docker and AWS.
    
    Experience:
    AI Developer at TechLabs (2023 - Present)
    - Developed custom Retrieval-Augmented Generation (RAG) pipelines using LangChain and Vector Databases.
    - Trained Transformers and BERT models for text classification tasks.
    - Worked on data analytics pipelines utilizing Pandas and NumPy.
    
    Software Engineer at CodeWorks (2021 - 2023)
    - Built responsive web interfaces using React.js and HTML/CSS.
    - Implemented REST APIs in Python using FastAPI.
    - Managed relational database migrations using PostgreSQL and Git.
    
    Education:
    B.S. in Computer Science - Stanford University
    
    Skills:
    Python, PyTorch, React, Docker, AWS, Git, FastAPI, SQL, PostgreSQL, NLP, Generative AI, RAG, Transformers, Pandas, NumPy
    """
    
    print("=== Testing Skills Extraction ===")
    skills_payload = extract_skills(mock_resume)
    print(f"Total skills matched: {len(skills_payload['matched_skills'])}")
    print(f"Extracted skills: {skills_payload['matched_skills']}")
    print(f"Categorized: {skills_payload['by_category']}")
    print()
    
    print("=== Testing Job Matching ===")
    match_payload = match_resume(mock_resume, skills_payload["matched_skills"])
    job_matches = match_payload["job_matches"]
    formatting = match_payload["formatting_analysis"]
    
    print(f"Formatting check score: {formatting['score']}/100")
    print(f"Formatting observations: {formatting['observations']}")
    print()
    
    print("Top 3 Job Matches:")
    for idx, match in enumerate(job_matches[:3]):
        print(f"{idx+1}. {match['title']} at {match['company']} ({match['department']})")
        print(f"   ATS Score: {match['match_scores']['ats_score']}%")
        print(f"   Semantic Match: {match['match_scores']['semantic_similarity']}% | Skills Match: {match['match_scores']['skills_match']}%")
        print(f"   Matched Skills: {match['skills_analysis']['matched_skills']}")
        print(f"   Missing Skills: {match['skills_analysis']['missing_skills']}")
        print("-" * 50)

if __name__ == "__main__":
    test_resume_analyzer()
