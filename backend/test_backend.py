# Test script for backend parsing and matching logic
import os
import json
from unittest.mock import patch

# Mock responses for testing when no GEMINI_API_KEY is configured
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
                return MockResponse(json.dumps({"extracted_skills": [], "job_semantic_matches": []}))
                
    def __init__(self, api_key=None):
        self.models = self.Models()

# Apply mock client if no GEMINI_API_KEY is found
api_key = os.getenv("GEMINI_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    print("WARNING: GEMINI_API_KEY not configured. Running tests using MOCKED Gemini client.")
    import matcher
    matcher.get_gemini_client = lambda: MockClient()
else:
    print("SUCCESS: GEMINI_API_KEY detected. Running tests with REAL Gemini API.")

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

    # 2. Mock mechanical engineering profile
    mech_resume = """
    Jane Smith
    Email: jane.smith@email.com
    Phone: 987-654-3210
    Location: Detroit, MI
    
    Summary:
    Dedicated Mechanical Engineer with expertise in robotics, 3D modeling, and HVAC systems design.
    
    Skills:
    CAD, SolidWorks, Robotics, HVAC, ROS, Thermodynamics, Fluid Mechanics, Pneumatics, Hydraulics, ANSYS, FEA
    """
    print("\n" + "=" * 40)
    print("=== Testing Mechanical Engineering Profile ===")
    print("=" * 40)
    skills_payload_mech = extract_skills(mech_resume)
    print(f"Total skills matched: {len(skills_payload_mech['matched_skills'])}")
    print(f"Extracted skills: {skills_payload_mech['matched_skills']}")
    match_payload_mech = match_resume(mech_resume, skills_payload_mech["matched_skills"])
    job_matches_mech = match_payload_mech["job_matches"]
    
    print("\nTop 3 Job Matches for Mechanical Profile:")
    for idx, match in enumerate(job_matches_mech[:3]):
        print(f"{idx+1}. {match['title']} at {match['company']} ({match['department']})")
        print(f"   ATS Score: {match['match_scores']['ats_score']}%")
        print(f"   Semantic Match: {match['match_scores']['semantic_similarity']}% | Skills Match: {match['match_scores']['skills_match']}%")
        print(f"   Matched Skills: {match['skills_analysis']['matched_skills']}")
        print(f"   Missing Skills: {match['skills_analysis']['missing_skills']}")
        print("-" * 50)

    # 3. Mock Finance profile
    finance_resume = """
    Robert Johnson
    Email: robert.j@email.com
    Phone: 555-019-2834
    Location: New York, NY
    
    Summary:
    Financial analyst with experience in financial modeling, budgeting, and forecasting. Strong expertise in corporate finance and Excel.
    
    Skills:
    Financial Analysis, Financial Modeling, Budgeting, Forecasting, Corporate Finance, Excel, Data Analysis
    """
    print("\n" + "=" * 40)
    print("=== Testing Finance Profile ===")
    print("=" * 40)
    skills_payload_fin = extract_skills(finance_resume)
    print(f"Total skills matched: {len(skills_payload_fin['matched_skills'])}")
    print(f"Extracted skills: {skills_payload_fin['matched_skills']}")
    match_payload_fin = match_resume(finance_resume, skills_payload_fin["matched_skills"])
    job_matches_fin = match_payload_fin["job_matches"]
    
    print("\nTop 3 Job Matches for Finance Profile:")
    for idx, match in enumerate(job_matches_fin[:3]):
        print(f"{idx+1}. {match['title']} at {match['company']} ({match['department']})")
        print(f"   ATS Score: {match['match_scores']['ats_score']}%")
        print(f"   Semantic Match: {match['match_scores']['semantic_similarity']}% | Skills Match: {match['match_scores']['skills_match']}%")
        print(f"   Matched Skills: {match['skills_analysis']['matched_skills']}")
        print(f"   Missing Skills: {match['skills_analysis']['missing_skills']}")
        print("-" * 50)

if __name__ == "__main__":
    test_resume_analyzer()
