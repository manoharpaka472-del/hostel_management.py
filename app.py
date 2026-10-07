import streamlit as st
import sqlite3
import hashlib
from datetime import datetime

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Hostel Management",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect(
    "hostel.db",
    check_same_thread=False
)

conn.row_factory = sqlite3.Row
cursor = conn.cursor()


# =========================================================
# CREATE TABLES
# =========================================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    name TEXT NOT NULL,
    active INTEGER DEFAULT 1
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    student_id TEXT UNIQUE NOT NULL,
    phone TEXT,
    email TEXT,
    branch TEXT,
    year TEXT,
    college TEXT,
    hostel TEXT,
    block TEXT,
    room TEXT,
    bed TEXT,
    guardian_name TEXT,
    guardian_phone TEXT,
    address TEXT,
    joining_date TEXT,
    hostel_fee REAL DEFAULT 80000,
    paid_fee REAL DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    room_number TEXT UNIQUE NOT NULL,
    block TEXT,
    floor TEXT,
    room_type TEXT,
    total_beds INTEGER,
    status TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS meals (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    meal_date TEXT,
    breakfast TEXT,
    lunch TEXT,
    snacks TEXT,
    dinner TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    category TEXT,
    subject TEXT,
    description TEXT,
    priority TEXT,
    status TEXT DEFAULT 'Submitted',
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS leave_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id TEXT,
    start_date TEXT,
    end_date TEXT,
    reason TEXT,
    destination TEXT,
    status TEXT DEFAULT 'Pending',
    remarks TEXT
)
""")

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


# =========================================================
# PASSWORD
# =========================================================

def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


# =========================================================
# DEMO DATA
# =========================================================

# ADMIN

admin = cursor.execute(
    "SELECT * FROM users WHERE username=?",
    ("admin",)
).fetchone()

if admin is None:

    cursor.execute("""
        INSERT INTO users
        (username, password, role, name, active)
        VALUES (?, ?, ?, ?, ?)
    """, (
        "admin",
        hash_password("admin123"),
        "admin",
        "Hostel Administrator",
        1
    ))

# STUDENT USER

student_user = cursor.execute(
    "SELECT * FROM users WHERE username=?",
    ("student",)
).fetchone()

if student_user is None:

    cursor.execute("""
        INSERT INTO users
        (username, password, role, name, active)
        VALUES (?, ?, ?, ?, ?)
    """, (
        "student",
        hash_password("student123"),
        "student",
        "Rahul Kumar",
        1
    ))

# STUDENT PROFILE

student = cursor.execute(
    "SELECT * FROM students WHERE username=?",
    ("student",)
).fetchone()

if student is None:

    cursor.execute("""
        INSERT INTO students
        (
            username,
            student_id,
            phone,
            email,
            branch,
            year,
            college,
            hostel,
            block,
            room,
            bed,
            guardian_name,
            guardian_phone,
            address,
            joining_date,
            hostel_fee,
            paid_fee
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "student",
        "STU001",
        "9876543210",
        "student@example.com",
        "Mechanical Engineering",
        "2nd Year",
        "ABC College",
        "ABC College Boys Hostel",
        "Block A",
        "A101",
        "Bed 1",
        "Ramesh Kumar",
        "9876500000",
        "Hyderabad, Telangana",
        "01-07-2026",
        80000,
        30000
    ))

# ROOMS

rooms = [
    ("A101", "A", "1", "Double", 2, "Occupied"),
    ("A102", "A", "1", "Double", 2, "Available"),
    ("A103", "A", "1", "Triple", 3, "Available"),
    ("B201", "B", "2", "Four Sharing", 4, "Available"),
    ("B202", "B", "2", "Four Sharing", 4, "Available"),
]

for room in rooms:

    exists = cursor.execute(
        "SELECT * FROM rooms WHERE room_number=?",
        (room[0],)
    ).fetchone()

    if exists is None:

        cursor.execute("""
            INSERT INTO rooms
            (
                room_number,
                block,
                floor,
                room_type,
                total_beds,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, room)

# ANNOUNCEMENT

announcement = cursor.execute(
    "SELECT * FROM announcements LIMIT 1"
).fetchone()

if announcement is None:

    cursor.execute("""
        INSERT INTO announcements
        (title, message, category, priority, created_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        "Welcome to Smart Hostel",
        "Hostel management system is now active.",
        "General",
        "Normal",
        datetime.now().strftime("%d-%m-%Y")
    ))

conn.commit()


# =========================================================
# SESSION
# =========================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = ""

if "username" not in st.session_state:
    st.session_state.username = ""

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(20, 90, 170, 0.45),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 15%,
            rgba(100, 40, 160, 0.40),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #07111f,
            #10182f 50%,
            #080d1c
        );

    color: white;
}

.block-container {
    padding-top: 2rem;
}

.hero {

    padding: 45px;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(31, 94, 170, 0.35),
            rgba(93, 43, 150, 0.35)
        );

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35);

    margin-bottom: 30px;
}

.hero h1 {

    font-size: 42px;

    font-weight: 800;

    margin-bottom: 10px;
}

.hero p {

    font-size: 18px;

    color: #cbd5e1;
}

.card {

    padding: 25px;

    border-radius: 20px;

    background:
        rgba(255,255,255,0.08);

    border:
        1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 10px 35px rgba(0,0,0,0.20);

}

.card h3 {

    margin-top: 0;

    color: white;
}

.big-number {

    font-size: 32px;

    font-weight: 800;

    color: #61c7ff;
}

.login-box {

    max-width: 600px;

    margin: auto;

    padding: 35px;

    border-radius: 25px;

    background:
        rgba(255,255,255,0.08);

    border:
        1px solid rgba(255,255,255,0.15);

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOGIN
# =========================================================

def login_page():

    st.markdown("""
    <div class="hero">

        <h1>🏠 Smart Hostel Management</h1>

        <p>
        Manage rooms, hostel fees, meals, complaints,
        leave requests and hostel operations from one platform.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="login-box">',
        unsafe_allow_html=True
    )

    st.subheader("🔐 Login")

    login_type = st.radio(
        "Login Type",
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

    if st.button(
        "🔐 Login",
        use_container_width=True,
        type="primary"
    ):

        user = cursor.execute("""
            SELECT *
            FROM users
            WHERE username=?
        """, (username,)).fetchone()

        if user is None:

            st.error(
                "Username does not exist."
            )

        elif user["active"] == 0:

            st.error(
                "This account is disabled."
            )

        elif hash_password(password) != user["password"]:

            st.error(
                "Incorrect password."
            )

        elif login_type.lower() != user["role"]:

            st.error(
                "Wrong login type selected."
            )

        else:

            st.session_state.logged_in = True
            st.session_state.role = user["role"]
            st.session_state.username = user["username"]
            st.session_state.page = "Dashboard"

            st.success(
                "Login successful."
            )

            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
        **Student Demo**

        Username: `student`

        Password: `student123`
        """)

    with col2:

        st.warning("""
        **Admin Demo**

        Username: `admin`

        Password: `admin123`
        """)


# =========================================================
# STUDENT PROFILE
# =========================================================

def student_profile():

    student = cursor.execute("""
        SELECT *
        FROM students
        WHERE username=?
    """, (st.session_state.username,)).fetchone()

    if student is None:

        st.error("Student profile not found.")

        return

    st.title("👤 My Profile")

    with st.form("student_profile_form"):

        col1, col2 = st.columns(2)

        with col1:

            phone = st.text_input(
                "Phone",
                value=student["phone"] or ""
            )

            email = st.text_input(
                "Email",
                value=student["email"] or ""
            )

            guardian = st.text_input(
                "Guardian Name",
                value=student["guardian_name"] or ""
            )

            guardian_phone = st.text_input(
                "Guardian Phone",
                value=student["guardian_phone"] or ""
            )

        with col2:

            address = st.text_area(
                "Address",
                value=student["address"] or ""
            )

            branch = st.text_input(
                "Branch",
                value=student["branch"] or ""
            )

            year = st.text_input(
                "Year",
                value=student["year"] or ""
            )

        if st.form_submit_button(
            "💾 Save Profile",
            use_container_width=True
        ):

            cursor.execute("""
                UPDATE students
                SET
                    phone=?,
                    email=?,
                    guardian_name=?,
                    guardian_phone=?,
                    address=?,
                    branch=?,
                    year=?
                WHERE username=?
            """, (
                phone,
                email,
                guardian,
                guardian_phone,
                address,
                branch,
                year,
                st.session_state.username
            ))

            conn.commit()

            st.success(
                "Profile updated successfully."
            )

            st.rerun()


# =========================================================
# STUDENT DASHBOARD
# =========================================================

def student_dashboard():

    student = cursor.execute("""
        SELECT *
        FROM students
        WHERE username=?
    """, (st.session_state.username,)).fetchone()

    if student is None:

        st.error("Student data not found.")

        return

    st.markdown("""
    <div class="hero">

        <h1>🎓 Student Dashboard</h1>

        <p>
        Welcome to your hostel management portal.
        </p>

    </div>
    """, unsafe_allow_html=True)

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

        pending = (
            student["hostel_fee"]
            - student["paid_fee"]
        )

        st.metric(
            "💰 Pending Fee",
            f"₹{pending:,.0f}"
        )

    with col4:

        st.metric(
            "📚 Year",
            student["year"]
        )

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">

        <h3>🏠 Hostel Information</h3>

        </div>
        """, unsafe_allow_html=True)

        st.write(
            "**Hostel:**",
            student["hostel"]
        )

        st.write(
            "**Block:**",
            student["block"]
        )

        st.write(
            "**Room:**",
            student["room"]
        )

        st.write(
            "**Bed:**",
            student["bed"]
        )

    with col2:

        st.markdown("""
        <div class="card">

        <h3>💰 Fee Information</h3>

        </div>
        """, unsafe_allow_html=True)

        st.write(
            f"Total Hostel Fee: ₹{student['hostel_fee']:,.0f}"
        )

        st.write(
            f"Paid: ₹{student['paid_fee']:,.0f}"
        )

        st.write(
            f"Pending: ₹{pending:,.0f}"
        )

        st.info(
            "Meal charges are included in your hostel fee. "
            "No additional payment is required."
        )


# =========================================================
# STUDENT ROOM
# =========================================================

def student_room():

    student = cursor.execute("""
        SELECT *
        FROM students
        WHERE username=?
    """, (st.session_state.username,)).fetchone()

    st.title("🏠 Room Details")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Hostel",
            student["hostel"]
        )

    with col2:

        st.metric(
            "Block",
            student["block"]
        )

    with col3:

        st.metric(
            "Room",
            student["room"]
        )

    st.divider()

    st.subheader("🛏️ Bed Information")

    st.success(
        f"You are allocated to {student['bed']}."
    )


# =========================================================
# STUDENT FEES
# =========================================================

def student_fees():

    student = cursor.execute("""
        SELECT *
        FROM students
        WHERE username=?
    """, (st.session_state.username,)).fetchone()

    st.title("💰 Hostel Fee")

    total = student["hostel_fee"]
    paid = student["paid_fee"]
    pending = total - paid

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Fee",
            f"₹{total:,.0f}"
        )

    with col2:
        st.metric(
            "Paid",
            f"₹{paid:,.0f}"
        )

    with col3:
        st.metric(
            "Pending",
            f"₹{pending:,.0f}"
        )

    st.divider()

    st.info(
        "Your hostel fee is a combined fee covering "
        "accommodation, utilities, maintenance and mess/meal facility."
    )

    st.success(
        "🍽️ Meal charges are included in your hostel fee. "
        "No additional payment is required."
    )

    payment = st.number_input(
        "Payment Amount",
        min_value=0.0,
        max_value=float(pending),
        value=0.0
    )

    method = st.selectbox(
        "Payment Method",
        [
            "UPI",
            "Card",
            "Net Banking"
        ]
    )

    if st.button(
        "💳 Pay Hostel Fee",
        type="primary"
    ):

        if payment <= 0:

            st.error(
                "Enter a valid payment amount."
            )

        else:

            new_paid = paid + payment

            cursor.execute("""
                UPDATE students
                SET paid_fee=?
                WHERE username=?
            """, (
                new_paid,
                st.session_state.username
            ))

            conn.commit()

            transaction_id = (
                "TXN"
                + datetime.now().strftime("%Y%m%d%H%M%S")
            )

            st.success(
                "Payment successful."
            )

            st.write(
                "**Transaction ID:**",
                transaction_id
            )

            st.write(
                "**Amount:**",
                f"₹{payment:,.2f}"
            )

            st.write(
                "**Method:**",
                method
            )


# =========================================================
# MEALS
# =========================================================

def student_meals():

    st.title("🍽️ Meal / Mess")

    st.success(
        "Meal charges are included in your hostel fee. "
        "No additional payment is required."
    )

    st.subheader("Today's Menu")

    meals = [
        ("🌅 Breakfast", "Idli, Sambar, Chutney"),
        ("☀️ Lunch", "Rice, Dal, Vegetable Curry"),
        ("🍪 Snacks", "Tea and Biscuits"),
        ("🌙 Dinner", "Chapati, Paneer Curry, Rice")
    ]

    for name, food in meals:

        with st.container(border=True):

            st.subheader(name)

            st.write(food)

            if st.button(
                "Book Meal",
                key="meal_" + name
            ):

                st.success(
                    name + " booked successfully."
                )


# =========================================================
# COMPLAINTS
# =========================================================

def student_complaints():

    st.title("🛠️ Complaints")

    with st.form("complaint_form"):

        category = st.selectbox(
            "Category",
            [
                "Food",
                "Room",
                "Electricity",
                "Water",
                "WiFi",
                "Cleaning",
                "Security",
                "Maintenance",
                "Other"
            ]
        )

        subject = st.text_input(
            "Subject"
        )

        description = st.text_area(
            "Description"
        )

        priority = st.selectbox(
            "Priority",
            [
                "Low",
                "Medium",
                "High",
                "Emergency"
            ]
        )

        submit = st.form_submit_button(
            "Submit Complaint"
        )

        if submit:
