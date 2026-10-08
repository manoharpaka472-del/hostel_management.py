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

    font-size:
