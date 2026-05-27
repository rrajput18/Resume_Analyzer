from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from pdf_parser import extract_text_from_pdf
from skills_extractor import extract_skills
from matcher import match_resume
from jobs_db import JOBS

app = FastAPI(
    title="AI-Powered Resume Analyzer API",
    description="Backend API for parsing resumes, extracting skills, and matching with job postings using NLP.",
    version="1.0.0"
)

# Configure CORS to allow communication from React Frontend (including production deployments)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    """
    Startup event handler.
    """
    print("Resume Analyzer API server started successfully.")

@app.get("/api/health")
def health_check():
    return {"status": "healthy", "message": "Resume Analyzer API is up and running"}

@app.get("/api/jobs")
def get_jobs():
    """
    Endpoint to retrieve the list of all available job listings.
    """
    return {"jobs": JOBS}

@app.post("/api/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    """
    Upload a resume PDF, parse text, extract skills, and match with the job database.
    """
    # 1. Validate file extension
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400, 
            detail="Invalid file format. Only PDF files are supported."
        )
    
    try:
        # 2. Read file bytes
        file_bytes = await file.read()
        
        # 3. Extract text
        resume_text = extract_text_from_pdf(file_bytes)
        if not resume_text or len(resume_text.strip()) == 0:
            raise HTTPException(
                status_code=400,
                detail="Could not extract text from the PDF. Please make sure the PDF is not scanned/image-only or encrypted."
            )
            
        # 4. Perform matching and ATS scoring (skills are extracted via Gemini inside match_resume)
        match_payload = match_resume(resume_text)
        skills_payload = match_payload["skills_extracted"]
        
        # 5. Calculate summary metrics
        job_matches = match_payload["job_matches"]
        avg_ats_score = int(sum(job["match_scores"]["ats_score"] for job in job_matches) / len(job_matches)) if job_matches else 0
        top_match_job = job_matches[0]["title"] if job_matches else "N/A"
        top_match_company = job_matches[0]["company"] if job_matches else "N/A"
        top_match_score = job_matches[0]["match_scores"]["ats_score"] if job_matches else 0
        
        return {
            "success": True,
            "filename": file.filename,
            "text_length": len(resume_text),
            "summary": {
                "skills_count": len(skills_payload["matched_skills"]),
                "average_ats_score": avg_ats_score,
                "top_match": {
                    "title": top_match_job,
                    "company": top_match_company,
                    "score": top_match_score
                }
            },
            "skills_extracted": skills_payload,
            "formatting_analysis": match_payload["formatting_analysis"],
            "job_matches": job_matches
        }
        
    except HTTPException as he:
        raise he
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"An unexpected error occurred during resume analysis: {str(e)}"
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
