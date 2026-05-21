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
