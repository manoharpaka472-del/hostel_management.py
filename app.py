import streamlit as st
import sqlite3
from datetime import date, datetime
import hashlib
import uuid
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Smart Hostel Management",
    page_icon="🏠",
    layout="wide"
)

DB = "hostel.db"


# =========================================================
# DATABASE
# =========================================================

def db():
    conn = sqlite3.connect(DB, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def init_db():

    conn = db()
    cur = conn.cursor()

    cur.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        name TEXT NOT NULL,
        active INTEGER DEFAULT 1
    );

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        student_id TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        phone TEXT,
        email TEXT,
        branch TEXT,
        year TEXT,
        hostel TEXT,
        block TEXT,
        room TEXT,
        bed TEXT,
        total_fee REAL DEFAULT 80000,
        paid_fee REAL DEFAULT 0
    );

    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_no TEXT UNIQUE NOT NULL,
        block TEXT NOT NULL,
        floor INTEGER DEFAULT 1,
        room_type TEXT NOT NULL,
        total_beds INTEGER DEFAULT 2,
        status TEXT DEFAULT 'Available'
    );

    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        category TEXT,
        subject TEXT,
        description TEXT,
        priority TEXT,
        status TEXT DEFAULT 'Submitted',
        created_at TEXT
    );

    CREATE TABLE IF NOT EXISTS leaves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        start_date TEXT,
        end_date TEXT,
        reason TEXT,
        destination TEXT,
        status TEXT DEFAULT 'Pending',
        created_at TEXT
    );

    CREATE TABLE IF NOT EXISTS announcements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        message TEXT,
        priority TEXT,
        created_at TEXT
    );

    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id TEXT,
        amount REAL,
        method TEXT,
        transaction_id TEXT,
        paid_at TEXT
    );

    CREATE TABLE IF NOT EXISTS meals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meal_date TEXT,
        breakfast TEXT,
        lunch TEXT,
        snacks TEXT,
        dinner TEXT
    );
    """)

    # -----------------------------------------------------
    # DEMO USERS
    # -----------------------------------------------------

    if cur.execute(
        "SELECT COUNT(*) FROM users"
    ).fetchone()[0] == 0:

        cur.execute(
            """
            INSERT INTO users
            (username, password, role, name)
            VALUES (?, ?, ?, ?)
            """,
            (
                "admin",
                hash_password("admin123"),
                "admin",
                "Hostel Administrator"
            )
        )

        cur.execute(
            """
            INSERT INTO users
            (username, password, role, name)
            VALUES (?, ?, ?, ?)
            """,
            (
                "student",
                hash_password("student123"),
                "student",
                "Rahul Kumar"
            )
        )

        student_user_id = cur.lastrowid

        cur.execute(
            """
            INSERT INTO students
            (
                user_id,
                student_id,
                name,
                phone,
                email,
                branch,
                year,
                hostel,
                block,
                room,
                bed,
                total_fee,
                paid_fee
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                student_user_id,
                "STU001",
                "Rahul Kumar",
                "9876543210",
                "rahul@example.com",
                "Mechanical Engineering",
                "2nd Year",
                "ABC College Boys Hostel",
                "A",
                "A101",
                "Bed 1",
                80000,
                30000
            )
        )

    # -----------------------------------------------------
    # DEMO ROOMS
    # -----------------------------------------------------

    if cur.execute(
        "SELECT COUNT(*) FROM rooms"
    ).fetchone()[0] == 0:

        rooms = [
            ("A101", "A", 1, "Double", 2, "Occupied"),
            ("A102", "A", 1, "Double", 2, "Available"),
            ("A103", "A", 1, "Triple", 3, "Available"),
            ("B201", "B", 2, "Four Sharing", 4, "Occupied"),
            ("B202", "B", 2, "Four Sharing", 4, "Available")
        ]

        cur.executemany(
            """
            INSERT INTO rooms
            (
                room_no,
                block,
                floor,
                room_type,
                total_beds,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            rooms
        )

    # -----------------------------------------------------
    # MEAL
    # -----------------------------------------------------

    if cur.execute(
        "SELECT COUNT(*) FROM meals"
    ).fetchone()[0] == 0:

        cur.execute(
            """
            INSERT INTO meals
            (
                meal_date,
                breakfast,
                lunch,
                snacks,
                dinner
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                str(date.today()),
                "Idli, Sambar, Chutney",
                "Rice, Dal, Vegetable Curry",
                "Tea, Biscuits",
                "Chapati, Paneer Curry"
            )
        )

    # -----------------------------------------------------
    # ANNOUNCEMENTS
    # -----------------------------------------------------

    if cur.execute(
        "SELECT COUNT(*) FROM announcements"
    ).fetchone()[0] == 0:

        cur.execute(
            """
            INSERT INTO announcements
            (title, message, priority, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                "Welcome to Hostel Portal",
                "Hostel fee payment and room services are now available.",
                "Important",
                now()
            )
        )

        cur.execute(
            """
            INSERT INTO announcements
            (title, message, priority, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (
                "Maintenance Notice",
                "Water maintenance is scheduled for Sunday.",
                "Normal",
                now()
            )
        )

    conn.commit()
    conn.close()


# =========================================================
# DATABASE HELPERS
# =========================================================

def query(sql, params=(), one=False):

    conn = db()

    rows = conn.execute(
        sql,
        params
    ).fetchall()

    conn.close()

    if one:
        return rows[0] if rows else None

    return rows


def execute(sql, params=()):

    conn = db()

    cur = conn.execute(
        sql,
        params
    )

    conn.commit()

    last_id = cur.lastrowid

    conn.close()

    return last_id


def money(value):

    return f"₹{float(value):,.0f}"


# =========================================================
# CSS / 3D STYLE
# =========================================================

def inject_css():

    st.markdown(
        """
        <style>

        .stApp {

            background:

            radial-gradient(
                circle at 10% 10%,
                rgba(0,140,255,0.30),
                transparent 30%
            ),

            radial-gradient(
                circle at 90% 15%,
                rgba(170,50,255,0.30),
                transparent 30%
            ),

            radial-gradient(
                circle at 50% 90%,
                rgba(0,220,255,0.10),
                transparent 35%
            ),

            linear-gradient(
                135deg,
                #050b16,
                #0b1730,
                #120a24
            );

            color: white;
        }

        .hero {

            padding: 40px;

            border-radius: 30px;

            margin-bottom: 25px;

            background:

            linear-gradient(
                135deg,
                rgba(0,140,255,0.20),
                rgba(170,60,255,0.18)
            );

            border:
                1px solid rgba(255,255,255,0.18);

            box-shadow:

                0 25px 70px
                rgba(0,0,0,0.45),

                inset 0 1px 1px
                rgba(255,255,255,0.10);

            backdrop-filter: blur(15px);
        }

        .hero h1 {

            font-size: 44px;

            font-weight: 800;

            margin: 0;
        }

        .hero p {

            font-size: 18px;

            color: #cbd5e1;
        }

        .glass-card {

            padding: 25px;

            border-radius: 24px;

            background:
                rgba(255,255,255,0.07);

            border:
                1px solid rgba(255,255,255,0.13);

            box-shadow:

                0 15px 45px
                rgba(0,0,0,0.30);

            backdrop-filter:
                blur(15px);
        }

        [data-testid="stSidebar"] {

            background:
                rgba(4,10,22,0.95);
        }

        div.stButton > button {

            border-radius: 12px;

            font-weight: 700;
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# LOGOUT
# =========================================================

def logout():

    st.session_state.clear()

    st.rerun()


# =========================================================
# LOGIN
# =========================================================

def login_screen():

    st.markdown(
        """
        <div class="hero">

            <h1>
                🏠 Smart Hostel Management System
            </h1>

            <p>
                Rooms • Fees • Meals • Complaints • Leave • Administration
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns([1.2, 1])

    with left:

        st.subheader("🔐 Login")

        role = st.radio(
            "Login As",
            ["Student", "Admin"],
            horizontal=True
        )

        username = st.text_input(
            "Username"
        )

        password = st.text_input(
            "Password",
            type="password"
        )

        login = st.button(
            "LOGIN",
            type="primary",
            use_container_width=True
        )

        if login:

            user = query(
                """
                SELECT *
                FROM users
                WHERE username=?
                AND password=?
                AND role=?
                AND active=1
                """,
                (
                    username,
                    hash_password(password),
                    role.lower()
                ),
                one=True
            )

            if user:

                st.session_state.user_id = user["id"]

                st.session_state.role = user["role"]

                st.session_state.name = user["name"]

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    with right:

        st.markdown(
            """
            <div class="glass-card">

            <h2>🎓 Student Demo</h2>

            Username:
            <b>student</b>

            <br><br>

            Password:
            <b>student123</b>

            <hr>

            <h2>👨‍💼 Admin Demo</h2>

            Username:
            <b>admin</b>

            <br><br>

            Password:
            <b>admin123</b>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# STUDENT SIDEBAR
# =========================================================

def student_nav():

    with st.sidebar:

        st.title("🏠 Hostel Portal")

        st.success(
            f"🎓 {st.session_state.name}"
        )

        page = st.radio(
            "Navigation",
            [
                "Dashboard",
                "My Profile",
                "Room Details",
                "Hostel Fee",
                "Payment History",
                "Meals / Mess",
                "Complaints",
                "Leave",
                "Announcements",
                "Notifications",
                "Settings"
            ]
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout()

    return page


# =========================================================
# ADMIN SIDEBAR
# =========================================================

def admin_nav():

    with st.sidebar:

        st.title("🏢 Admin Portal")

        st.success(
            "👨‍💼 Administrator"
        )

        page = st.radio(
            "Admin Navigation",
            [
                "Dashboard",
                "Students",
                "Rooms",
                "Room Allocation",
                "Hostel Fees",
                "Payments",
                "Meal Management",
                "Complaints",
                "Leave Requests",
                "Announcements",
                "Reports",
                "Settings"
            ]
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            logout()

    return page


# =========================================================
# GET CURRENT STUDENT
# =========================================================

def get_student():

    return query(
        """
        SELECT *
        FROM students
        WHERE user_id=?
        """,
        (st.session_state.user_id,),
        one=True
    )


# =========================================================
# STUDENT APPLICATION
# =========================================================

def student_app():

    page = student_nav()

    student = get_student()

    if not student:

        st.error(
            "Student profile not found."
        )

        return

    # -----------------------------------------------------
    # DASHBOARD
    # -----------------------------------------------------

    if page == "Dashboard":

        st.markdown(
            f"""
            <div class="hero">

                <h1>
                    🎓 Welcome, {student["name"]}
                </h1>

                <p>
                    Student ID:
                    {student["student_id"]}
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        pending = max(
            0,
            student["total_fee"] -
            student["paid_fee"]
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🏠 Room",
            student["room"] or "-"
        )

        c2.metric(
            "🛏️ Bed",
            student["bed"] or "-"
        )

        c3.metric(
            "💰 Paid",
            money(student["paid_fee"])
        )

        c4.metric(
            "⚠️ Pending",
            money(pending)
        )

        st.success(
            "🍽️ Meal charges are included in your hostel fee. "
            "No additional payment is required."
        )

        st.subheader(
            "🍽️ Today's Menu"
        )

        meal = query(
            """
            SELECT *
            FROM meals
            WHERE meal_date=?
            """,
            (str(date.today()),),
            one=True
        )

        if meal:

            st.dataframe(
                pd.DataFrame(
                    [{
                        "Breakfast":
                            meal["breakfast"],

                        "Lunch":
                            meal["lunch"],

                        "Snacks":
                            meal["snacks"],

                        "Dinner":
                            meal["dinner"]
                    }]
                ),
                use_container_width=True,
                hide_index=True
            )

        st.subheader(
            "📢 Latest Announcements"
        )

        announcements = query(
            """
            SELECT *
            FROM announcements
            ORDER BY id DESC
            LIMIT 3
            """
        )

        for announcement in announcements:

            st.info(
                f"**{announcement['title']}**\n\n"
                f"{announcement['message']}"
            )

    # -----------------------------------------------------
    # PROFILE
    # -----------------------------------------------------

    elif page == "My Profile":

        st.title(
            "👤 My Profile"
        )

        with st.form(
            "student_profile"
        ):

            name = st.text_input(
                "Full Name",
                student["name"]
            )

            phone = st.text_input(
                "Phone",
                student["phone"] or ""
            )

            email = st.text_input(
                "Email",
                student["email"] or ""
            )

            branch = st.text_input(
                "Branch",
                student["branch"] or ""
            )

            years = [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ]

            current_year = (
                years.index(student["year"])
                if student["year"] in years
                else 0
            )

            year = st.selectbox(
                "Year",
                years,
                index=current_year
            )

            save = st.form_submit_button(
                "💾 Save Changes",
                type="primary"
            )

        if save:

            execute(
                """
                UPDATE students
                SET name=?,
                    phone=?,
                    email=?,
                    branch=?,
                    year=?
                WHERE id=?
                """,
                (
                    name,
                    phone,
                    email,
                    branch,
                    year,
                    student["id"]
                )
            )

            execute(
                """
                UPDATE users
                SET name=?
                WHERE id=?
                """,
                (
                    name,
                    st.session_state.user_id
                )
            )

            st.session_state.name = name

            st.success(
                "Profile updated successfully!"
            )

    # -----------------------------------------------------
    # ROOM
    # -----------------------------------------------------

    elif p
