import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Manohar | Mechanical Engineering Portfolio",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html {
    scroll-behavior: smooth;
}

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(37,99,235,0.20), transparent 25%),
        radial-gradient(circle at 90% 90%, rgba(124,58,237,0.18), transparent 25%),
        #050816;
    color: white;
}

/* Remove Streamlit default top space */
.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* Main headings */
.hero-title {
    font-size: 70px;
    font-weight: 800;
    line-height: 1.05;
    margin-bottom: 10px;
}

.hero-title span {
    color: #60a5fa;
}

.hero-subtitle {
    font-size: 25px;
    font-weight: 600;
    color: #cbd5e1;
    margin-bottom: 20px;
}

.hero-description {
    font-size: 17px;
    color: #94a3b8;
    line-height: 1.8;
    max-width: 700px;
}

/* Section titles */
.section-title {
    font-size: 40px;
    font-weight: 800;
    margin-top: 70px;
    margin-bottom: 8px;
}

.section-title span {
    color: #60a5fa;
}

.section-description {
    color: #94a3b8;
    margin-bottom: 35px;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 28px;
    margin-bottom: 20px;
    transition: 0.3s;
    height: 100%;
}

.card:hover {
    border-color: rgba(96,165,250,0.55);
    box-shadow: 0 15px 45px rgba(0,0,0,0.25);
    transform: translateY(-5px);
}

.card h3 {
    color: white;
    margin-bottom: 12px;
}

.card p {
    color: #94a3b8;
    line-height: 1.7;
}

/* Project cards */
.project-card {
    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 25px;
    min-height: 350px;
    transition: 0.3s;
}

.project-card:hover {
    transform: translateY(-7px);
    border-color: #60a5fa;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}

.project-icon {
    font-size: 55px;
    margin-bottom: 15px;
}

.project-card h3 {
    color: white;
}

.project-card p {
    color: #94a3b8;
    line-height: 1.7;
}

/* Tags */
.tag {
    display: inline-block;
    padding: 6px 12px;
    margin: 4px 4px 4px 0;
    border-radius: 20px;
    background: rgba(96,165,250,0.10);
    border: 1px solid rgba(96,165,250,0.25);
    color: #93c5fd;
    font-size: 12px;
}

/* Hero card */
.hero-card {
    background: linear-gradient(
        145deg,
        rgba(37,99,235,0.15),
        rgba(124,58,237,0.10)
    );

    border: 1px solid rgba(96,165,250,0.2);
    border-radius: 25px;
    padding: 45px;
}

/* Gear */
.gear {
    font-size: 150px;
    text-align: center;
    animation: spin 12s linear infinite;
    filter: drop-shadow(0 0 25px rgba(96,165,250,0.35));
}

@keyframes spin {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}

/* Skill bars */
.skill-name {
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
    color: #e2e8f0;
}

.progress-container {
    background: #1e293b;
    border-radius: 20px;
    height: 9px;
    overflow: hidden;
    margin-bottom: 20px;
}

.progress-bar {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        #2563eb,
        #60a5fa
    );
}

/* Stats */
.stat-card {
    text-align: center;
    padding: 25px;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 15px;
}

.stat-number {
    font-size: 35px;
    font-weight: 800;
    color: #60a5fa;
}

.stat-text {
    color: #94a3b8;
}

/* Buttons */
div.stButton > button,
div.stDownloadButton > button {
    border-radius: 10px;
    border: 1px solid #60a5fa;
    background: #2563eb;
    color: white;
    font-weight: 600;
    padding: 10px 20px;
    transition: 0.3s;
}

div.stButton > button:hover,
div.stDownloadButton > button:hover {
    background: #1d4ed8;
    border-color: #93c5fd;
}

/* Navigation */
.nav-box {
    text-align: center;
    padding: 12px;
    margin-bottom: 25px;
    background: rgba(5,8,22,0.7);
    border-bottom: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
}

.nav-box a {
    color: #cbd5e1;
    text-decoration: none;
    margin: 0 12px;
    font-size: 14px;
}

.nav-box a:hover {
    color: #60a5fa;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    padding: 45px 10px 10px 10px;
    margin-top: 70px;
    border-top: 1px solid rgba(255,255,255,0.08);
}

.footer span {
    color: #60a5fa;
}

/* Mobile */
@media (max-width: 768px) {

    .hero-title {
        font-size: 45px;
    }

    .hero-subtitle {
        font-size: 20px;
    }

    .section-title {
        font-size: 32px;
    }

    .hero-card {
        padding: 25px;
    }

    .gear {
        font-size: 100px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("""
<div class="nav-box">

<a href="#home">Home</a>
<a href="#about">About</a>
<a href="#skills">Skills</a>
<a href="#projects">Projects</a>
<a href="#achievements">Achievements</a>
<a href="#resume">Resume</a>
<a href="#contact">Contact</a>

</div>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.6, 1])

with col1:

    st.markdown("""
    <div class="hero-card">

        <p style="color:#60a5fa;font-size:18px;">
            Hello, I'm
        </p>

        <div class="hero-title">
            Manohar<span>.</span>
        </div>

        <div class="hero-subtitle">
            Mechanical Engineering Student
        </div>

        <p class="hero-description">
            I am a 2nd-year Mechanical Engineering student at
            SR University, passionate about CAD design, 3D modelling,
            manufacturing, product development and innovative
            engineering projects.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    b1, b2 = st.columns(2)

    with b1:
        if st.button("⚙️ View My Projects", use_container_width=True):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=#projects">',
                unsafe_allow_html=True
            )

    with b2:
        if st.button("📧 Contact Me", use_container_width=True):
            st.markdown(
                '<meta http-equiv="refresh" content="0; url=#contact">',
                unsafe_allow_html=True
            )


with col2:

    st.markdown("""
    <div class="hero-card" style="
        height:100%;
        display:flex;
        justify-content:center;
        align-items:center;
    ">

        <div>

            <div class="gear">
                ⚙️
            </div>

            <h3 style="
                text-align:center;
                color:#60a5fa;
            ">
                ENGINEER
            </h3>

            <p style="
                text-align:center;
                color:#94a3b8;
            ">
                Design • Build • Innovate
            </p>

        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# QUICK STATS
# =========================================================

st.write("")
st.write("")

s1, s2, s3, s4 = st.columns(4)

with s1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">2nd</div>
        <div class="stat-text">Year</div>
    </div>
    """, unsafe_allow_html=True)

with s2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">3+</div>
        <div class="stat-text">Projects</div>
    </div>
    """, unsafe_allow_html=True)

with s3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">CAD</div>
        <div class="stat-text">Design</div>
    </div>
    """, unsafe_allow_html=True)

with s4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">🏆</div>
        <div class="stat-text">Semester Topper</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ABOUT
# =========================================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">About <span>Me</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'My education, interests and engineering goals'
    '</div>',
    unsafe_allow_html=True
)

about1, about2 = st.columns(2)

with about1:

    st.markdown("""
    <div class="card">

        <h3>👨‍🎓 Who I Am</h3>

        <p>
        I am a Mechanical Engineering student interested in
        practical engineering, CAD design and product development.
        </p>

        <p>
        I enjoy converting engineering concepts into physical
        designs and prototypes. I am currently improving my
        knowledge of Fusion 360, engineering drawing,
        manufacturing processes and programming.
        </p>

        <p>
        My goal is to develop strong technical skills and gain
        real-world industry experience through internships,
        projects and continuous learning.
        </p>

    </div>
    """, unsafe_allow_html=True)


with about2:

    st.markdown("""
    <div class="card">

        <h3>📋 Personal Details</h3>

        <p>
        <strong style="color:#60a5fa;">Name:</strong>
        Manohar
        </p>

        <p>
        <strong style="color:#60a5fa;">Branch:</strong>
        Mechanical Engineering
        </p>

        <p>
        <strong style="color:#60a5fa;">Year:</strong>
        2nd Year
        </p>

        <p>
        <strong style="color:#60a5fa;">University:</strong>
        SR University
        </p>

        <p>
        <strong style="color:#60a5fa;">Interests:</strong>
        CAD, 3D Modelling, Manufacturing
        </p>

        <p>
        <strong style="color:#60a5fa;">Career Goal:</strong>
        Engineering & Space Technology
        </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# SKILLS
# =========================================================

st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">My <span>Skills</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Technical skills I am currently developing'
    '</div>',
    unsafe_allow_html=True
)

skill1, skill2 = st.columns(2)

with skill1:

    skills = [
        ("Fusion 360", 75),
        ("Engineering Drawing", 80),
        ("AutoCAD", 65),
        ("Python", 60),
    ]

    for name, value in skills:

        st.markdown(
            f"""
            <div class="skill-name">
                <span>{name}</span>
                <span>{value}%</span>
            </div>

            <div class="progress-container">
                <div class="progress-bar"
                     style="width:{value}%">
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


with skill2:

    skill_cards = [
        ("⚙️", "CAD Design", "2D and 3D mechanical design"),
        ("🔧", "Manufacturing", "Manufacturing processes"),
        ("🧊", "3D Modelling", "Product and component modelling"),
        ("💻", "Programming", "Python and basic programming"),
    ]

    for icon, title, description in skill_cards:

        st.markdown(
            f"""
            <div class="card">

                <div style="font-size:35px;">
                    {icon}
                </div>

                <h3>{title}</h3>

                <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PROJECTS
# =========================================================

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">My <span>Projects</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Engineering projects and product ideas'
    '</div>',
    unsafe_allow_html=True
)

p1, p2, p3 = st.columns(3)


with p1:

    st.markdown("""
    <div class="project-card">

        <div class="project-icon">❄️</div>

        <h3>Passive Cooling Enclosure</h3>

        <p>
        A compact passive cooling enclosure designed using
        aluminium components for thermal management without
        relying on active cooling.
        </p>

        <span class="tag">Mechanical</span>
        <span class="tag">Thermal</span>
        <span class="tag">CAD</span>
        <span class="tag">Aluminium</span>

    </div>
    """, unsafe_allow_html=True)


with p2:

    st.markdown("""
    <div class="project-card">

        <div class="project-icon">👕</div>

        <h3>Portable Cloth Dryer</h3>

        <p>
        A foldable and portable cloth drying mechanism designed
        for efficient space utilisation and convenient mounting.
        </p>

        <span class="tag">Product Design</span>
        <span class="tag">Manufacturing</span>
        <span class="tag">Mechanism</span>

    </div>
    """, unsafe_allow_html=True)


with p3:

    st.markdown("""
    <div class="project-card">

        <div class="project-icon">🤖</div>

        <h3>AI Voice Car</h3>

        <p>
        A small physical AI voice robot concept using Raspberry Pi
        and ESP32, designed to move and respond to voice commands.
        </p>

        <span class="tag">Raspberry Pi</span>
        <span class="tag">ESP32</span>
        <span class="tag">Robotics</span>
        <span class="tag">AI</span>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ACHIEVEMENTS
# =========================================================

st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">'
    '<span>Achievements</span>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Academic achievements and milestones'
    '</div>',
    unsafe_allow_html=True
)

a1, a2, a3 = st.columns(3)

with a1:

    st.markdown("""
    <div class="card">

        <div style="font-size:50px;">🏆</div>

        <h3>Semester Topper</h3>

        <p>
        Received a Semester Topper Certificate from the
        Dean and Head of Department.
        </p>

    </div>
    """, unsafe_allow_html=True)


with a2:

    st.markdown("""
    <div class="card">

        <div style="font-size:50px;">🎓</div>

        <h3>Mechanical Engineering</h3>

        <p>
        Currently pursuing Mechanical Engineering at
        SR University.
        </p>

    </div>
    """, unsafe_allow_html=True)


with a3:

    st.markdown("""
    <div class="card">

        <div style="font-size:50px;">🚀</div>

        <h3>Engineering Projects</h3>

        <p>
        Developing practical engineering projects and
        improving CAD and design skills.
        </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# RESUME
# =========================================================

st.markdown('<div id="resume"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">My <span>Resume</span></div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card" style="text-align:center;">

    <h2>📄 My Resume</h2>

    <p>
    Download my resume to learn more about my education,
    skills, projects and achievements.
    </p>

</div>
""", unsafe_allow_html=True)

try:

    with open("resume.pdf", "rb") as file:

        st.download_button(
            label="📥 Download My Resume",
            data=file,
            file_name="Manohar_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

except FileNotFoundError:

    st.info(
        "Add your resume PDF to the project folder and name it "
        "'resume.pdf' to enable the download button."
    )


# =========================================================
# CONTACT
# =========================================================

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Contact <span>Me</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Let’s connect and build something useful'
    '</div>',
    unsafe_allow_html=True
)

contact1, contact2 = st.columns(2)

with contact1:

    st.markdown("""
    <div class="card">

        <h3>📧 Get In Touch</h3>

        <br>

        <p>
        <strong style="color:#60a5fa;">
        Email
        </strong>
        <br>
        your-email@example.com
        </p>

        <br>

        <p>
        <strong style="color:#60a5fa;">
        LinkedIn
        </strong>
        <br>
        linkedin.com/in/your-profile
        </p>

        <br>

        <p>
        <strong style="color:#60a5fa;">
        GitHub
        </strong>
        <br>
        github.com/your-username
        </p>

        <br>

        <p>
        <strong style="color:#60a5fa;">
        Location
        </strong>
        <br>
        Telangana, India
        </p>

    </div>
    """, unsafe_allow_html=True)


with contact2:

    st.markdown("""
    <div class="card">

        <h3>🤝 Let's Connect</h3>

        <p>
        I am interested in internships, engineering projects,
        CAD design opportunities and learning from industry
        professionals.
        </p>

        <br>

        <p>
        Feel free to connect with me through LinkedIn or email.
        </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("💼 Open LinkedIn", use_container_width=True):

        st.markdown(
            "[Click here to open LinkedIn](https://www.linkedin.com/)",
            unsafe_allow_html=True
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <p>
        © 2026 <span>Manohar</span>
    </p>

    <p>
        Mechanical Engineering Student | SR University
    </p>

    <p>
        Designed with Python & Streamlit ⚙️
    </p>

</div>
""", unsafe_allow_html=True)
