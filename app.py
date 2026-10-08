import streamlit as st
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Manohar | Mechanical Engineer",
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
# HELPER FUNCTIONS
# ============================================================

def image_exists(filename):
    return (IMAGE_DIR / filename).exists()


def show_image(filename, caption="", width="100%"):
    path = IMAGE_DIR / filename

    if path.exists():
        st.image(
            str(path),
            caption=caption,
            use_container_width=True
        )
    else:
        st.markdown(
            f"""
            <div class="image-placeholder">
                <div class="placeholder-icon">⚙️</div>
                <div>{caption if caption else "Project Image"}</div>
                <small>
                    Add <b>images/{filename}</b>
                </small>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PROFESSIONAL CSS
# ============================================================

st.markdown("""
<style>

/* ---------- GLOBAL ---------- */

html {
    scroll-behavior: smooth;
}

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(37,99,235,.20),
            transparent 28%
        ),
        radial-gradient(
            circle at 95% 90%,
            rgba(124,58,237,.18),
            transparent 28%
        ),
        #050816;
    color: #ffffff;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* ---------- HIDE STREAMLIT ---------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* ---------- NAVIGATION ---------- */

.navbar {
    position: sticky;
    top: 10px;
    z-index: 100;

    padding: 15px 25px;

    border: 1px solid rgba(255,255,255,.10);

    border-radius: 16px;

    background: rgba(5,8,22,.78);

    backdrop-filter: blur(18px);

    margin-bottom: 35px;

    text-align: center;
}

.navbar a {
    color: #cbd5e1;
    text-decoration: none;

    margin: 0 13px;

    font-size: 14px;

    transition: .3s;
}

.navbar a:hover {
    color: #60a5fa;
}

/* ---------- HERO ---------- */

.hero {
    min-height: 600px;

    display: flex;

    align-items: center;

    padding: 55px;

    border-radius: 30px;

    border: 1px solid rgba(96,165,250,.18);

    background:
        linear-gradient(
            135deg,
            rgba(37,99,235,.14),
            rgba(124,58,237,.08)
        );

    box-shadow:
        0 30px 80px rgba(0,0,0,.30);
}

.hero-small {
    color: #60a5fa;

    font-weight: 700;

    letter-spacing: 3px;

    text-transform: uppercase;

    font-size: 13px;
}

.hero-title {
    font-size: clamp(48px, 7vw, 82px);

    line-height: 1;

    font-weight: 800;

    margin: 15px 0;
}

.hero-title span {
    color: #60a5fa;
}

.hero-role {
    font-size: 25px;

    color: #cbd5e1;

    font-weight: 600;

    margin-bottom: 20px;
}

.hero-text {
    color: #94a3b8;

    font-size: 17px;

    line-height: 1.8;

    max-width: 700px;
}

/* ---------- PROFILE IMAGE ---------- */

.profile-container {
    text-align: center;
}

.profile-image {
    width: 300px;
    height: 300px;

    border-radius: 50%;

    object-fit: cover;

    border: 4px solid #60a5fa;

    box-shadow:
        0 0 50px rgba(37,99,235,.35);
}

.profile-placeholder {
    width: 300px;
    height: 300px;

    border-radius: 50%;

    margin: auto;

    display: flex;

    justify-content: center;

    align-items: center;

    flex-direction: column;

    background:
        linear-gradient(
            135deg,
            #172554,
            #312e81
        );

    border: 3px solid #60a5fa;

    font-size: 70px;
}

.profile-placeholder small {
    font-size: 13px;

    color: #94a3b8;

    margin-top: 10px;
}

/* ---------- SECTION ---------- */

.section {
    padding-top: 100px;
}

.section-heading {
    font-size: 42px;

    font-weight: 800;

    margin-bottom: 8px;
}

.section-heading span {
    color: #60a5fa;
}

.section-subtitle {
    color: #94a3b8;

    margin-bottom: 35px;
}

/* ---------- CARDS ---------- */

.card {
    height: 100%;

    padding: 28px;

    border-radius: 20px;

    background: rgba(255,255,255,.045);

    border: 1px solid rgba(255,255,255,.09);

    transition: .35s;
}

.card:hover {
    transform: translateY(-6px);

    border-color: rgba(96,165,250,.55);

    box-shadow:
        0 20px 50px rgba(0,0,0,.25);
}

.card h3 {
    margin-bottom: 12px;
}

.card p {
    color: #94a3b8;

    line-height: 1.75;
}

/* ---------- INFO ---------- */

.info-row {
    padding: 13px 0;

    border-bottom:
        1px solid rgba(255,255,255,.07);

    color: #cbd5e1;
}

.info-label {
    color: #60a5fa;

    font-weight: 700;
}

/* ---------- SKILLS ---------- */

.skill-title {
    display: flex;

    justify-content: space-between;

    margin-bottom: 7px;

    color: #e2e8f0;
}

.skill-percent {
    color: #60a5fa;
}

.skill-track {
    height: 9px;

    background: #1e293b;

    border-radius: 20px;

    overflow: hidden;

    margin-bottom: 22px;
}

.skill-fill {
    height: 100%;

    background:
        linear-gradient(
            90deg,
            #2563eb,
            #60a5fa
        );

    border-radius: 20px;
}

/* ---------- PROJECT ---------- */

.project-card {
    overflow: hidden;

    border-radius: 20px;

    border: 1px solid rgba(255,255,255,.09);

    background: rgba(255,255,255,.045);

    transition: .35s;

    margin-bottom: 25px;
}

.project-card:hover {
    transform: translateY(-7px);

    border-color: #60a5fa;

    box-shadow:
        0 20px 55px rgba(0,0,0,.3);
}

.project-content {
    padding: 25px;
}

.project-content p {
    color: #94a3b8;

    line-height: 1.7;
}

.project-number {
    color: #60a5fa;

    font-weight: 800;

    letter-spacing: 2px;

    font-size: 13px;
}

/* ---------- TAGS ---------- */

.tag {
    display: inline-block;

    padding: 6px 11px;

    margin: 5px 4px 0 0;

    border-radius: 30px;

    color: #93c5fd;

    background: rgba(96,165,250,.10);

    border: 1px solid rgba(96,165,250,.25);

    font-size: 12px;
}

/* ---------- IMAGE PLACEHOLDER ---------- */

.image-placeholder {
    height: 280px;

    display: flex;

    justify-content: center;

    align-items: center;

    flex-direction: column;

    background:
        linear-gradient(
            135deg,
            rgba(37,99,235,.16),
            rgba(124,58,237,.12)
        );

    color: #94a3b8;

    text-align: center;

    border-bottom:
        1px solid rgba(255,255,255,.08);
}

.placeholder-icon {
    font-size: 60px;

    margin-bottom: 10px;
}

.image-placeholder small {
    margin-top: 8px;

    color: #64748b;
}

/* ---------- GALLERY ---------- */

.gallery-title {
    font-size: 22px;

    font-weight: 700;

    margin-top: 30px;

    margin-bottom: 15px;
}

/* ---------- ACHIEVEMENT ---------- */

.achievement {
    text-align: center;

    padding: 30px;

    border-radius: 20px;

    background: rgba(255,255,255,.045);

    border: 1px solid rgba(255,255,255,.09);
}

.achievement-icon {
    font-size: 55px;

    margin-bottom: 15px;
}

/* ---------- STATS ---------- */

.stat {
    text-align: center;

    padding: 25px;

    border-radius: 16px;

    background: rgba(255,255,255,.04);

    border: 1px solid rgba(255,255,255,.08);
}

.stat-number {
    font-size: 32px;

    font-weight: 800;

    color: #60a5fa;
}

.stat-text {
    color: #94a3b8;

    font-size: 14px;
}

/* ---------- CONTACT ---------- */

.contact-box {
    padding: 35px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(37,99,235,.13),
            rgba(124,58,237,.08)
        );

    border:
        1px solid rgba(96,165,250,.18);
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;

    margin-top: 100px;

    padding: 35px 10px;

    border-top:
        1px solid rgba(255,255,255,.08);

    color: #64748b;
}

.footer span {
    color: #60a5fa;
}

/* ---------- BUTTONS ---------- */

.stButton button,
.stDownloadButton button {
    border-radius: 10px !important;

    border: 1px solid #60a5fa !important;

    background: #2563eb !important;

    color: white !important;

    font-weight: 700 !important;
}

.stButton button:hover,
.stDownloadButton button:hover {
    background: #1d4ed8 !important;
}

/* ---------- MOBILE ---------- */

@media(max-width:768px) {

    .navbar a {
        margin: 0 5px;

        font-size: 11px;
    }

    .hero {
        padding: 30px;

        text-align: center;
    }

    .hero-title {
        font-size: 48px;
    }

    .profile-image,
    .profile-placeholder {
        width: 220px;
        height: 220px;
    }

    .section-heading {
        font-size: 32px;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVBAR
# ============================================================

st.markdown("""
<div class="navbar">

<a href="#home">HOME</a>
<a href="#about">ABOUT</a>
<a href="#skills">SKILLS</a>
<a href="#projects">PROJECTS</a>
<a href="#cad">CAD GALLERY</a>
<a href="#achievements">ACHIEVEMENTS</a>
<a href="#resume">RESUME</a>
<a href="#contact">CONTACT</a>

</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown('<div id="home"></div>', unsafe_allow_html=True)

hero1, hero2 = st.columns([1.5, 1], gap="large")

with hero1:

    st.markdown("""
    <div class="hero">

        <div>

            <div class="hero-small">
                Mechanical Engineering Portfolio
            </div>

            <div class="hero-title">
                Manohar<span>.</span>
            </div>

            <div class="hero-role">
                Mechanical Engineering Student
            </div>

            <div class="hero-text">

                2nd-year Mechanical Engineering student at
                SR University with a strong interest in
                CAD design, 3D modelling, manufacturing,
                thermal engineering and innovative product development.

            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


with hero2:

    if image_exists("profile.jpg"):

        st.markdown(
            '<div class="profile-container">',
            unsafe_allow_html=True
        )

        st.image(
            str(IMAGE_DIR / "profile.jpg"),
            use_container_width=True
        )

        st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="profile-placeholder">

            👨‍🎓

            <small>
                Add images/profile.jpg
            </small>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# STATS
# ============================================================

st.write("")

c1, c2, c3, c4 = st.columns(4)

stats = [
    ("2nd", "Year"),
    ("3+", "Projects"),
    ("4+", "Technical Skills"),
    ("🏆", "Achievement")
]

for col, (number, text) in zip(
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

                <div class="stat-text">
                    {text}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# ABOUT
# ============================================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section">'
    '<div class="section-heading">'
    'About <span>Me</span>'
    '</div>'
    '<div class="section-subtitle">'
    'My background, interests and career direction'
    '</div>'
    '</div>',
    unsafe_allow_html=True
)

a1, a2 = st.columns(2, gap="large")

with a1:

    st.markdown("""
    <div class="card">

        <h3>👨‍🎓 Who I Am</h3>

        <p>
        I am a Mechanical Engineering student who enjoys
        learning through practical projects and engineering
        design.
        </p>

        <p>
        My main interests are CAD modelling, product design,
        manufacturing, thermal engineering and robotics.
        </p>

        <p>
        I am continuously developing my technical skills
        through academic projects, self-learning and
        hands-on experimentation.
        </p>

    </div>
    """, unsafe_allow_html=True)


with a2:

    st.markdown("""
    <div class="card">

        <h3>📋 Education & Profile</h3>

        <div class="info-row">
            <span class="info-label">Name:</span>
            Manohar
        </div>

        <div class="info-row">
            <span class="info-label">Branch:</span>
            Mechanical Engineering
        </div>

        <div class="info-row">
            <span class="info-label">Year:</span>
            2nd Year
        </div>

        <div class="info-row">
            <span class="info-label">University:</span>
            SR University
        </div>

        <div class="info-row">
            <span class="info-label">Interests:</span>
            CAD • Design • Manufacturing
        </div>

        <div class="info-row">
            <span class="info-label">Career Goal:</span>
            Engineering & Space Technology
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# SKILLS
# ============================================================

st.markdown('<div id="skills"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-heading">
        Technical <span>Skills</span>
    </div>

    <div class="section-subtitle">
        Tools and engineering skills I am developing
    </div>

</div>
""", unsafe_allow_html=True)

skill_col1, skill_col2 = st.columns(2)

with skill_col1:

    skills = [
        ("Fusion 360", 75),
        ("Engineering Drawing", 80),
        ("AutoCAD", 65),
        ("Python", 60),
        ("Manufacturing", 70)
    ]

    for name, percentage in skills:

        st.markdown(
            f"""
            <div class="skill-title">

                <span>{name}</span>

                <span class="skill-percent">
                    {percentage}%
                </span>

            </div>

            <div class="skill-track">

                <div class="skill-fill"
                     style="width:{percentage}%">
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


with skill_col2:

    skill_cards = [
        ("⚙️", "CAD Design",
         "2D and 3D mechanical modelling"),

        ("🔧", "Manufacturing",
         "Manufacturing processes and product development"),

        ("📐", "Engineering Drawing",
         "Technical drawings and dimensions"),

        ("💻", "Programming",
         "Python and engineering applications"),

        ("🤖", "Robotics",
         "Basic electronics and robotic systems")
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


# ============================================================
# PROJECTS
# ============================================================

st.markdown('<div id="projects"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-heading">
        Featured <span>Projects</span>
    </div>

    <div class="section-subtitle">
        Selected engineering projects and product concepts
    </div>

</div>
""", unsafe_allow_html=True)


# ---------------- PROJECT 01 ----------------

st.markdown("""
<div class="project-card">
""", unsafe_allow_html=True)

show_image(
    "cooling.jpg",
    "Passive Cooling Enclosure"
)

st.markdown("""
<div class="project-content">

<div class="project-number">
PROJECT 01
</div>

<h2>
Passive Cooling Enclosure
</h2>

<p>
A compact passive cooling enclosure developed as a
Materials Science & Engineering project. The design
focuses on thermal management using aluminium
components without depending on active cooling.
</p>

<p>
<strong>Design focus:</strong>
thermal management, compact enclosure design,
aluminium construction and testing space.
</p>

<span class="tag">Mechanical Design</span>
<span class="tag">Thermal Engineering</span>
<span class="tag">Fusion 360</span>
<span class="tag">Aluminium</span>

</div>
</div>
""", unsafe_allow_html=True)


# ---------------- PROJECT 02 ----------------

st.markdown("""
<div class="project-card">
""", unsafe_allow_html=True)

show_image(
    "cloth_dryer.jpg",
    "Portable Cloth Dryer"
)

st.markdown("""
<div class="project-content">

<div class="project-number">
PROJECT 02
</div>

<h2>
Portable Cloth Dryer
</h2>

<p>
A foldable and portable cloth drying mechanism designed
for efficient use of space. The mechanism is designed
for wall or ceiling mounting and convenient folding.
</p>

<p>
<strong>Design focus:</strong>
folding mechanism, hinges, frame design and
space-efficient product development.
</p>

<span class="tag">Product Design</span>
<span class="tag">Mechanism</span>
<span class="tag">Manufacturing</span>
<span class="tag">CAD</span>

</div>
</div>
""", unsafe_allow_html=True)


# ---------------- PROJECT 03 ----------------

st.markdown("""
<div class="project-card">
""", unsafe_allow_html=True)

show_image(
    "ai_car.jpg",
    "AI Voice Car"
)

st.markdown("""
<div class="project-content">

<div class="project-number">
PROJECT 03
</div>

<h2>
AI Voice Car
</h2>

<p>
A physical AI voice robot concept designed in a small
car-like form. The system combines a Raspberry Pi,
ESP32, motors, speaker and display.
</p>

<p>
<strong>Design focus:</strong>
voice interaction, autonomous movement,
embedded systems and robotics.
</p>

<span class="tag">Raspberry Pi</span>
<span class="tag">ESP32</span>
<span class="tag">Robotics</span>
<span class="tag">AI</span>

</div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# CAD GALLERY
# ============================================================

st.markdown('<div id="cad"></div>', unsafe_allow_html=True)

st.markdown("""
<div class="section">

    <div class="section-heading">
        CAD & <span>Design Gallery</span>
    </div>

    <div class="section-subtitle">
        Engineering models, drawings and design development
    </div>

</div>
""", unsafe_allow_html=True)


g1, g2 = st.columns(2)

with g1:

    st.markdown(
        '<div class="gallery-title">'
        'Passive Cooling CAD'
        '</div>',
        unsafe_allow_html=True
    )

    show_image(
        "cooling_cad.jpg",
        "Fusion 360 / CAD Design"
    )


with g2:

    st.markdown(
        '<div class="gallery-title">'
        'Portable Dryer CAD'
        '</div>',
        unsafe_allow_html=True
    )

    show_image()
