import streamlit as st
from pathlib import Path

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Manohar Paka | Mechanical Engineering Portfolio",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"
RESUME_FILE = BASE_DIR / "resume.pdf"

# ============================================================
# ONLINE ENGINEERING IMAGES
# ============================================================

IMAGES = {
    "hero":
        "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=1200&q=85",

    "mechanical":
        "https://images.unsplash.com/photo-1581092160607-ee22621dd758?auto=format&fit=crop&w=1200&q=85",

    "cad":
        "https://images.unsplash.com/photo-1535378917042-10a22c95931a?auto=format&fit=crop&w=1200&q=85",

    "manufacturing":
        "https://images.unsplash.com/photo-1565610222536-ef125c59da2e?auto=format&fit=crop&w=1200&q=85",

    "robot":
        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=1200&q=85",

    "technology":
        "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1200&q=85",

    "engineering2":
        "https://images.unsplash.com/photo-1537462715879-360eeb61a0ad?auto=format&fit=crop&w=1200&q=85"
}

# ============================================================
# LOCAL IMAGE HELPER
# ============================================================

def local_image(name):
    path = IMAGE_DIR / name
    return str(path) if path.exists() else None


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

html {
    scroll-behavior: smooth;
}

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(37,99,235,0.20),
            transparent 25%
        ),

        radial-gradient(
            circle at 90% 80%,
            rgba(124,58,237,0.16),
            transparent 25%
        ),

        #050816;

    color: white;
}

.block-container {

    max-width: 1250px;

    padding-top: 20px;
    padding-bottom: 60px;
}

/* Hide Streamlit */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ========================================================
NAVBAR
======================================================== */

.navbar {

    position: sticky;
    top: 12px;

    z-index: 999;

    display: flex;
    justify-content: center;
    flex-wrap: wrap;

    gap: 10px;

    padding: 15px 20px;

    margin-bottom: 35px;

    border-radius: 18px;

    background: rgba(5,8,22,0.82);

    border: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(20px);
}

.navbar a {

    color: #cbd5e1;

    text-decoration: none;

    padding: 8px 13px;

    border-radius: 8px;

    font-size: 13px;

    font-weight: 600;

    transition: 0.3s;
}

.navbar a:hover {

    background: rgba(96,165,250,0.12);

    color: #60a5fa;
}

/* ========================================================
HERO
======================================================== */

.hero {

    min-height: 560px;

    padding: 55px;

    border-radius: 30px;

    border: 1px solid rgba(96,165,250,0.18);

    background:
        linear-gradient(
            135deg,
            rgba(37,99,235,0.15),
            rgba(124,58,237,0.08)
        );

    box-shadow:
        0 30px 80px rgba(0,0,0,0.30);
}

.hero-small {

    color: #60a5fa;

    letter-spacing: 3px;

    font-size: 13px;

    font-weight: 800;

    text-transform: uppercase;
}

.hero-title {

    font-size: clamp(50px, 7vw, 85px);

    line-height: 1;

    font-weight: 800;

    margin-top: 15px;
}

.hero-title span {
    color: #60a5fa;
}

.hero-role {

    font-size: 25px;

    color: #e2e8f0;

    font-weight: 600;

    margin-top: 20px;
}

.hero-description {

    color: #94a3b8;

    font-size: 17px;

    line-height: 1.8;

    max-width: 700px;

    margin-top: 20px;
}

/* ========================================================
PROFILE
======================================================== */

.profile-box {

    text-align: center;

    padding: 20px;
}

.profile-box img {

    width: 300px;

    height: 300px;

    object-fit: cover;

    border-radius: 50%;

    border: 4px solid #60a5fa;

    box-shadow:
        0 0 50px rgba(37,99,235,0.35);
}

/* ========================================================
SECTION
======================================================== */

.section {

    padding-top: 100px;

    margin-bottom: 35px;
}

.section-title {

    font-size: 42px;

    font-weight: 800;
}

.section-title span {
    color: #60a5fa;
}

.section-subtitle {

    color: #94a3b8;

    margin-top: 8px;

    font-size: 15px;
}

/* ========================================================
CARDS
======================================================== */

.card {

    padding: 28px;

    height: 100%;

    border-radius: 20px;

    background: rgba(255,255,255,0.045);

    border: 1px solid rgba(255,255,255,0.09);

    transition: 0.3s;
}

.card:hover {

    transform: translateY(-6px);

    border-color: rgba(96,165,250,0.55);

    box-shadow:
        0 20px 50px rgba(0,0,0,0.25);
}

.card p {

    color: #94a3b8;

    line-height: 1.75;
}

/* ========================================================
PROJECT CARD
======================================================== */

.project-card {

    background: rgba(255,255,255,0.045);

    border: 1px solid rgba(255,255,255,0.09);

    border-radius: 22px;

    overflow: hidden;

    margin-bottom: 30px;

    transition: 0.35s;
}

.project-card:hover {

    transform: translateY(-7px);

    border-color: #60a5fa;

    box-shadow:
        0 25px 60px rgba(0,0,0,0.3);
}

.project-image {

    width: 100%;

    height: 260px;

    object-fit: cover;
}

.project-content {

    padding: 28px;
}

.project-number {

    color: #60a5fa;

    font-size: 12px;

    font-weight: 800;

    letter-spacing: 2px;
}

.project-content h2 {

    margin-top: 10px;
}

.project-content p {

    color: #94a3b8;

    line-height: 1.75;
}

/* ========================================================
TAGS
======================================================== */

.tag {

    display: inline-block;

    padding: 6px 12px;

    margin: 5px 5px 0 0;

    border-radius: 30px;

    color: #93c5fd;

    background: rgba(96,165,250,0.10);

    border: 1px solid rgba(96,165,250,0.25);

    font-size: 12px;
}

/* ========================================================
SKILLS
======================================================== */

.skill-row {

    margin-bottom: 22px;
}

.skill-header {

    display: flex;

    justify-content: space-between;

    margin-bottom: 7px;

    color: #e2e8f0;
}

.skill-percent {

    color: #60a5fa;
}

.skill-bar {

    height: 8px;

    border-radius: 20px;

    background: #1e293b;

    overflow: hidden;
}

.skill-fill {

    height: 100%;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #60a5fa
        );
}

/* ========================================================
TIMELINE
======================================================== */

.timeline {

    border-left: 2px solid #2563eb;

    padding-left: 25px;

    margin-left: 10px;
}

.timeline-item {

    margin-bottom: 35px;

    position: relative;
}

.timeline-item:before {

    content: "";

    width: 12px;

    height: 12px;

    border-radius: 50%;

    background: #60a5fa;

    position: absolute;

    left: -32px;

    top: 5px;

    box-shadow:
        0 0 15px rgba(96,165,250,0.8);
}

.timeline-year {

    color: #60a5fa;

    font-weight: 800;

    font-size: 13px;
}

/* ========================================================
STATS
======================================================== */

.stat {

    text-align: center;

    padding: 25px;

    border-radius: 18px;

    background: rgba(255,255,255,0.04);

    border: 1px solid rgba(255,255,255,0.08);
}

.stat-number {

    font-size: 32px;

    font-weight: 800;

    color: #60a5fa;
}

.stat-label {

    color: #94a3b8;

    font-size: 13px;
}

/* ========================================================
CONTACT
======================================================== */

.contact {

    padding: 40px;

    border-radius: 25px;

    background:
        linear-gradient(
            135deg,
            rgba(37,99,235,0.14),
            rgba(124,58,237,0.08)
        );

    border: 1px solid rgba(96,165,250,0.18);
}

/* ========================================================
FOOTER
======================================================== */

.footer {

    text-align: center;

    margin-top: 100px;

    padding: 35px;

    color: #64748b;

    border-top:
        1px solid rgba(255,255,255,0.08);
}

.footer span {
    color: #60a5fa;
}

/* ========================================================
MOBILE
======================================================== */

@media(max-width:768px) {

    .hero {

        padding: 30px;

        text-align: center;
    }

    .hero-title {

        font-size: 50px;
    }

    .hero-role {

        font-size: 20px;
    }

    .section-title {

        font-size: 32px;
    }

    .profile-box img {

        width: 220px;
        height: 220px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown("""
<div class="navbar">

<a href="#home">HOME</a>

<a href="#about">ABOUT</a>

<a href="#skills">SKILLS</a>

<a href="#projects">PROJECTS</a>

<a href="#education">EDUCATION</a>

<a href="#achievements">ACHIEVEMENTS</a>

<a href="#resume">RESUME</a>

<a href="#contact">CONTACT</a>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

hero_left, hero_right = st.columns(
    [1.5, 1],
    gap="large"
)

with hero_left:

    st.markdown("""
    <div class="hero">

        <div class="hero-small">
            Mechanical Engineering Portfolio
        </div>

        <div class="hero-title">
            Manohar<span>.</span>
        </div>

        <div class="hero-role">
            Mechanical Engineering Student
        </div>

        <div class="hero-description">

            2nd-year B.Tech Mechanical Engineering student
            at SR University, passionate about mechanical
            design, CAD modelling, manufacturing,
            thermal engineering and innovative product development.

            <br><br>

            <strong style="color:#e2e8f0;">
            Design • Build • Learn • Innovate
            </strong>

        </div>

    </div>
    """, unsafe_allow_html=True)


with hero_right:

    profile = local_image("profile.jpg")

    if profile:

        st.markdown(
            '<div class="profile-box">',
            unsafe_allow_html=True
        )

        st.image(
            profile,
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.markdown(
            f"""
            <div class="profile-box">

                <img src="{IMAGES['hero']}">

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# STATS
# ============================================================

st.write("")

c1, c2, c3, c4 = st.columns(4)

stats = [
    ("2nd", "Year"),
    ("3+", "Engineering Projects"),
    ("5+", "Technical Areas"),
    ("🏆", "Semester Topper")
]

for col, (number, label) in zip(
    [c1, c2, c3, c4],
    stats
):

    with col:

        st.markdown(
            f"""
            <div class="stat">

                <div class="stat-number">
                    {number}
                </div>

                <div class="stat-label">
                    {label}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ABOUT
# ============================================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        About <span>Me</span>
    </div>

    <div class="section-subtitle">
        A little about my engineering journey
    </div>

</div>
""", unsafe_allow_html=True)


about1, about2 = st.columns(
    2,
    gap="large"
)

with about1:

    st.markdown("""
    <div class="card">

        <h2>👨‍🎓 Who I Am</h2>

        <p>
        I am a Mechanical Engineering student who enjoys
        converting engineering ideas into practical designs.
        </p>

        <p>
        I am especially interested in CAD modelling,
        product development, manufacturing processes,
        thermal systems and robotics.
        </p>

        <p>
        My goal is to continuously improve my technical
        knowledge through projects, internships and
        hands-on engineering experience.
        </p>

    </div>
    """, unsafe_allow_html=True)


with about2:

    st.markdown("""
    <div class="card">

        <h2>⚙️ What I Like</h2>

        <p>
        • Mechanical Design
        </p>

        <p>
        • Fusion 360 & 3D Modelling
        </p>

        <p>
        • Engineering Drawing
        </p>

        <p>
        • Manufacturing Technology
        </p>

        <p>
        • Product Development
        </p>

        <p>
        • Robotics & Embedded Systems
        </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SKILLS
# ============================================================

st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        Technical <span>Skills</span>
    </div>

    <div class="section-subtitle">
        Engineering tools and capabilities
    </div>

</div>
""", unsafe_allow_html=True)


skill_left, skill_right = st.columns(2)

skills = [
    ("Fusion 360", 78),
    ("Engineering Drawing", 82),
    ("AutoCAD", 68),
    ("Python", 62),
    ("Manufacturing", 72),
    ("Product Design", 75)
]

with skill_left:

    for name, percent in skills[:3]:

        st.markdown(
            f"""
            <div class="skill-row">

                <div class="skill-header">

                    <span>{name}</span>

                    <span class="skill-percent">
                        {percent}%
                    </span>

                </div>

                <div class="skill-bar">

                    <div class="skill-fill"
                         style="width:{percent}%">
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


with skill_right:

    for name, percent in skills[3:]:

        st.markdown(
            f"""
            <div class="skill-row">

                <div class="skill-header">

                    <span>{name}</span>

                    <span class="skill-percent">
                        {percent}%
                    </span>

                </div>

                <div class="skill-bar">

                    <div class="skill-fill"
                         style="width:{percent}%">
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PROJECTS
# ============================================================

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        Featured <span>Projects</span>
    </div>

    <div class="section-subtitle">
        Mechanical design and technology projects
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT 1 - PASSIVE COOLING
# ============================================================

cooling_local = local_image("passive_cooling.jpg")

if cooling_local:

    st.image(
        cooling_local,
        use_container_width=True
    )

else:

    st.image(
        IMAGES["engineering2"],
        use_container_width=True
    )

st.markdown("""
<div class="project-card">

    <div class="project-content">

        <div class="project-number">
            PROJECT 01
        </div>

        <h2>
            Passive Cooling Enclosure
        </h2>

        <p>
        A compact passive cooling enclosure developed
        as a Materials Science & Engineering project.
        The design focuses on thermal management,
        aluminium construction, airflow and heat dissipation.
        </p>

        <p>
        Current concept dimensions are approximately
        <strong style="color:white;">
        20 × 15 × 9 cm
        </strong>.
        </p>

        <span class="tag">Fusion 360</span>
        <span class="tag">Thermal Design</span>
        <span class="tag">Aluminium</span>
        <span class="tag">CAD</span>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT 2 - CLOTH DRYER
# ============================================================

dryer_local = local_image("cloth_dryer.jpg")

if dryer_local:

    st.image(
        dryer_local,
        use_container_width=True
    )

else:

    st.image(
        IMAGES["manufacturing"],
        use_container_width=True
    )

st.markdown("""
<div class="project-card">

    <div class="project-content">

        <div class="project-number">
            PROJECT 02
        </div>

        <h2>
            Foldable Wall & Ceiling Mounted Dryer
        </h2>

        <p>
        A space-saving cloth dryer concept designed with
        two folding frames and a hinge mechanism.
        </p>

        <p>
        The design allows the dryer to remain horizontal
        during use and fold toward the wall when not required.
        </p>

        <span class="tag">Product Design</span>
        <span class="tag">Mechanism</span>
        <span class="tag">Manufacturing</span>
        <span class="tag">CAD</span>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT 3 - AI VOICE CAR
# ============================================================

st.image(
    IMAGES["robot"],
    use_container_width=True
)

st.markdown("""
<div class="project-card">

    <div class="project-content">

        <div class="project-number">
            PROJECT 03
        </div>

        <h2>
            AI Voice Car
        </h2>

        <p>
        A small physical AI robot concept designed in a
        car-like form. The system is planned around
        Raspberry Pi and ESP32 control.
        </p>

        <p>
        The concept includes voice interaction, motor
        movement, speaker output, earphone support and
        a small display.
        </p>

        <span class="tag">Raspberry Pi</span>
        <span class="tag">ESP32</span>
        <span class="tag">Robotics</span>
        <span class="tag">AI</span>
        <span class="tag">Embedded Systems</span>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# EDUCATION
# ============================================================

st.markdown('<div id="education"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        <span>Education</span>
    </div>

    <div class="section-subtitle">
        My academic journey
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="timeline">

    <div class="timeline-item">

        <div class="timeline-year">
            2025 – 2029
        </div>

        <h2>
            B.Tech – Mechanical Engineering
        </h2>

        <p style="color:#94a3b8;">
            SR University, Telangana
        </p>

        <p style="color:#94a3b8;">
            Currently pursuing 2nd year of B.Tech Mechanical
            Engineering with interest in CAD, manufacturing,
            thermal engineering and product development.
        </p>

    </div>


    <div class="timeline-item">

        <div class="timeline-year">
            2023 – 2025
        </div>

        <h2>
            Intermediate
        </h2>

        <p style="color:#94a3b8;">
            Alphores Junior College
        </p>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# ACHIEVEMENTS
# ============================================================

st.markdown('<div id="achievements"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        <span>Achievements</span>
    </div>

    <div class="section-subtitle">
        Academic and technical achievements
    </div>

</div>
""", unsafe_allow_html=True)

achievement1, achievement2 = st.columns(2, gap="large")

with achievement1:

    st.markdown("""
    <div class="card">

        <h2>🏆 Semester Topper</h2>

        <p>
        Received a Semester Topper Certificate from the
        Dean and Head of the Department for academic
        performance.
        </p>

    </div>
    """, unsafe_allow_html=True)


with achievement2:

    st.markdown("""
    <div class="card">

        <h2>⚙️ Engineering Projects</h2>

        <p>
        Working on practical engineering projects involving
        mechanical design, CAD modelling, thermal management,
        manufacturing and robotics.
        </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# RESUME
# ============================================================

st.markdown('<div id="resume"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        My <span>Resume</span>
    </div>

    <div class="section-subtitle">
        Download my professional resume
    </div>

</div>
""", unsafe_allow_html=True)

resume_col1, resume_col2 = st.columns([2, 1], gap="large")

with resume_col1:

    st.markdown("""
    <div class="card">

        <h2>📄 Professional Resume</h2>

        <p>
        My resume contains my education, technical skills,
        engineering projects, achievements and career interests.
        </p>

    </div>
    """, unsafe_allow_html=True)


with resume_col2:

    if RESUME_FILE.exists():

        with open(RESUME_FILE, "rb") as file:

            st.download_button(
                label="⬇️ Download Resume",
                data=file,
                file_name="Manohar_Paka_Resume.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    else:

        st.warning(
            "resume.pdf not found. Add your resume.pdf "
            "to the project folder."
        )


# ============================================================
# PROFESSIONAL PROFILE
# ============================================================

st.markdown("""
<div class="section">

    <div class="section-title">
        Professional <span>Profile</span>
    </div>

    <div class="section-subtitle">
        Connect with me online
    </div>

</div>
""", unsafe_allow_html=True)

linkedin_url = (
    "https://www.linkedin.com/in/"
    "manohar-paka-3537b5399"
    "?utm_source=share_via"
    "&utm_content=profile"
    "&utm_medium=member_android"
)

profile1, profile2 = st.columns(2, gap="large")

with profile1:

    st.markdown("""
    <div class="card">

        <h2>💼 LinkedIn</h2>

        <p>
        View my professional profile, engineering interests,
        projects and academic activities.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🔗 Open LinkedIn Profile",
        linkedin_url,
        use_container_width=True
    )


with profile2:

    st.markdown("""
    <div class="card">

        <h2>🚀 Career Interests</h2>

        <p>
        Mechanical Design • CAD • Manufacturing • Robotics
        • Thermal Engineering • Product Development
        </p>

        <p>
        I am interested in internships and opportunities
        where I can gain practical engineering experience.
        </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CONTACT
# ============================================================

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-title">
        <span>Contact</span>
    </div>

    <div class="section-subtitle">
        Let's connect
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="contact">

    <h2>
        📩 Interested in connecting?
    </h2>

    <p style="color:#94a3b8; font-size:16px; line-height:1.8;">
        I am open to learning opportunities, internships,
        engineering projects and professional connections.
    </p>

    <p style="font-size:18px;">
        📧
        <a href="mailto:manoharpaka472@gmail.com"
           style="color:#60a5fa; text-decoration:none;">
            manoharpaka472@gmail.com
        </a>
    </p>

    <p style="font-size:18px;">
        📍 Telangana, India
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <p>
        Designed & Built by
        <span>Manohar Paka</span>
    </p>

    <p>
        Mechanical Engineering Student • SR University
    </p>

    <p>
        © 2026 Manohar Paka. All rights reserved.
    </p>

</div>
""", unsafe_allow_html=True)
