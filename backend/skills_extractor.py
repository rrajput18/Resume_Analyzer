import spacy
from spacy.matcher import PhraseMatcher

# A comprehensive list of skills categorized for analysis
SKILL_CATEGORIES = {
    "Programming Languages": [
        "Python", "JavaScript", "TypeScript", "Go", "C++", "C#", "Java", "R", 
        "Ruby", "PHP", "Rust", "Swift", "Kotlin", "Bash", "SQL", "HTML", "CSS"
    ],
    "Machine Learning & AI": [
        "Machine Learning", "Deep Learning", "NLP", "Natural Language Processing",
        "Computer Vision", "Neural Networks", "CNN", "RNN", "Transformers", 
        "LLMs", "Large Language Models", "Generative AI", "RAG", "A/B Testing", 
        "Statistics", "Linear Algebra", "Reinforcement Learning", "OpenCV", 
        "Vector Databases", "LangChain", "BERT", "GPT", "YOLO"
    ],
    "Frameworks & Libraries": [
        "PyTorch", "TensorFlow", "Scikit-Learn", "Pandas", "NumPy", "Keras", 
        "Hugging Face", "spaCy", "NLTK", "React", "React.js", "Next.js", 
        "FastAPI", "Django", "Flask", "Express", "Angular", "Vue", "Redux", 
        "Tailwind CSS", "Bootstrap", "Sass", "Matplotlib", "Seaborn"
    ],
    "Databases & Tools": [
        "PostgreSQL", "MySQL", "SQLite", "MongoDB", "Redis", "Kafka", 
        "Elasticsearch", "Neo4j", "Tableau", "Power BI", "Figma", "Git", 
        "GitHub", "Docker", "Kubernetes", "Ansible", "Terraform", "AWS", 
        "GCP", "Google Cloud", "Azure", "Jenkins", "CI/CD", "Apache Spark", 
        "Hadoop", "Excel"
    ],
    "Concepts & Methodologies": [
        "Agile", "Scrum", "Product Management", "REST APIs", "GraphQL", 
        "Microservices", "gRPC", "Distributed Systems", "Cloud Security", 
        "System Design", "Data Warehousing", "Data Visualization", "Reporting",
        "Market Research", "Roadmapping", "UX Design"
    ],
    "Mechanical Engineering": [
        "CAD", "SolidWorks", "FEA", "Finite Element Analysis", "Manufacturing", 
        "GD&T", "ANSYS", "Thermodynamics", "Fluid Mechanics", "HVAC", "Heat Transfer",
        "Robotics", "Pneumatics", "Hydraulics"
    ],
    "Civil Engineering": [
        "Structural Analysis", "AutoCAD", "STAAD.Pro", "Concrete Design", 
        "Steel Design", "Revit", "Construction Management", "Surveying", 
        "Geotechnical Engineering", "GIS", "Hydraulics", "Estimation"
    ],
    "Electrical Engineering": [
        "Circuit Design", "PCB Design", "Altium Designer", "MATLAB", 
        "Microcontrollers", "PLC", "Control Systems", "Arduino", 
        "Power Systems", "Signal Processing", "FPGA", "VHDL", "Verilog", "Oscilloscope"
    ],
    "Chemical Engineering": [
        "Process Simulation", "Aspen Plus", "Chemical Safety", "P&ID", 
        "Mass Balance", "Energy Balance", "Reaction Kinetics", "Refining", 
        "Process Optimization"
    ]
}

# Flatten list for general matcher lookup
ALL_SKILLS = []
for skills in SKILL_CATEGORIES.values():
    ALL_SKILLS.extend(skills)

# Create a mapping from lowercase skill to the display name
SKILL_MAP = {skill.lower(): skill for skill in ALL_SKILLS}

# Custom normalization map to group variations (e.g., "react.js" and "react" can both map to "React")
SKILL_NORMALIZATION = {
    "react.js": "React",
    "reactjs": "React",
    "natural language processing": "NLP",
    "large language models": "LLMs",
    "google cloud": "GCP",
    "scikit-learn": "Scikit-Learn",
    "scikitlearn": "Scikit-Learn",
    "tailwind css": "Tailwind CSS",
    "tailwindcss": "Tailwind CSS",
}

nlp = None
matcher = None

def initialize_nlp():
    """
    Initializes spaCy model and configures the PhraseMatcher.
    """
    global nlp, matcher
    if nlp is not None:
        return
        
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        # Fallback to blank model if not downloaded yet
        nlp = spacy.blank("en")
        
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    
    # Add skills patterns to the matcher
    for skill in ALL_SKILLS:
        patterns = [nlp.make_doc(skill)]
        matcher.add(skill, patterns)

def extract_skills(text: str) -> dict:
    """
    Parses the text and extracts skills using spaCy PhraseMatcher.
    Returns a dictionary with:
    - 'matched_skills': flat list of display names
    - 'by_category': dictionary mapping categories to lists of matched skills
    """
    initialize_nlp()
    
    doc = nlp(text)
    matches = matcher(doc)
    
    matched_skills = set()
    
    for match_id, start, end in matches:
        span = doc[start:end]
        raw_match = span.text.lower()
        
        # Resolve display name
        display_name = SKILL_MAP.get(raw_match, span.text)
        
        # Apply normalization (e.g. react.js -> React)
        normalized_name = SKILL_NORMALIZATION.get(display_name.lower(), display_name)
        matched_skills.add(normalized_name)
        
    # Categorize matched skills
    categorized = {category: [] for category in SKILL_CATEGORIES.keys()}
    
    for skill in matched_skills:
        # Find which category this skill belongs to
        found = False
        for category, list_of_skills in SKILL_CATEGORIES.items():
            # Check normal list or normalization matches
            normalized_list = [SKILL_NORMALIZATION.get(s.lower(), s).lower() for s in list_of_skills]
            if skill.lower() in normalized_list:
                # Add the proper display name to the category
                # Find display name from original list
                for orig_skill in list_of_skills:
                    norm_orig = SKILL_NORMALIZATION.get(orig_skill.lower(), orig_skill)
                    if norm_orig.lower() == skill.lower():
                        categorized[category].append(norm_orig)
                        found = True
                        break
            if found:
                break
                
    # Filter out empty categories
    categorized = {k: sorted(list(set(v))) for k, v in categorized.items() if v}
    
    return {
        "matched_skills": sorted(list(matched_skills)),
        "by_category": categorized
    }
