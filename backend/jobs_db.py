# Mock database of job listings for the Resume Analyzer

JOBS = [
    {
        "id": 1,
        "title": "Machine Learning Engineer",
        "company": "DeepScale AI",
        "location": "San Francisco, CA (Hybrid)",
        "department": "AI/ML",
        "salary_range": "$130,000 - $170,000",
        "description": "We are seeking a Machine Learning Engineer to design, build, and deploy production-grade ML models. You will work on scaling our deep learning infrastructure, optimizing model inference times, and integrating models into our core SaaS product. Experience with LLMs, PyTorch, and cloud deployment is highly valued.",
        "skills_required": [
            "Python", "PyTorch", "TensorFlow", "Scikit-Learn", "Machine Learning", 
            "Deep Learning", "SQL", "Docker", "AWS", "Git", "Kubernetes", "Transformers"
        ]
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "company": "DataVibe Analytics",
        "location": "New York, NY (Remote)",
        "department": "Data Science",
        "salary_range": "$115,000 - $145,000",
        "description": "Join our analytics team to uncover actionable insights from complex multi-source datasets. In this role, you will build predictive models, run A/B tests, design statistical experiments, and present key metrics to leadership. You should have strong skills in data visualization, exploratory data analysis, and predictive modeling.",
        "skills_required": [
            "Python", "R", "SQL", "Pandas", "NumPy", "Scikit-Learn", "Data Visualization",
            "Tableau", "Statistics", "A/B Testing", "Machine Learning", "Matplotlib"
        ]
    },
    {
        "id": 3,
        "title": "NLP Research Scientist",
        "company": "SemanticWeb Corp",
        "location": "Boston, MA (On-site)",
        "department": "AI/ML",
        "salary_range": "$140,000 - $185,000",
        "description": "We are looking for an NLP Scientist to push the boundaries of natural language understanding and generation. You will train large-scale language models, design custom retrieval-augmented generation (RAG) pipelines, and implement advanced text parsing algorithms. Deep understanding of attention mechanisms and Hugging Face is required.",
        "skills_required": [
            "Python", "PyTorch", "NLP", "spaCy", "NLTK", "Hugging Face", "Transformers",
            "BERT", "GPT", "RAG", "Vector Databases", "Deep Learning", "LangChain"
        ]
    },
    {
        "id": 4,
        "title": "Full Stack Software Engineer (React & FastAPI)",
        "company": "SaaSify Systems",
        "location": "Austin, TX (Hybrid)",
        "department": "Software Engineering",
        "salary_range": "$110,000 - $150,000",
        "description": "We are hiring a Full Stack Engineer to lead development on our web applications. You will build clean user interfaces in React and implement robust APIs in Python using FastAPI. A strong understanding of modern web architectures, database design (PostgreSQL), and state management is key.",
        "skills_required": [
            "JavaScript", "TypeScript", "React", "HTML", "CSS", "Python", "FastAPI",
            "PostgreSQL", "REST APIs", "Git", "Docker", "Redux", "Tailwind CSS"
        ]
    },
    {
        "id": 5,
        "title": "Backend Systems Engineer",
        "company": "HyperGrid Technologies",
        "location": "Seattle, WA (Remote)",
        "department": "Software Engineering",
        "salary_range": "$125,000 - $165,000",
        "description": "Looking for a Backend Systems Engineer to architect and implement highly concurrent, low-latency microservices. You will work on distributed databases, messaging queues, and system integrations. Focus on writing clean, testable, and optimized code in Python/Go.",
        "skills_required": [
            "Python", "Go", "FastAPI", "Docker", "Kubernetes", "Redis", "Kafka",
            "PostgreSQL", "gRPC", "Microservices", "Git", "CI/CD", "Distributed Systems"
        ]
    },
    {
        "id": 6,
        "title": "Frontend Developer",
        "company": "PixelPerfect UI",
        "location": "Los Angeles, CA (Remote)",
        "department": "Software Engineering",
        "salary_range": "$95,000 - $130,000",
        "description": "We are seeking a creative Frontend Developer to craft visually stunning, accessible, and performant web interfaces. You will work closely with design teams to translate Figma mockups into interactive React components. Mastery of CSS, responsive design, and animations is essential.",
        "skills_required": [
            "HTML", "CSS", "JavaScript", "TypeScript", "React", "Next.js", 
            "Figma", "Redux", "Sass", "Webpack", "Tailwind CSS", "Git"
        ]
    },
    {
        "id": 7,
        "title": "Cloud DevOps Engineer",
        "company": "InfraShield Solutions",
        "location": "Chicago, IL (Hybrid)",
        "department": "Infrastructure/DevOps",
        "salary_range": "$120,000 - $160,000",
        "description": "Join our infrastructure team to manage and scale our multi-cloud deployment environments. You will build and optimize CI/CD pipelines, manage infrastructure as code (Terraform), and secure our Kubernetes clusters. Strong scripting skills and familiarity with AWS/Azure are required.",
        "skills_required": [
            "AWS", "Terraform", "Docker", "Kubernetes", "CI/CD", "Linux", "Bash",
            "Python", "GitHub Actions", "Ansible", "Cloud Security", "Prometheus", "Grafana"
        ]
    },
    {
        "id": 8,
        "title": "Computer Vision Engineer",
        "company": "OpticAI Labs",
        "location": "San Jose, CA (On-site)",
        "department": "AI/ML",
        "salary_range": "$140,000 - $180,000",
        "description": "We are looking for a Computer Vision Engineer to work on object detection, image segmentation, and video tracking algorithms. You will train Convolutional Neural Networks (CNNs) and deploy them to edge devices. Experience with OpenCV and PyTorch is a must.",
        "skills_required": [
            "Python", "C++", "OpenCV", "PyTorch", "TensorFlow", "Deep Learning",
            "Computer Vision", "CNN", "YOLO", "Image Processing", "CUDA", "Docker"
        ]
    },
    {
        "id": 9,
        "title": "Data Analyst",
        "company": "RetailPulse Business",
        "location": "Atlanta, GA (Hybrid)",
        "department": "Data Science",
        "salary_range": "$80,000 - $105,000",
        "description": "We are hiring a Data Analyst to transform complex transactional data into business intelligence. You will write advanced SQL queries, design dynamic dashboards in Power BI/Tableau, and draft business recommendation reports. Strong logical thinking and storytelling with data is expected.",
        "skills_required": [
            "SQL", "Python", "Pandas", "Excel", "Tableau", "Power BI", 
            "Data Visualization", "Statistics", "Data Warehousing", "Reporting"
        ]
    },
    {
        "id": 10,
        "title": "AI Product Manager",
        "company": "SmartNode Inc",
        "location": "San Francisco, CA (On-site)",
        "department": "Product/AI",
        "salary_range": "$145,000 - $190,000",
        "description": "Define the vision and roadmap for our enterprise AI agents. In this role, you will work closely with AI research teams, software engineers, and customers to identify market needs, draft PRDs, and guide the development of generative AI applications. Experience with AI product lifecycles is key.",
        "skills_required": [
            "Product Management", "Agile", "Generative AI", "NLP", "Scrum",
            "Data Analysis", "Roadmapping", "UX Design", "SQL", "Market Research"
        ]
    },
    {
        "id": 11,
        "title": "Mechanical Design Engineer",
        "company": "Apex Engineering Group",
        "location": "Detroit, MI (Hybrid)",
        "department": "Mechanical Engineering",
        "salary_range": "$85,000 - $110,000",
        "description": "We are seeking a Mechanical Design Engineer to create detailed 3D CAD models, run finite element analysis (FEA), and prepare engineering drawings using SolidWorks. You will work on automotive components, analyze heat transfer, and coordinate prototype testing.",
        "skills_required": [
            "SolidWorks", "AutoCAD", "FEA", "Manufacturing", "GD&T", "ANSYS", "CAD", "Thermodynamics", "Fluid Mechanics"
        ]
    },
    {
        "id": 12,
        "title": "Civil Structural Engineer",
        "company": "BuildCorp Infrastructure",
        "location": "Chicago, IL (On-site)",
        "department": "Civil Engineering",
        "salary_range": "$90,000 - $120,000",
        "description": "Join our structural team to perform load calculations, analyze steel and concrete frames, and design resilient foundations. You will model structures using STAAD.Pro and Revit, and collaborate with construction managers to ensure project execution.",
        "skills_required": [
            "Structural Analysis", "AutoCAD", "STAAD.Pro", "Concrete Design", "Steel Design", "Revit", "Construction Management", "Surveying"
        ]
    },
    {
        "id": 13,
        "title": "Electrical Systems Engineer",
        "company": "VoltEdge Power Solutions",
        "location": "Denver, CO (Hybrid)",
        "department": "Electrical Engineering",
        "salary_range": "$95,000 - $125,000",
        "description": "We are hiring an Electrical Systems Engineer to design circuits, create PCB layouts, and program PLCs for industrial automation. You will work with Altium Designer, test microcontrollers, and analyze power distributions using MATLAB.",
        "skills_required": [
            "Circuit Design", "PCB Design", "Altium Designer", "PLC", "Microcontrollers", "MATLAB", "Control Systems", "Arduino", "Oscilloscope"
        ]
    },
    {
        "id": 14,
        "title": "Chemical Process Engineer",
        "company": "ChemFlow Refining",
        "location": "Houston, TX (On-site)",
        "department": "Chemical Engineering",
        "salary_range": "$100,000 - $135,000",
        "description": "Seeking a Chemical Process Engineer to design, simulate, and refine chemical processes. You will perform mass and energy balances, design P&ID schematics, select equipment, and ensure adherence to chemical safety standards using Aspen Plus.",
        "skills_required": [
            "Process Simulation", "Aspen Plus", "Chemical Safety", "P&ID", "Mass Balance", "Thermodynamics", "Excel"
        ]
    }
]
