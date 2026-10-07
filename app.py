import streamlit as st
import sqlite3
import hashlib
import secrets
import os
import csv
import io
from datetime import datetime, date, timedelta

# ============================================================
# CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Hostel Management System",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

DB_FILE = "hostel.db"

# ============================================================
# DATABASE
# ============================================================

def get_db():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def execute(sql, params=(), fetch=False, many=False):
    conn = get_db()
    cur = conn.cursor()

    if many:
        cur.executemany(sql, params)
    else:
        cur.execute(sql, params)

    if fetch:
        result = cur.fetchall()
        conn.close()
        return result

    conn.commit()
    last_id = cur.lastrowid
    conn.close()
    return last_id


def hash_password(password):
    salt = secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        120000
    ).hex()
    return f"{salt}${hashed}"


def verify_password(password, stored):
    try:
        salt, hashed = stored.split("$")
        check = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt.encode(),
            120000
        ).hex()
        return secrets.compare_digest(check, hashed)
    except Exception:
        return False


def init_db():

    conn = get_db()
    c = conn.cursor()

    c.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('student','admin')),
        active INTEGER DEFAULT 1,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER UNIQUE,
        student_id TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        dob TEXT,
        gender TEXT,
        phone TEXT,
        email TEXT,
        guardian_name TEXT,
        guardian_phone TEXT,
        address TEXT,
        course TEXT,
        branch TEXT,
        year TEXT,
        college TEXT,
        hostel TEXT,
        block TEXT,
        room TEXT,
        bed INTEGER,
        joining_date TEXT,
        profile_photo TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS hostels (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        address TEXT,
        phone TEXT,
        email TEXT
    );

    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hostel TEXT,
        block TEXT,
        floor INTEGER,
        room_number TEXT UNIQUE,
        room_type TEXT,
        total_beds INTEGER,
        status TEXT DEFAULT 'Available'
    );

    CREATE TABLE IF NOT EXISTS beds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_id INTEGER,
        bed_number INTEGER,
        occupied INTEGER DEFAULT 0,
        student_id INTEGER,
        FOREIGN KEY(room_id) REFERENCES rooms(id),
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS hostel_fees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        academic_year TEXT,
        total_fee REAL DEFAULT 80000,
        discount REAL DEFAULT 0,
        paid REAL DEFAULT 0,
        due_date TEXT,
        status TEXT DEFAULT 'Pending',
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        receipt_number TEXT UNIQUE,
        transaction_id TEXT UNIQUE,
        amount REAL,
        method TEXT,
        payment_date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS meal_menus (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        menu_date TEXT,
        breakfast TEXT,
        lunch TEXT,
        snacks TEXT,
        dinner TEXT,
        UNIQUE(menu_date)
    );

    CREATE TABLE IF NOT EXISTS meal_bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        booking_date TEXT,
        meal TEXT,
        status TEXT DEFAULT 'Booked',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(student_id, booking_date, meal),
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS leave_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        start_date TEXT,
        end_date TEXT,
        reason TEXT,
        destination TEXT,
        guardian_contact TEXT,
        status TEXT DEFAULT 'Pending',
        remarks TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS complaints (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        category TEXT,
        subject TEXT,
        description TEXT,
        priority TEXT,
        status TEXT DEFAULT 'Submitted',
        admin_comment TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS maintenance_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        category TEXT,
        description TEXT,
        priority TEXT,
        status TEXT DEFAULT 'Submitted',
        staff TEXT,
        comment TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS room_change_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        current_room TEXT,
        preferred_room TEXT,
        reason TEXT,
        comments TEXT,
        status TEXT DEFAULT 'Pending',
        remarks TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(student_id) REFERENCES students(id)
    );

    CREATE TABLE IF NOT EXISTS announcements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        priority TEXT,
        announcement_date TEXT,
        expiry_date TEXT
    );

    CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        message TEXT,
        is_read INTEGER DEFAULT 0,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    );

    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT,
        details TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()

    seed_data()


# ============================================================
# SEED DATA
# ============================================================

def seed_data():

    # Admin
    admin = execute(
        "SELECT id FROM users WHERE username=?",
        ("admin",),
        fetch=True
    )

    if not admin:
        admin_id = execute(
            """
            INSERT INTO users(username,password,role)
            VALUES(?,?,?)
            """,
            ("admin", hash_password("Admin@123"), "admin")
        )
    else:
        admin_id = admin[0]["id"]

    # Student
    student_user = execute(
        "SELECT id FROM users WHERE username=?",
        ("student001",),
        fetch=True
    )

    if not student_user:

        uid = execute(
            """
            INSERT INTO users(username,password,role)
            VALUES(?,?,?)
            """,
            ("student001", hash_password("Student@123"), "student")
        )

        execute(
            """
            INSERT INTO students(
                user_id,student_id,name,dob,gender,phone,email,
                guardian_name,guardian_phone,address,course,branch,
                year,college,hostel,block,room,bed,joining_date
            )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                uid,
                "STU001",
                "Rahul Kumar",
                "2006-04-15",
                "Male",
                "9876543210",
                "rahul@example.com",
                "Ramesh Kumar",
                "9876500000",
                "Hyderabad, Telangana",
                "B.Tech",
                "Mechanical Engineering",
                "2nd Year",
                "ABC College",
                "ABC College Boys Hostel",
                "Block A",
                "A101",
                1,
                "2026-07-01"
            )
        )

    # Hostels
    if not execute(
        "SELECT id FROM hostels LIMIT 1",
        fetch=True
    ):
        execute(
            """
            INSERT INTO hostels(name,address,phone,email)
            VALUES(?,?,?,?)
            """,
            (
                "ABC College Boys Hostel",
                "ABC College Campus, Telangana",
                "9876543210",
                "hostel@example.com"
            )
        )

    # Rooms
    rooms = [
        ("ABC College Boys Hostel", "Block A", 1, "A101", "Four-sharing", 4),
        ("ABC College Boys Hostel", "Block A", 1, "A102", "Four-sharing", 4),
        ("ABC College Boys Hostel", "Block A", 1, "A103", "Triple", 3),
        ("ABC College Boys Hostel", "Block B", 2, "B201", "Four-sharing", 4),
        ("ABC College Boys Hostel", "Block B", 2, "B202", "Double", 2),
    ]

    for r in rooms:

        exists = execute(
            "SELECT id FROM rooms WHERE room_number=?",
            (r[3],),
            fetch=True
        )

        if not exists:
            room_id = execute(
                """
                INSERT INTO rooms(
                    hostel,block,floor,room_number,
                    room_type,total_beds
                )
                VALUES(?,?,?,?,?,?)
                """,
                r
            )

            for bed_no in range(1, r[5] + 1):
                execute(
                    """
                    INSERT INTO beds(room_id,bed_number)
                    VALUES(?,?)
                    """,
                    (room_id, bed_no)
                )

    # Allocate demo student
    student = execute(
        "SELECT id FROM students WHERE student_id='STU001'",
        fetch=True
    )

    room = execute(
        "SELECT id FROM rooms WHERE room_number='A101'",
        fetch=True
    )

    if student and room:

        already = execute(
            """
            SELECT id FROM beds
            WHERE room_id=? AND bed_number=1
            """,
            (room[0]["id"],),
            fetch=True
        )

        if already:
            execute(
                """
                UPDATE beds
                SET occupied=1,student_id=?
                WHERE room_id=? AND bed_number=1
                """,
                (student[0]["id"], room[0]["id"])
            )

    # Fee
    if student:

        fee = execute(
            "SELECT id FROM hostel_fees WHERE student_id=?",
            (student[0]["id"],),
            fetch=True
        )

        if not fee:
            execute(
                """
                INSERT INTO hostel_fees(
                    student_id,academic_year,total_fee,
                    discount,paid,due_date,status
                )
                VALUES(?,?,?,?,?,?,?)
                """,
                (
                    student[0]["id"],
                    "2026-27",
                    80000,
                    0,
                    30000,
                    "2026-12-15",
                    "Partially Paid"
                )
            )

    # Menus
    today = date.today()

    for i in range(7):

        d = today + timedelta(days=i)
        ds = d.isoformat()

        exists = execute(
            "SELECT id FROM meal_menus WHERE menu_date=?",
            (ds,),
            fetch=True
        )

        if not exists:
            execute(
                """
                INSERT INTO meal_menus(
                    menu_date,breakfast,lunch,snacks,dinner
                )
                VALUES(?,?,?,?,?)
                """,
                (
                    ds,
                    "Idli + Sambar + Tea",
                    "Rice + Dal + Vegetable Curry + Curd",
                    "Tea + Biscuits",
                    "Chapati + Paneer Curry + Rice"
                )
            )

    # Announcement
    if not execute(
        "SELECT id FROM announcements LIMIT 1",
        fetch=True
    ):
        execute(
            """
            INSERT INTO announcements(
                title,description,priority,
                announcement_date,expiry_date
            )
            VALUES(?,?,?,?,?)
            """,
            (
                "Welcome to the New Academic Year",
                "Students are requested to follow hostel rules and maintain cleanliness.",
                "Normal",
                str(today),
                str(today + timedelta(days=30))
            )
        )


init_db()


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

.main-title {
    font-size: 2.3rem;
    font-weight: 800;
}

.subtitle {
    color: #64748b;
}

.card {
    padding: 22px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e2e8f0;
    box-shadow: 0 5px 18px rgba(15,23,42,0.06);
    margin-bottom: 15px;
}

.metric-card {
    padding: 20px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e2e8f0;
    box-shadow: 0 5px 15px rgba(15,23,42,0.05);
}

.metric-title {
    color: #64748b;
    font-size: 14px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    margin-top: 5px;
}

.success-box {
    padding: 15px;
    border-radius: 12px;
    background: #ecfdf5;
    border: 1px solid #a7f3d0;
}

.warning-box {
    padding: 15px;
    border-radius: 12px;
    background: #fffbeb;
    border: 1px solid #fde68a;
}

.info-box {
    padding: 15px;
    border-radius: 12px;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
}

.danger-box {
    padding: 15px;
    border-radius: 12px;
    background: #fef2f2;
    border: 1px solid #fecaca;
}

.login-box {
    max-width: 500px;
    margin: 50px auto;
}

.status-paid {
    color: #059669;
    font-weight: bold;
}

.status-pending {
    color: #d97706;
    font-weight: bold;
}

.status-danger {
    color: #dc2626;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HELPERS
# ============================================================

def money(value):
    return f"₹{value:,.2f}"


def notify(user_id, title, message):
    execute(
        """
        INSERT INTO notifications(user_id,title,message)
        VALUES(?,?,?)
        """,
        (user_id, title, message)
    )


def audit(user_id, action, details):
    execute(
        """
        INSERT INTO audit_logs(user_id,action,details)
        VALUES(?,?,?)
        """,
        (user_id, action, details)
    )


def get_student(user_id):
    rows = execute(
        "SELECT * FROM students WHERE user_id=?",
        (user_id,),
        fetch=True
    )
    return rows[0] if rows else None


def get_student_by_id(student_id):
    rows = execute(
        "SELECT * FROM students WHERE id=?",
        (student_id,),
        fetch=True
    )
    return rows[0] if rows else None


def get_room(room_number):
    rows = execute(
        "SELECT * FROM rooms WHERE room_number=?",
        (room_number,),
        fetch=True
    )
    return rows[0] if rows else None


def available_beds(room_id):
    return execute(
        """
        SELECT * FROM beds
        WHERE room_id=? AND occupied=0
        """,
        (room_id,),
        fetch=True
    )


def update_room_status(room_id):
    room = execute(
        "SELECT * FROM rooms WHERE id=?",
        (room_id,),
        fetch=True
    )[0]

    occupied = execute(
        """
        SELECT COUNT(*) AS c FROM beds
        WHERE room_id=? AND occupied=1
        """,
        (room_id,),
        fetch=True
    )[0]["c"]

    if occupied == 0:
        status = "Available"
    elif occupied >= room["total_beds"]:
        status = "Full"
    else:
        status = "Partially Occupied"

    execute(
        "UPDATE rooms SET status=? WHERE id=?",
        (status, room_id)
    )


# ============================================================
# LOGIN
# ============================================================

def login_page():

    st.markdown(
        "<div class='login-box'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center;'>🏠 Smart Hostel</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;color:#64748b;'>"
        "Hostel Management System"
        "</p>",
        unsafe_allow_html=True
    )

    tab1, tab2 = st.tabs(["🎓 Student Login", "🛡️ Admin Login"])

    with tab1:

        username = st.text_input(
            "Student ID / Username",
            key="student_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="student_password"
        )

        remember = st.checkbox(
            "Remember me",
            key="student_remember"
        )

        if st.button(
            "Login as Student",
            use_container_width=True,
            type="primary"
        ):

            user = execute(
                """
                SELECT * FROM users
                WHERE username=? AND role='student'
                """,
                (username,),
                fetch=True
            )

            if user and user[0]["active"] and verify_password(
                password,
                user[0]["password"]
            ):

                st.session_state.logged_in = True
                st.session_state.user_id = user[0]["id"]
                st.session_state.role = "student"

                st.rerun()

            else:
                st.error("Invalid student username or password.")

    with tab2:

        username = st.text_input(
            "Admin Username",
            key="admin_username"
        )

        password = st.text_input(
            "Admin Password",
            type="password",
            key="admin_password"
        )

        if st.button(
            "Login as Admin",
            use_container_width=True,
            type="primary"
        ):

            user = execute(
                """
                SELECT * FROM users
                WHERE username=? AND role='admin'
                """,
                (username,),
                fetch=True
            )

            if user and user[0]["active"] and verify_password(
                password,
                user[0]["password"]
            ):

                st.session_state.logged_in = True
                st.session_state.user_id = user[0]["id"]
                st.session_state.role = "admin"

                st.rerun()

            else:
                st.e