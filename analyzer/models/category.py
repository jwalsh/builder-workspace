import ast
import inspect
import sys
from enum import Enum

import astor


class CategoryEnum(str, Enum):
    UNKNOWN = "Unclassified or unknown category."
    AI_ML = (
        "Artificial intelligence and machine learning technologies and applications."
    )
    AUTOMATION = "Systems automating complex tasks across various industries."
    AUTONOMOUS_SYSTEMS = (
        "Technologies for autonomous vehicles, drones, and self-operating systems."
    )
    BIOTECH = "Biotechnology, genetic engineering, and biocomputing applications."
    BLOCKCHAIN = "Solutions enhancing blockchain applications and security."
    DOCUMENTATION = "Tools for generating and maintaining technical documentation."
    EDUCATION = "Solutions aimed at education and personalized learning paths."
    ENERGY = "Energy production, distribution, and optimization technologies."
    ENVIRONMENTAL = (
        "Environmental protection and climate change mitigation technologies."
    )
    FINANCE = "Applications for financial analysis, fraud detection, and predictions."
    FORENSICS = "Applied to digital forensics and investigative analysis."
    GAMING = "Technologies used in gaming, simulations, and interactive experiences."
    HCI = "Human-computer interaction and advanced user interfaces."
    HEALTHCARE = "Applications improving healthcare diagnostics and patient care."
    HR = "Human Resources technologies for workforce management and development."
    INFRASTRUCTURE = (
        "Innovations in construction, infrastructure, and system architecture."
    )
    IOT = "Internet of Things technologies for interconnected smart systems."
    LOGISTICS = "Optimizing supply chain, transport, and logistics."
    MARKETING = "Technologies for marketing, customer insights, and personalization."
    ORCHESTRATION = "Tools for orchestrating processes and services across platforms."
    QUANTUM = "Quantum computing innovations and applications."
    REAL_ESTATE = "Tools for managing and analyzing real estate and housing markets."
    SECURITY = "Solutions for enhancing security measures, including cybersecurity."
    SOCIAL_MEDIA = "Platforms for social networking, community building, and digital communication."
    SPACE = "Space exploration, satellite systems, and related technologies."
    SUSTAINABILITY = "Solutions for sustainable development and energy optimization."
    TRANSPORT = "Transportation systems and mobility solutions."
    TRAVEL = "Technologies related to travel, tourism, and hospitality industries."
    XR = "Extended reality technologies, including VR, AR, and MR experiences."
    ADVANCED_MATERIALS = "Nanomaterials, metamaterials, and smart materials with programmable properties."
    AGRICULTURAL = "Agtech including precision farming, vertical farming, agri-robotics, and AI crop management."
    ALGORITHMS_AND_ARCHITECTURES = (
        "Advanced algorithms, quantum computing, and novel computational paradigms."
    )
    BCI = "Brain-computer interfaces for direct communication between the brain and external devices."
    BIO_ENHANCEMENT = "Biotech for human enhancement, including genetic engineering and synthetic biology."
    CLOUD = "Cloud computing infrastructure, PaaS, SaaS, and related distributed computing technologies."
    COGNITIVE_ENHANCEMENT = "Brain-computer interfaces, neurofeedback systems, and cognitive training tools."
    COMMUNICATIONS = "Advanced telecom, 5G and beyond, satellite comms, and emerging network protocols."
    ENTERTAINMENT = "Entertainment and education tech, from interactive media and gaming to e-learning platforms."
    HUMAN_AUGMENTATION = (
        "AI-powered systems for enhancing human capabilities and decision-making."
    )
    IMMERSIVE = (
        "VR, AR, MR, and other technologies blending digital and physical worlds."
    )
    INTEGRATION = "Cross-account integration for seamless data and process integration across systems."
    INTERNET = "Web technologies, internet protocols, CDNs, and internet infrastructure innovations."
    LEGAL = "Legal tech for contract analysis, compliance, research, and AI-assisted legal services."
    MANUFACTURING = "Advanced manufacturing tech including smart factories, 3D printing, robotics, and Industry 4.0."
    MILITARY = "Defense tech including advanced weapons, cybersecurity, and military AI applications."
    MIND_INTERFACES = "Direct neural interfaces, thought-controlled devices, and brain-computer interaction systems."
    NEURAL_INTERFACES = "Technologies connecting the human nervous system with external devices or systems."
    PERSONAL_ENHANCEMENT = "Wearables, health tracking, cognitive training, and lifestyle optimization tools."
    PHILOSOPHY = (
        "Ethical frameworks and philosophical implications of advanced technologies."
    )
    RENEWABLE_ENERGY = "Sustainable energy solutions including solar, wind, geothermal, and energy storage."
    SIMULATION = "Engineering and simulation tech for modeling, digital twins, and virtual testing environments."
    SOFTWARE_ENGINEERING = "App development tech, languages, frameworks, DevOps tools, and software engineering practices."
    URBAN = "Smart city tech, intelligent transportation, urban planning, and smart infrastructure."
    VIRTUALIZATION = "Virtual and cloud computing, including server virtualization and container technologies."
    WEARABLE = "Smart watches, fitness trackers, AR glasses, and other body-worn smart devices."
    SCIENCE = "Engineering and scientific research technologies, including advanced laboratory equipment, data analysis tools for scientific research, simulation software for complex scientific phenomena, and innovations in experimental design and execution. This category covers technologies that accelerate scientific discovery, enhance research methodologies, and bridge the gap between theoretical and applied sciences across various disciplines such as physics, chemistry, biology, and interdisciplinary fields."
    PRODUCTIVITY = "Personal productivity tools and technologies, encompassing task management systems, time-tracking applications, focus-enhancing software, collaborative platforms, and smart personal assistants. This category includes innovations aimed at optimizing individual and team productivity, streamlining workflows, reducing cognitive load, and enhancing decision-making processes in both personal and professional contexts."
    INNOVATION = "Innovation-driven technologies, including idea generation systems, predictive innovation platforms, advanced design tools, and technologies that facilitate creative problem-solving. This category covers applications that augment human creativity, accelerate the innovation process, identify emerging trends and opportunities, and enable rapid prototyping and testing of new concepts across various industries and domains."
    WELLBEING = "Technologies for personal and community wellbeing, including mental health support systems, meditation and mindfulness apps, personalized health and fitness coaches, and community health management platforms. This category encompasses innovations that improve physical, mental, and emotional health, promote work-life balance, and enhance overall quality of life for individuals and communities."
    ACCESSIBILITY = "Advanced accessibility solutions, including adaptive interfaces, real-time translation and captioning systems, navigation aids for the visually impaired, and cognitive assistance tools. This category covers technologies that break down barriers for people with disabilities, enhance digital and physical accessibility, and promote inclusive design in products, services, and environments."
    ARTS = "Art and culture technologies, including computer-assisted creative tools, digital art platforms, cultural heritage preservation systems, and immersive cultural experiences. This category encompasses innovations that blend technology with artistic expression, facilitate cultural exchange, preserve and digitize cultural artifacts, and create new forms of interactive and generative art."
    PETS = "Pet care and animal welfare technologies, including smart pet health monitoring systems, automated pet care devices, behavior analysis tools for animals, and platforms for pet services. This category covers innovations that enhance the well-being of pets and other animals, assist pet owners in providing better care, and advance veterinary medicine and animal science."
    RETAIL = "Retail automation and smart shopping technologies, including intelligent inventory management systems, personalized shopping assistants, automated checkout solutions, and predictive demand forecasting tools. This category encompasses innovations that transform the retail experience, optimize supply chain operations, enhance customer engagement, and enable data-driven decision-making in the retail sector."
    CONSTRUCTION = "Advanced technologies for building design, construction processes, and infrastructure development."
    MUSIC = "Innovative technologies for music creation, production, distribution, and interactive experiences."


def show_categories():
    categories = [
        category.name for category in CategoryEnum if category != CategoryEnum.UNKNOWN
    ]
    print("Available categories:")
    for category in categories:
        print(f"- {category}")


def update_category_enum(new_categories):
    global CategoryEnum
    module = ast.parse(inspect.getsource(sys.modules[__name__]))
    enum_class = next(
        (
            node
            for node in module.body
            if isinstance(node, ast.ClassDef) and node.name == "CategoryEnum"
        ),
        None,
    )
    if enum_class:
        existing_categories = {
            node.targets[0].id: node.value.s
            for node in enum_class.body
            if isinstance(node, ast.Assign)
        }
        for category in new_categories:
            if category not in existing_categories:
                new_assign = ast.Assign(
                    targets=[ast.Name(id=category, ctx=ast.Store())],
                    value=ast.Str(s=f"New category: {category}"),
                )
                enum_class.body.append(new_assign)
        new_enum_dict = {name: value for name, value in existing_categories.items()}
        new_enum_dict.update(
            {
                category: f"New category: {category}"
                for category in new_categories
                if category not in existing_categories
            }
        )
        CategoryEnum = Enum("CategoryEnum", new_enum_dict)
        updated_source = astor.to_source(module)
        with open(__file__, "w") as file:
            file.write(updated_source)
        print(f"CategoryEnum updated with new categories: {', '.join(new_categories)}")
    else:
        print("Error: CategoryEnum not found in the source code.")
