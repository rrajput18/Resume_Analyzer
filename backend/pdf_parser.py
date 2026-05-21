import io
from pypdf import PdfReader

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts and cleans text from PDF file bytes using the pypdf library.
    """
    try:
        pdf_file = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_file)
        text_content = []
        
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_content.append(page_text)
                
        # Combine pages and normalize spaces
        full_text = "\n".join(text_content)
        
        # Clean up excess empty lines and clean whitespaces
        lines = [line.strip() for line in full_text.splitlines()]
        cleaned_lines = [line for line in lines if line]
        
        return "\n".join(cleaned_lines)
    except Exception as e:
        print(f"Error parsing PDF file: {str(e)}")
        return ""
