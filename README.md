# ProfileFit® - AI-Powered Resume Analyzer & Job Matcher

ProfileFit® is a state-of-the-art, responsive web application designed to help job seekers evaluate their resumes against current job descriptions. Using **Google Gemini 2.5 Flash**, the system contextually extracts skills, performs a formatting audit, predicts ATS compatibility scores, and recommends tailored additions to maximize match success.

---

## 🌐 Live Demo & Deployments

The project is deployed and accessible online:

*   **Frontend (UI)**: [https://resume-analyzer-theta-weld.vercel.app/](https://resume-analyzer-theta-weld.vercel.app/)
    *   *Hosted on:* **Vercel** (Static Site Hosting)
    *   *Description:* Serves the responsive React single-page application and handles interactive charts, compatibility gauges, and theme switching.
*   **Backend (API)**: [https://resume-analyzer-vqve.onrender.com](https://resume-analyzer-vqve.onrender.com)
    *   *Hosted on:* **Render** (Web Service container)
    *   *Description:* Runs the FastAPI python server, processes PDF resume uploads using PyPDF, and connects to the Google Gemini API for zero-shot extraction.
    *   *Note on Free Hosting:* The backend uses Render's free tier, which goes to sleep after 15 minutes of inactivity. When you first access the site or upload a resume after a period of inactivity, the server may take **50-90 seconds** to boot back up. Subsequent actions will load instantly.

---

## 🌟 Key Features

*   **Contextual Gemini API Matching**: Powered by `gemini-2.5-flash` with a 1M+ token context window, ensuring full-length resumes are analyzed without truncation.
*   **Universal Skill Extraction**: Dynamic zero-shot skill extraction and categorization across all industries (Tech, Mechanical, Civil, Chemical, Finance, Business, HR, etc.) without rigid keyword matching.
*   **ATS Compatibility Scoring**: Hybrid evaluation combining semantic text similarity (50%), math-based skill criteria (40%), and formatting checks (10%).
*   **Automated Formatting Audit**: Structural review detecting word count issues, standard sections (Experience, Education, Projects), and missing contact details (Email, Phone).
*   **Actionable Tailoring Suggestions**: Real-time feedback calculating how much your score will improve by adding specific missing keywords.
*   **Stunning UI**: Responsive dashboard with animations, theme toggles (Dark/Light mode), and compatibility gauges.

---

## 🏗️ Architecture & Pipeline Diagram

```
[Resume PDF] ──> (pypdf Text Extraction) 
                       │
                       ▼ (Plain Text)
         ┌─────────────┴─────────────┐
         ▼                           ▼
(Local Regex Audits)       (Google Gemini 2.5 Flash API)
  - Word Count               - Zero-Shot Skill Extraction
  - Section Headings         - Dynamic Categorization
  - Contact Details          - Semantic Job Alignment Rating
         │                           │
         └─────────────┬─────────────┘
                       ▼
          (Combined ATS Score Calculation)
                       │
                       ▼ (Structured JSON Response)
             [React Dashboard UI]
```

---

## 📂 Project Structure

*   `backend/`: FastAPI server containing parsing logic, Gemini API integrations, and the job database.
*   `frontend/`: React SPA built with Vite and clean, responsive vanilla CSS.

---

## 🚀 Getting Started

### Prerequisites
*   Python 3.10+
*   Node.js v18+ and NPM
*   A **Google Gemini API Key** (Get one for free at the [Google AI Studio](https://aistudio.google.com/))

---

### Backend Setup & Run

1.  **Navigate to the backend folder**:
    ```bash
    cd backend
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**:
    Create a `.env` file in the `backend/` directory and insert your API key:
    ```env
    GEMINI_API_KEY=your_gemini_api_key_here
    ```

4.  **Start the API Server**:
    ```bash
    uvicorn main:app --reload
    ```
    *The API will run on http://127.0.0.1:8000.*

---

### Frontend Setup & Run

1.  **Navigate to the frontend folder**:
    ```bash
    cd ../frontend
    ```

2.  **Install node packages**:
    ```bash
    npm install
    ```

3.  **Start the Dev Server**:
    ```bash
    npm run dev
    ```
    *The Web app will be accessible at http://localhost:5173/.*

---

## ⚙️ How the ATS Scoring System Works

The overall compatibility percentage is computed using three weighted layers:
1.  **Semantic Match (50% weight)**: Gemini evaluates how close your resume's experiences and projects match the role description and responsibilities.
2.  **Skills Match (40% weight)**: Compares required skills in the job posting against the extracted resume skills (supporting fuzzy substring matches for spelling variations).
3.  **Formatting Check (10% weight)**: Evaluates structural layout compliance (standard sections, word counts, contact info).
