import streamlit as st
import sqlite3
import hashlib
import os
from datetime import date, datetime
import pandas as pd

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart Hostel Management",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# DATABASE
# ============================================================

DB_FILE = "hostel.db"


def get_connection():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


conn = get_connection()


def init_database():

    cursor = conn.cursor()

    # Users
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            active INTEGER DEFAULT 1
        )
    """)

    # Students
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            student_id TEXT UNIQUE,
            name TEXT,
            phone TEXT,
            email TEXT,
            course TEXT,
            branch TEXT,
            year TEXT,
            college TEXT,
            guardian_name TEXT,
            guardian_phone TEXT,
            address TEXT,
            hostel TEXT,
            block TEXT,
            room TEXT,
            bed TEXT,
            joining_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    # Rooms
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostel TEXT,
            block TEXT,
            floor TEXT,
            room_no TEXT UNIQUE,
            room_type TEXT,
            total_beds INTEGER,
            occupied_beds INTEGER DEFAULT 0,
            status TEXT DEFAULT 'Available'
        )
    """)

    # Fees
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            academic_year TEXT,
            total_fee REAL,
            paid REAL DEFAULT 0,
            due_date TEXT,
            status TEXT
        )
    """)

    # Meals
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meal_date TEXT,
            meal_type TEXT,
            menu TEXT
        )
    """)

    # Complaints
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            category TEXT,
            subject TEXT,
            description TEXT,
            priority TEXT,
            status TEXT DEFAULT 'Submitted',
            admin_reply TEXT,
            created_at TEXT
        )
    """)

    # Leave
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leave_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT,
            start_date TEXT,
            end_date TEXT,
            reason TEXT,
            destination TEXT,
            status TEXT DEFAULT 'Pending',
            admin_reply TEXT,
            created_at TEXT
        )
    """)

    # Announcements
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS announcements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            message TEXT,
            category TEXT,
            priority TEXT,
            created_at TEXT
        )
    """)

    conn.commit()


# ============================================================
# PASSWORD
# ============================================================

def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def check_password(password, hashed):
    return hash_password(password) == hashed


# ============================================================
# SEED DATA
# ============================================================

def seed_database():

    cursor = conn.cursor()

    # ---------------- ADMIN ----------------

    admin_exists = cursor.execute(
        "SELECT id FROM users WHERE username=?",
        ("admin",)
    ).fetchone()

    if not admin_exists:

        cursor.execute("""
            INSERT INTO users
            (username, password, role, name, email)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "admin",
            hash_password("admin123"),
            "admin",
            "Hostel Administrator",
            "admin@college.edu"
        ))

    # ---------------- STUDENT ----------------

    student_exists = cursor.execute(
        "SELECT id FROM users WHERE username=?",
        ("student",)
    ).fetchone()

    if not student_exists:

        cursor.execute("""
            INSERT INTO users
            (username, password, role, name, email)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "student",
            hash_password("student123"),
            "student",
            "Rahul Kumar",
            "rahul@college.edu"
        ))

        user_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO students
            (
                user_id,
                student_id,
                name,
                phone,
                email,
                course,
                branch,
                year,
                college,
                guardian_name,
                guardian_phone,
                address,
                hostel,
                block,
                room,
                bed,
                joining_date
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id,
            "STU001",
            "Rahul Kumar",
            "9876543210",
            "rahul@college.edu",
            "B.Tech",
            "Mechanical Engineering",
            "2nd Year",
            "ABC Engineering College",
            "Ramesh Kumar",
            "9876500000",
            "Hyderabad, Telangana",
            "ABC College Boys Hostel",
            "Block A",
            "A101",
            "Bed 1",
            "2026-07-01"
        ))

    # ---------------- ROOMS ----------------

    rooms = [
        ("ABC College Boys Hostel", "Block A", "1", "A101",
         "Double", 2, 1, "Available"),

        ("ABC College Boys Hostel", "Block A", "1", "A102",
         "Double", 2, 0, "Available"),

        ("ABC College Boys Hostel", "Block A", "1", "A103",
         "Triple", 3, 0, "Available"),

        ("ABC College Boys Hostel", "Block B", "2", "B201",
         "Four Sharing", 4, 0, "Available"),

        ("ABC College Boys Hostel", "Block B", "2", "B202",
         "Four Sharing", 4, 0, "Available")
    ]

    for room in rooms:

        exists = cursor.execute(
            "SELECT id FROM rooms WHERE room_no=?",
            (room[3],)
        ).fetchone()

        if not exists:

            cursor.execute("""
                INSERT INTO rooms
                (
                    hostel,
                    block,
                    floor,
                    room_no,
                    room_type,
                    total_beds,
                    occupied_beds,
                    status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, room)

    # ---------------- FEES ----------------

    fee_exists = cursor.execute(
        "SELECT id FROM fees WHERE student_id=?",
        ("STU001",)
    ).fetchone()

    if not fee_exists:

        cursor.execute("""
            INSERT INTO fees
            (
                student_id,
                academic_year,
                total_fee,
                paid,
                due_date,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            "STU001",
            "2026-27",
            80000,
            50000,
            "2026-12-15",
            "Partially Paid"
        ))

    # ---------------- MEALS ----------------

    today = str(date.today())

    meals = [
        ("Breakfast", "Idli, Sambar, Chutney"),
        ("Lunch", "Rice, Dal, Vegetable Curry, Curd"),
        ("Snacks", "Tea and Biscuits"),
        ("Dinner", "Chapati, Paneer Curry, Rice")
    ]

    for meal_type, menu in meals:

        exists = cursor.execute("""
            SELECT id
            FROM meals
            WHERE meal_date=? AND meal_type=?
        """, (today, meal_type)).fetchone()

        if not exists:

            cursor.execute("""
                INSERT INTO meals
                (meal_date, meal_type, menu)
                VALUES (?, ?, ?)
            """, (
                today,
                meal_type,
                menu
            ))

    # ---------------- ANNOUNCEMENT ----------------

    announcement_exists = cursor.execute(
        "SELECT id FROM announcements LIMIT 1"
    ).fetchone()

    if not announcement_exists:

        cursor.execute("""
            INSERT INTO announcements
            (title, message, category, priority, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "Welcome to New Academic Year",
            "Hostel registration and room allocation are now open.",
            "General",
            "Normal",
            datetime.now().strftime("%Y-%m-%d %H:%M")
        ))

    conn.commit()


init_database()
seed_database()


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

/* Main background */

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(0, 140, 255, 0.22),
            transparent 28%
        ),

        radial-gradient(
            circle at 90% 10%,
            rgba(150, 60, 255, 0.22),
            transparent 30%
        ),

        linear-gradient(
            135deg,
            #050b16 0%,
            #0a1530 45%,
            #0b1025 100%
        );

    color: white;
}


/* Grid */

.stApp::before {

    content: "";

    position: fixed;

    left: 0;
    right: 0;
    top: 0;
    bottom: 0;

    background-image:

        linear-gradient(
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),

        linear-gradient(
            90deg,
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        );

    background-size: 45px 45px;

    pointer-events: none;

}


/* Main */

.block-container {

    max-width: 1400px;

    padding-top: 2rem;

    padding-bottom: 3rem;

}


/* Sidebar */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #071226,
            #050b17
        );

    border-right:
        1px solid
        rgba(255,255,255,0.10);

}


/* Text */

h1, h2, h3, h4, p, label {

    color: white !important;

}


/* Cards */

div[data-testid="stMetric"] {

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.11),
            rgba(255,255,255,0.035)
        );

    border:
        1px solid
        rgba(255,255,255,0.12);

    border-radius: 20px;

    padding: 20px;

    box-shadow:
        0 15px 40px
        rgba(0,0,0,0.30);

    transition: 0.25s;

}


div[data-testid="stMetric"]:hover {

    transform:
        translateY(-5px);

    box-shadow:
        0 25px 60px
        rgba(0,0,0,0.40);

}


/* Metric values */

div[data-testid="stMetricValue"] {

    color: white !important;

}


/* Buttons */

.stButton > button {

    border-radius: 12px;

    min-height: 45px;

    background:
        linear-gradient(
            135deg,
            #237cff,
            #7045e8
        );

    color: white;

    border:
        1px solid
        rgba(255,255,255,0.15);

    font-weight: 700;

}


.stButton > button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 10px 30px
        rgba(60,100,255,0.35);

}


/* Inputs */

input, textarea {

    color: white !important;

}


/* Dataframe */

[data-testid="stDataFrame"] {

    border-radius: 15px;

}


/* Hero */

.hero-box {

    background:
        linear-gradient(
            135deg,
            rgba(20,60,120,0.90),
            rgba(50,20,100,0.90)
        );

    border:
        1px solid
        rgba(255,255,255,0.12);

    border-radius: 28px;

    padding: 40px;

    margin-bottom: 30px;

    box-shadow:
        0 30px 70px
        rgba(0,0,0,0.40);

}


/* Mobile */

@media(max-width: 768px) {

    .block-container {

        padding:
            1rem 0.8rem;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION
# ============================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "role" not in st.session_state:
    st.session_state.role = None

if "username" not in st.session_state:
    st.session_state.username = None


# ============================================================
# LOGIN
# ============================================================

def login_page():

    st.markdown(
        """
        # 🏢 Smart Hostel Management System

        ### Secure Hostel Management Platform
        """,
    )

    st.info(
        "Login as Student or Administrator"
    )

    tab1, tab2 = st.tabs(
        ["🎓 Student Login", "👨‍💼 Admin Login"]
    )

    # --------------------------------------------------------
    # STUDENT LOGIN
    # --------------------------------------------------------

    with tab1:

        with st.form("student_login"):

            username = st.text_input(
                "Student Username"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "🔐 Student Login",
                use_container_width=True
            )

            if submitted:

                user = conn.execute("""
                    SELECT *
                    FROM users
                    WHERE username=? AND role='student'
                """, (username,)).fetchone()

                if user and check_password(
                    password,
                    user["password"]
                ):

                    if user["active"] != 1:

                        st.error(
                            "Your account is not active."
                        )

                    else:

                        st.session_state.logged_in = True
                        st.session_state.user_id = user["id"]
                        st.session_state.role = "student"
                        st.session_state.username = username

                        st.rerun()

                else:

                    st.error(
                        "Invalid student username or password."
                    )

    # --------------------------------------------------------
    # ADMIN LOGIN
    # --------------------------------------------------------

    with tab2:

        with st.form("admin_login"):

            username = st.text_input(
                "Admin Username"
            )

            password = st.text_input(
                "Admin Password",
                type="password"
            )

            submitted = st.form_submit_button(
                "🔐 Admin Login",
                use_container_width=True
            )

            if submitted:

                user = conn.execute("""
                    SELECT *
                    FROM users
                    WHERE username=? AND role='admin'
                """, (username,)).fetchone()

                if user and check_password(
                    password,
                    user["password"]
                ):

                    st.session_state.logged_in = True
                    st.session_state.user_id = user["id"]
                    st.session_state.role = "admin"
                    st.session_state.username = username

                    st.rerun()

                else:

                    st.error(
                        "Invalid admin username or password."
                    )

    st.divider()

    st.warning(
        "Demo Admin Login: admin / admin123"
    )

    st.info(
        "Demo Student Login: student / student123"
    )


# ============================================================
# LOGOUT
# ============================================================

def logout():

    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.role = None
    st.session_state.username = None

    st.rerun()


# ============================================================
# STUDENT DASHBOARD
# ============================================================

def student_dashboard():

    student = conn.execute("""
        SELECT *
        FROM students
        WHERE user_id=?
    """, (
        st.session_state.user_id,
    )).fetchone()

    if not student:

        st.error(
            "Student profile not found."
        )

        return

    st.title(
        f"Welcome, {student['name']} 👋"
    )

    st.caption(
        f"Student ID: {student['student_id']}"
    )

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    fee = conn.execute("""
        SELECT *
        FROM fees
        WHERE student_id=?
    """, (
        student["student_id"],
    )).fetchone()

    if fee:

        pending = fee["total_fee"] - fee["paid"]

    else:

        pending = 0

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏠 Room",
            student["room"]
        )

    with col2:

        st.metric(
            "🛏️ Bed",
            student["bed"]
        )

    with col3:

        st.metric(
            "💰 Fee Paid",
            f"₹{fee['paid']:,.0f}" if fee else "₹0"
        )

    with col4:

        st.metric(
            "⏳ Pending",
            f"₹{pending:,.0f}"
        )

    st.divider()

    # --------------------------------------------------------
    # TABS
    # --------------------------------------------------------

    tabs = st.tabs([
        "📊 Dashboard",
        "👤 Profile",
        "🏠 Room",
        "💰 Hostel Fee",
        "🍽️ Meals",
        "📝 Leave",
        "📢 Complaints",
        "📣 Announcements"
    ])

    # ========================================================
    # DASHBOARD
    # ========================================================

    with tabs[0]:

        st.subheader(
            "Quick Actions"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.success(
                "🏠 Room allocated"
            )

        with col2:

            st.info(
                "🍽️ Meal charges included"
            )

        with col3:

            st.warning(
                "🔔 Check announcements"
            )

        st.subheader(
            "Hostel Information"
        )

        st.write(
            f"**Hostel:** {student['hostel']}"
        )

        st.write(
            f"**Block:** {student['block']}"
        )

        st.write(
            f"**Room:** {student['room']}"
        )

        st.write(
            f"**Course:** {student['course']}"
        )

        st.write(
            f"**Branch:** {student['branch']}"
        )

    # ========================================================
    # PROFILE
