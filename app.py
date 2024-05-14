import streamlit as st

# HTML content for the personal website
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Kgotso's Personal Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f5f5f5;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        .banner {
            width: 100%;
            border-radius: 8px;
        }
        .profile-pic {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-top: -75px;
            border: 5px solid #fff;
        }
        .header {
            text-align: center;
            margin-bottom: 40px;
        }
        .experience, .education {
            margin-bottom: 40px;
        }
        .experience-item, .education-item {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://media.licdn.com/dms/image/D5616AQFU7V0o3hyh2w/profile-displaybackgroundimage-shrink_350_1400/0/1675699695999?e=1721260800&v=beta&t=e3YaSJADRMn4hExJeC-rGkSdToBVEouyzre3xfbKQLw" alt="Banner" class="banner">
            <img src="https://media.licdn.com/dms/image/C5603AQF3fwvIdxcMkQ/profile-displayphoto-shrink_800_800/0/1644348770230?e=1721260800&v=beta&t=v6XMYI65RxP1Rpb7U7aboiHXgFyXwZY3OvwpPzQ8Wxc" alt="Profile Picture" class="profile-pic">
            <h1>Kgotso Phela</h1>
            <p>Data Scientist | Software Engineer | Python | SQL | API's | Angular</p>
        </div>
        <div class="experience">
            <h2>Experience</h2>
            <div class="experience-item">
                <h3>Nerdma - Machine Learning & Software Engineer</h3>
                <p><em>Aug 2023 - Present (10 mos)</em></p>
                <p>Remote</p>
                <ul>
                    <li>Back-end Development: Building scalable and reliable back-end systems using Flask, and sometimes Java-Spring-boot, to deliver high-performance APIs and web services.</li>
                    <li>Front-end Development: Skilled in crafting intuitive and responsive user interfaces using Angular to create seamless user experiences.</li>
                    <li>Machine Learning: Experienced in harnessing the capabilities of state-of-the-art machine learning models, including Large Language Models (LLMs), to extract valuable insights and automate tasks.</li>
                    <li>Natural Language Processing (NLP): Utilize NLP techniques to analyze and understand text data, enabling intelligent information retrieval and document processing.</li>
                    <li>Tool Proficiency: Familiar with tools such as Llama, OpenAI, Chroma, and Langchain to enhance productivity and streamline workflows in machine learning and software development projects.</li>
                    <li>Responsibilities:</li>
                    <ul>
                        <li>Collaborate with cross-functional teams to design, develop, and deploy machine learning-powered applications and services.</li>
                        <li>Architect and implement backend systems using Flask, ensuring scalability, security, and maintainability of the software.</li>
                        <li>Design and implement intuitive user interfaces using Angular, focusing on delivering engaging user experiences.</li>
                        <li>Integrate machine learning models into software solutions to automate tasks, extract insights, and enhance decision-making processes.</li>
                        <li>Conduct research and experimentation with various machine learning algorithms and techniques to address business challenges effectively.</li>
                        <li>Stay updated on the latest developments in machine learning, software engineering, and related technologies to drive continuous improvement and innovation.</li>
                    </ul>
                </ul>
            </div>
            <div class="experience-item">
                <h3>Lubanzi ICT Consulting - Data Scientist</h3>
                <p><em>Feb 2023 - Aug 2023 (7 mos)</em></p>
                <p>South Africa (Hybrid)</p>
                <ul>
                    <li>Identify valuable data sources and automate collection processes.</li>
                    <li>Undertake pre-processing of structured and unstructured data.</li>
                    <li>Analyze large amounts of information to discover trends and patterns.</li>
                    <li>Build predictive models and machine-learning algorithms.</li>
                    <li>Combine models through ensemble modelling.</li>
                    <li>Present information using data visualization techniques.</li>
                    <li>Propose solutions and strategies to business challenges.</li>
                    <li>Collaborate with engineering and product development teams.</li>
                </ul>
            </div>
            <div class="experience-item">
                <h3>Deviare - Data Scientist</h3>
                <p><em>Jul 2022 - Dec 2022 (6 mos)</em></p>
                <p>South Africa</p>
                <ul>
                    <li>Gathering and analyzing data from various sources to create meaningful insights and reports.</li>
                    <li>Developing and maintaining data models and connections to data sources.</li>
                    <li>Designing and building interactive dashboards and visualizations that effectively communicate insights to stakeholders.</li>
                    <li>Collaborating with other teams to gather requirements and provide recommendations for data-driven decision making.</li>
                </ul>
            </div>
            <div class="experience-item">
                <h3>ExploreAI - Junior Data Scientist</h3>
                <p><em>Jul 2021 - Jun 2022 (1 yr)</em></p>
                <p>Johannesburg Metropolitan Area</p>
                <ul>
                    <li>Data Collection, Cleaning, Manipulation and Analytics using Python, PySpark and SQL together with visualization tools such as Matplotlib, Seaborn, and Plotly.</li>
                    <li>Built dashboards using Power BI.</li>
                    <li>Built machine learning models to predict various target variables (e.g., 3-hourly load shortfall or load shedding with regression, sentiment analysis and classification on global warming using Twitter data, and building a movie recommender engine).</li>
                </ul>
            </div>
            <div class="experience-item">
                <h3>Department of Basic Education - Labour Relations Intern</h3>
                <p><em>Nov 2020 - Oct 2021 (1 yr)</em></p>
                <p>Pretoria, Gauteng, South Africa</p>
                <ul>
                    <li>Attended and observed disciplinary, grievance, and counselling hearings.</li>
                    <li>Chaired disciplinary hearings with Senior consultant supervision.</li>
                    <li>Travelled extensively to deliver Audi Letters to the accused in different schools and conducted investigations on reported labour cases.</li>
                    <li>Interpreted during hearings (Northern Sotho to English and English to Northern Sotho).</li>
                    <li>Worked closely with HR to implement sanctions.</li>
                    <li>Did administrative duties for Labour Relations unit.</li>
                </ul>
            </div>
            <div class="experience-item">
                <h3>Department of Basic Education - Data Capturer & Learner Transport Monitor</h3>
                <p><em>Aug 2020 - Oct 2020 (3 mos)</em></p>
                <ul>
                    <li>Collected data from my disinfection point in terms of learner transport disinfection due to Covid-19.</li>
                    <li>Received data from other disinfection point monitors and compiled an overall statistical report for the whole District (Tshwane South District).</li>
                </ul>
            </div>
        </div>
        <div class="education">
            <h2>Education</h2>
            <div class="education-item">
                <h3>ExploreAI Academy</h3>
                <p><em>Data Science (National Certificate Information Technology System Development), Information Technology (Jul 2021 - Jun 2022)</em></p>
                <ul>
                    <li>Data Preparation, Microsoft PowerPoint, and more skills.</li>
                </ul>
            </div>
            <div class="education-item">
                <h3>University of Limpopo</h3>
                <p><em>Bachelor of Arts in Criminology and Psychology (Jan 2017 - Nov 2019)</em></p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Streamlit app
st.set_page_config(page_title="Kgotso's Personal Website")
st.markdown(html_content, unsafe_allow_html=True)
