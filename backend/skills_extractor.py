# Thin wrapper for skills extraction using the Gemini-based matcher
from matcher import match_resume

def initialize_nlp():
    """
    Dummy function for backwards compatibility.
    No local NLP models to load now since we use the Gemini API.
    """
    pass

def extract_skills(text: str) -> dict:
    """
    Extracts skills by calling the unified match_resume function.
    Returns:
    - 'matched_skills': flat list of display names
    - 'by_category': dictionary mapping categories to lists of matched skills
    """
    analysis = match_resume(text)
    return analysis["skills_extracted"]
