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
    },
    {
        "id": 15,
        "title": "HVAC Design Engineer",
        "company": "Therma Corp",
        "location": "Phoenix, AZ (Hybrid)",
        "department": "Mechanical Engineering",
        "salary_range": "$80,000 - $105,000",
        "description": "We are seeking an HVAC Design Engineer to create heating, ventilation, and air conditioning system layouts. You will calculate heating and cooling loads, select equipment, perform duct designs using CAD software, and ensure compliance with building regulations.",
        "skills_required": [
            "CAD", "HVAC", "Heat Transfer", "Duct Design", "Load Calculations", "Thermodynamics", "Fluid Mechanics"
        ]
    },
    {
        "id": 16,
        "title": "Robotics & Automation Engineer",
        "company": "RoboTech Solutions",
        "location": "Pittsburgh, PA (On-site)",
        "department": "Mechanical Engineering",
        "salary_range": "$95,000 - $130,000",
        "description": "Join our robotics group to design and program robotic arms, pick-and-place systems, and automated guided vehicles (AGVs). You will integrate sensors, design pneumatic and hydraulic mechanisms, and program motion profiles using ROS and Python/C++.",
        "skills_required": [
            "Robotics", "Pneumatics", "Hydraulics", "ROS", "SolidWorks", "Python", "CAD", "Control Systems"
        ]
    },
    {
        "id": 17,
        "title": "Construction Project Manager",
        "company": "Summit Builders",
        "location": "Dallas, TX (Hybrid)",
        "department": "Civil Engineering",
        "salary_range": "$95,000 - $125,000",
        "description": "We are hiring a Construction Project Manager to oversee large commercial construction projects. You will develop project timelines, manage sub-contractors, monitor material estimations, ensure site safety compliance, and coordinate structural inspections.",
        "skills_required": [
            "Construction Management", "Estimation", "Scheduling", "Subcontractor Coordination", "AutoCAD", "Site Safety", "Budgeting"
        ]
    },
    {
        "id": 18,
        "title": "Geotechnical Engineer",
        "company": "EarthCore Consultants",
        "location": "Salt Lake City, UT (On-site)",
        "department": "Civil Engineering",
        "salary_range": "$85,000 - $110,000",
        "description": "Perform subsurface investigations, soil mechanics testing, and foundation analyses. You will write geotechnical reports, evaluate slope stability, recommend retaining wall designs, and use GIS databases to map ground conditions.",
        "skills_required": [
            "Geotechnical Engineering", "Soil Mechanics", "Foundation Design", "GIS", "Surveying", "AutoCAD"
        ]
    },
    {
        "id": 19,
        "title": "PCB Hardware Design Engineer",
        "company": "CircuitCraft Labs",
        "location": "San Jose, CA (Hybrid)",
        "department": "Electrical Engineering",
        "salary_range": "$105,000 - $140,000",
        "description": "Design multi-layer high-speed printed circuit boards (PCBs) for consumer electronics. You will select electronic components, perform schematic capture and PCB layout in Altium Designer, run signal integrity simulations, and debug prototypes using oscilloscopes.",
        "skills_required": [
            "PCB Design", "Circuit Design", "Altium Designer", "Signal Integrity", "Oscilloscope", "Microcontrollers", "Debugging"
        ]
    },
    {
        "id": 20,
        "title": "Automation & Controls Specialist",
        "company": "LogicFlow Controls",
        "location": "Cleveland, OH (Hybrid)",
        "department": "Electrical Engineering",
        "salary_range": "$90,000 - $115,000",
        "description": "Program and integrate programmable logic controllers (PLCs) and HMI interfaces for assembly line automation. You will design electrical control cabinets, select sensor networks, and troubleshoot industrial control systems on-site.",
        "skills_required": [
            "PLC", "Control Systems", "HMI Programming", "SCADA", "Electrical Troubleshooting", "Arduino", "MATLAB"
        ]
    },
    {
        "id": 21,
        "title": "Petroleum Refinery Engineer",
        "company": "RefineCo Energy",
        "location": "New Orleans, LA (On-site)",
        "department": "Chemical Engineering",
        "salary_range": "$110,000 - $145,000",
        "description": "Optimize crude distillation, catalytic cracking, and hydrotreating operations in a major oil refinery. You will perform mass balances, conduct process safety reviews (HAZOP), troubleshoot equipment malfunctions, and optimize energy efficiency using Aspen Plus.",
        "skills_required": [
            "Refining", "Chemical Safety", "Process Optimization", "Aspen Plus", "Mass Balance", "P&ID", "Thermodynamics"
        ]
    },
    {
        "id": 22,
        "title": "Business Development Manager",
        "company": "GrowthScale Partners",
        "location": "New York, NY (Hybrid)",
        "department": "Business & Management",
        "salary_range": "$95,000 - $130,000",
        "description": "Identify new B2B sales opportunities, forge strategic partnerships, and drive revenue growth. You will conduct market research, manage client acquisition pipelines, deliver sales presentations, and coordinate closely with product marketing teams.",
        "skills_required": [
            "Business Development", "Client Relations", "Market Research", "Negotiation", "Sales Strategy", "CRM", "Presentation"
        ]
    },
    {
        "id": 23,
        "title": "Operations & Logistics Manager",
        "company": "GlobalLogistics Group",
        "location": "Miami, FL (On-site)",
        "department": "Business & Management",
        "salary_range": "$85,000 - $115,000",
        "description": "Manage warehouse operations, distribution channels, and inventory logistics. You will streamline supply chain workflows, negotiate freight contracts, manage logistics staff, and implement data-driven process optimization strategies.",
        "skills_required": [
            "Operations Management", "Supply Chain", "Logistics", "Inventory Management", "Process Optimization", "Budgeting", "Excel"
        ]
    },
    {
        "id": 24,
        "title": "Financial Planning & Analysis Specialist",
        "company": "CapitalInvest Corp",
        "location": "Charlotte, NC (Hybrid)",
        "department": "Finance & Accounting",
        "salary_range": "$90,000 - $120,000",
        "description": "Build financial models, forecast quarterly revenues, and analyze budget variances. You will support leadership with financial planning, perform capital structure analysis, and compile periodic corporate financial reports using Excel and ERP software.",
        "skills_required": [
            "Financial Analysis", "Financial Modeling", "Forecasting", "Budgeting", "Corporate Finance", "Excel", "Data Analysis"
        ]
    },
    {
        "id": 25,
        "title": "Human Resources Operations Manager",
        "company": "TalentSync Solutions",
        "location": "Atlanta, GA (Remote)",
        "department": "Human Resources",
        "salary_range": "$80,000 - $105,000",
        "description": "Lead HR operations, payroll configuration, and employee onboarding compliance. You will resolve employee relations inquiries, administer corporate benefit programs, and update HR policy handbooks in accordance with state and federal labor laws.",
        "skills_required": [
            "Human Resources", "Onboarding", "Employee Relations", "Payroll", "Labor Law Compliance", "Conflict Resolution", "Performance Management"
        ]
    },
    {
        "id": 26,
        "title": "Biomedical Design Engineer",
        "company": "MedTech Instruments",
        "location": "Minneapolis, MN (Hybrid)",
        "department": "Healthcare & Biomedical",
        "salary_range": "$90,000 - $120,000",
        "description": "Design and test innovative medical devices, surgical tools, and health monitoring sensors. You will create 3D CAD assemblies, conduct biocompatibility testing, perform mechanical stress simulations, and compile FDA regulatory compliance documentation.",
        "skills_required": [
            "Biomedical Engineering", "Medical Devices", "Biocompatibility", "FDA Regulations", "SolidWorks", "CAD", "Testing"
        ]
    },
    {
        "id": 27,
        "title": "Clinical Research Associate",
        "company": "Pathology Research Labs",
        "location": "Philadelphia, PA (On-site)",
        "department": "Healthcare & Biomedical",
        "salary_range": "$75,000 - $100,000",
        "description": "Monitor and coordinate clinical trial projects in accordance with Good Clinical Practice guidelines. You will review case report forms, audit clinical trial sites, track patient enrollment milestones, and manage data compliance logs.",
        "skills_required": [
            "Clinical Trials", "GCP Guidelines", "Clinical Research", "Data Compliance", "Regulatory Affairs", "Medical Terminology"
        ]
    }
]
