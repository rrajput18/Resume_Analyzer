# AI-Powered Resume Analyzer & Job Recommendation System

This project is a modern web application that allows users to upload a PDF resume, parses its text, extracts technical skills using Natural Language Processing (NLP), estimates an ATS score against job descriptions, highlights missing recommended skills, and provides job matches with semantic similarity analysis.

## Repository Structure

- `backend/`: FastAPI Python server containing the PDF parser, skills extraction engine (spaCy), and recommendation matcher (Sentence Transformers).
- `frontend/`: React single-page application built with Vite and custom premium CSS.

## Getting Started

### Prerequisites
- Python 3.10+
- Node.js v24.15.0+ and NPM

### Running the Backend
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the spaCy language model:
   ```bash
   python -m spacy download en_core_web_sm
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   The backend will run on `http://localhost:8000`.

### Running the Frontend
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the Vite development server:
   ```bash
   npm run dev
   ```
   The frontend will run on `http://localhost:5173`.
