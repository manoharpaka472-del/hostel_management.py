import streamlit as st
import sqlite3
import hashlib

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Smart Hostel Management",
    page_icon="🏠",
    layout="wide"
)

# =========================
# DATABASE
# =========================

conn = sqlite3.connect(
    "hostel.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    student_id TEXT,
    phone TEXT,
    branch TEXT,
    year TEXT,
    hostel TEXT,
    block TEXT,
    room TEXT,
    bed TEXT,
    fee REAL
)
""")

conn.commit()


# =========================
# PASSWORD FUNCTION
# =========================

def make_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


# =========================
# CREATE DEMO ACCOUNTS
# =========================

cursor.execute(
    "SELECT * FROM users WHERE username=?",
    ("admin",)
)

if cursor.fetchone() is None:

    cursor.execute("""
    INSERT INTO users
    (username, password, role, name)
    VALUES (?, ?, ?, ?)
    """, (
        "admin",
        make_password("admin123"),
        "admin",
        "Hostel Administrator"
    ))


cursor.execute(
    "SELECT * FROM users WHERE username=?",
    ("student",)
)

if cursor.fetchone() is None:

    cursor.execute("""
    INSERT INTO users
    (username, password, role, name)
    VALUES (?, ?, ?, ?)
    """, (
        "student",
        make_password("student123"),
        "student",
        "Rahul Kumar"
    ))

    cursor.execute("""
    INSERT INTO students
    (
        username,
        student_id,
        phone,
        branch,
        year,
        hostel,
        block,
        room,
        bed,
        fee
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "student",
        "STU001",
        "9876543210",
        "Mechanical Engineering",
        "2nd Year",
        "ABC College Boys Hostel",
        "Block A",
        "A101",
        "Bed 1",
        80000
    ))

conn.commit()


# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {

    background:
        radial-gradient(
            circle at 10% 10%,
            #164e8a,
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 20%,
            #512b82,
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #07111f,
            #101b38
        );

}

.main-title {

    font-size: 48px;
    font-weight: 800;
    color: white;

}

.subtitle {

    font-size: 18px;
    color: #b8c7df;

}

.card {

    background: rgba(255,255,255,0.08);

    border: 1px solid rgba(255,255,255,0.15);

    border-radius: 20px;

    padding: 25px;

    margin-bottom: 20px;

}

.card h2 {

    color: white;

}

.card p {

    color: #cbd5e1;

}

</style>
""", unsafe_allow_html=True)


# =========================
# SESSION
# =========================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "role" not in st.session_state:

    st.session_state.role = ""

if "username" not in st.session_state:

    st.session_state.username = ""


# =========================
# LOGIN PAGE
# =========================

def login_page():

    st.markdown(
        '<div class="main-title">'
        '🏠 Smart Hostel Management System'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Modern Hostel Management Platform'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    login_type = st.selectbox(
        "Login As",
        [
            "Student",
            "Admin"
        ]
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
        use_container_width=True
    ):

        user = cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=?
            """,
            (username,)
        ).fetchone()

        if user is None:

            st.error(
                "Username not found."
            )

            return

        stored_password = user[2]
        role = user[3]

        if make_password(password) != stored_password:

            st.error(
                "Incorrect password."
            )

            return

        if login_type == "Admin" and role != "admin":

            st.error(
                "This account is not an admin account."
            )

            return

        if login_type == "Student" and role != "student":

            st.error(
                "This account is not a student account."
            )

            return

        st.session_state.logged_in = True
        st.session_state.role = role
        st.session_state.username = username

        st.rerun()

    st.divider()

    st.info(
        "Demo Admin: admin / admin123"
    )

    st.info(
        "Demo Student: student / student123"
    )


# =========================
# STUDENT DASHBOARD
# =========================

def student_dashboard():

    student = cursor.execute(
        """
        SELECT *
        FROM students
        WHERE username=?
        """,
        (st.session_state.username,)
    ).fetchone()

    if student is None:

        st.error(
            "Student information not found."
        )

        return

    st.title(
        "🎓 Student Dashboard"
    )

    st.write(
        "Welcome,",
        student[1]
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏠 Room",
            student[7]
        )

    with col2:

        st.metric(
            "🛏️ Bed",
            student[8]
        )

    with col3:

        st.metric(
            "💰 Hostel Fee",
            "₹80,000"
        )

    with col4:

        st.metric(
            "📚 Year",
            student[5]
        )

    st.divider()

    tab1, tab2, tab3 = st.tabs(
        [
            "👤 Profile",
            "🏠 Room Details",
            "🍽️ Meals"
        ]
    )

    with tab1:

        st.subheader(
            "My Profile"
        )

        st.write(
            "**Student ID:**",
            student[2]
        )

        st.write(
            "**Phone:**",
            student[3]
        )

        st.write(
            "**Branch:**",
            student[4]
        )

        st.write(
            "**Year:**",
            student[5]
        )

    with tab2:

        st.subheader(
            "Room Details"
        )

        st.write(
            "**Hostel:**",
            student[6]
        )

        st.write(
            "**Block:**",
            student[7]
        )

        st.write(
            "**Room:**",
            student[7]
        )

        st.write(
            "**Bed:**",
            student[8]
        )

    with tab3:

        st.subheader(
            "Today's Meals"
        )

        st.success(
            "🍽️ Meal charges are included "
            "in your hostel fee. "
            "No additional payment is required."
        )

        meals = [
            ("🌅 Breakfast", "Idli + Sambar"),
            ("☀️ Lunch", "Rice + Dal + Curry"),
            ("🍪 Snacks", "Tea + Biscuits"),
            ("🌙 Dinner", "Chapati + Curry")
        ]

        for meal_name, food in meals:

            with st.container(border=True):

                st.write(
                    f"### {meal_name}"
                )

                st.write(food)

                if st.button(
                    "Book Meal",
                    key=meal_name
                ):

                    st.success(
                        "Meal booked successfully."
                    )


# =========================
# ADMIN DASHBOARD
# =========================

def admin_dashboard():

    st.title(
        "👨‍💼 Admin Dashboard"
    )

    st.write(
        "Hostel Administrator Control Panel"
    )

    students = cursor.execute(
        "SELECT * FROM students"
    ).fetchall()

    rooms = [
        "A101",
        "A102",
        "A103",
        "B201",
        "B202"
    ]

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🎓 Students",
            len(students)
        )

    with col2:

        st.metric(
            "🏠 Rooms",
            len(rooms)
        )

    with col3:

        st.metric(
            "🛏️ Beds",
            20
        )

    with col4:

        st.metric(
            "💰 Hostel Fee",
            "₹80,000"
        )

    st.divider()

    menu = st.selectbox(
        "Admin Management",
        [
            "Students",
            "Rooms",
            "Hostel Fees",
            "Meal Management"
        ]
    )

    # =========================
    # STUDENT EDIT
    # =========================

    if menu == "Students":

        st.header(
            "🎓 Student Management"
        )

        df = pd.DataFrame(
            students,
            columns=[
                "ID",
                "Username",
                "Student ID",
                "Phone",
                "Branch",
                "Year",
                "Hostel",
                "Block",
                "Room",
                "Bed",
                "Fee"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "✏️ Edit Student"
        )

        student_ids = [
            x[2]
            for x in students
        ]

        selected_id = st.selectbox(
            "Select Student",
            student_ids
        )

        selected = cursor.execute(
            """
            SELECT *
            FROM students
            WHERE student_id=?
            """,
            (selected_id,)
        ).fetchone()

        if selected:

            with st.form(
                "edit_student"
            ):

                name = st.text_input(
                    "Username",
                    value=selected[1]
                )

                phone = st.text_input(
                    "Phone",
                    value=selected[3]
                )

                branch = st.text_input(
                    "Branch",
                    value=selected[4]
                )

                year = st.text_input(
                    "Year",
                    value=selected[5]
                )

                hostel = st.text_input(
                    "Hostel",
                    value=selected[6]
                )

                block = st.text_input(
                    "Block",
                    value=selected[7]
                )

                room = st.text_input(
                    "Room",
                    value=selected[8]
                )

                bed = st.text_input(
                    "Bed",
                    value=selected[9]
                )

                fee = st.number_input(
                    "Hostel Fee",
                    min_value=0.0,
                    value=float(selected[10])
                )

                save = st.form_submit_button(
                    "💾 Save Changes",
                    use_container_width=True
                )

                if save:

                    cursor.execute(
                        """
                        UPDATE students
                        SET
                            username=?,
                            phone=?,
                            branch=?,
                            year=?,
                            hostel=?,
                            block=?,
                            room=?,
                            bed=?,
                            fee=?
                        WHERE student_id=?
                        """,
                        (
                            name,
                            phone,
                            branch,
                            year,
                            hostel,
                            block,
                            room,
                            bed,
                            fee,
                            selected_id
                        )
                    )

                    conn.commit()

                    st.success(
                        "Student details updated successfully."
                    )

                    st.rerun()

    # =========================
    # ROOMS
    # =========================

    elif menu == "Rooms":

        st.header(
            "🏠 Room Management"
        )

        room_data = pd.DataFrame({
            "Room": [
                "A101",
                "A102",
                "A103",
                "B201",
                "B202"
            ],
            "Block": [
                "A",
                "A",
                "A",
                "B",
                "B"
            ],
            "Type": [
                "Double",
                "Double",
                "Triple",
                "Four Sharing",
                "Four Sharing"
            ],
            "Beds": [
                2,
                2,
                3,
                4,
                4
            ],
            "Status": [
                "Occupied",
                "Available",
                "Available",
                "Available",
                "Available"
            ]
        })

        st.dataframe(
            room_data,
            use_container_width=True
        )

        st.subheader(
            "Edit Room"
        )

        room = st.selectbox(
            "Select Room",
            room_data["Room"]
        )

        new_status = st.selectbox(
            "Room Status",
            [
                "Available",
                "Occupied",
                "Maintenance",
                "Closed"
            ]
        )

        if st.button(
            "💾 Update Room"
        ):

            st.success(
                f"{room} updated to {new_status}."
            )

    # =========================
    # FEES
    # =========================

    elif menu == "Hostel Fees":

        st.header(
            "💰 Hostel Fee Management"
        )

        st.info(
            "The hostel fee is a combined fee. "
            "Meal charges are included."
        )

        total_fee = st.number_input(
            "Annual Hostel Fee",
            min_value=0,
            value=80000
        )

        if st.button(
            "💾 Save Fee Structure"
        ):

            st.success(
                f"Hostel fee updated to ₹{total_fee:,}"
            )

    # =========================
    # MEALS
    # =========================

    elif menu == "Meal Management":

        st.header(
            "🍽️ Meal Management"
        )

        st.success(
            "Meal charges are included in the hostel fee."
        )

        breakfast = st.text_input(
            "Breakfast",
            "Idli + Sambar"
        )

        lunch = st.text_input(
            "Lunch",
            "Rice + Dal + Curry"
        )

        snacks = st.text_input(
            "Snacks",
            "Tea + Biscuits"
        )

        dinner = st.text_input(
            "Dinner",
            "Chapati + Curry"
        )

        if st.button(
            "💾 Save Meal Menu"
        ):

            st.success(
                "Meal menu updated successfully."
            )


# =========================
# APPLICATION
# =========================

if not st.session_state.logged_in:

    login_page()

else:

    with st.sidebar:

        st.title(
            "🏢 Smart Hostel"
        )

        st.write(
            f"Logged in as: "
            f"**{st.session_state.username}**"
        )

        st.divider()

        if st.session_state.role == "admin":

            st.success(
                "👨‍💼 ADMIN"
            )

        else:

            st.success(
                "🎓 STUDENT"
            )

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False
            st.session_state.role = ""
            st.session_state.username = ""

            st.rerun()

    if st.session_state.role == "admin":

        admin_dashboard()

    else:

        student_dashboard()
