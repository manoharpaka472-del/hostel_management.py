import streamlit as st

st.set_page_config(
    page_title="Smart Hostel Management",
    page_icon="🏠",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 10% 10%,
            #173d70 0%,
            transparent 35%
        ),
        radial-gradient(
            circle at 90% 10%,
            #482060 0%,
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #07111f,
            #101a32,
            #080d18
        );

    color: white;
}

.hero {
    padding: 50px;
    border-radius: 30px;
    background: linear-gradient(
        135deg,
        rgba(0, 120, 255, 0.25),
        rgba(150, 50, 255, 0.25)
    );
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 45px;
    font-weight: 800;
}

.hero p {
    font-size: 19px;
    color: #cbd5e1;
}

.card {
    padding: 25px;
    border-radius: 22px;
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow: 0 15px 40px rgba(0,0,0,0.25);
}

.big {
    font-size: 35px;
    font-weight: bold;
    color: #4fc3ff;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION ----------------

if "login" not in st.session_state:
    st.session_state.login = False

if "role" not in st.session_state:
    st.session_state.role = ""


# ---------------- LOGIN ----------------

if not st.session_state.login:

    st.markdown("""
    <div class="hero">

        <h1>🏠 Smart Hostel Management System</h1>

        <p>
        Manage rooms, hostel fees, meals, complaints,
        leave requests and hostel operations.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("🔐 Login")

    login_type = st.radio(
        "Select Login",
        ["Student", "Admin"],
        horizontal=True
    )

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button(
        "LOGIN",
        type="primary",
        use_container_width=True
    ):

        # ADMIN
        if (
            login_type == "Admin"
            and username == "admin"
            and password == "admin123"
        ):

            st.session_state.login = True
            st.session_state.role = "admin"
            st.rerun()

        # STUDENT
        elif (
            login_type == "Student"
            and username == "student"
            and password == "student123"
        ):

            st.session_state.login = True
            st.session_state.role = "student"
            st.rerun()

        else:

            st.error(
                "Invalid username or password."
            )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.info("""
        **Student Demo Login**

        Username: `student`

        Password: `student123`
        """)

    with col2:

        st.warning("""
        **Admin Demo Login**

        Username: `admin`

        Password: `admin123`
        """)


# =====================================================
# STUDENT
# =====================================================

elif st.session_state.role == "student":

    with st.sidebar:

        st.title("🏠 Hostel")

        st.success("🎓 Student")

        menu = st.radio(
            "Menu",
            [
                "Dashboard",
                "My Profile",
                "Room",
                "Hostel Fee",
                "Meals",
                "Complaints",
                "Leave",
                "Announcements"
            ]
        )

        st.divider()

        if st.button(
            "Logout",
            use_container_width=True
        ):

            st.session_state.login = False
            st.session_state.role = ""
            st.rerun()


    # DASHBOARD

    if menu == "Dashboard":

        st.markdown("""
        <div class="hero">

            <h1>🎓 Student Dashboard</h1>

            <p>
            Welcome back, Rahul Kumar
            </p>

        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.markdown("""
            <div class="card">
            <h3>🏠 ROOM</h3>
            <div class="big">A101</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card">
            <h3>🛏️ BED</h3>
            <div class="big">01</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="card">
            <h3>💰 PENDING</h3>
            <div class="big">₹50,000</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown("""
            <div class="card">
            <h3>📚 YEAR</h3>
            <div class="big">2nd</div>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        c1, c2 = st.columns(2)

        with c1:

            st.markdown("""
            <div class="card">

            <h2>🏠 Room Information</h2>

            <p>Hostel: ABC College Boys Hostel</p>

            <p>Block: A</p>

            <p>Floor: 1</p>

            <p>Room: A101</p>

            <p>Bed: Bed 1</p>

            </div>
            """, unsafe_allow_html=True)

        with c2:

            st.markdown("""
            <div class="card">

            <h2>💰 Fee Information</h2>

            <p>Total Hostel Fee: ₹80,000</p>

            <p>Paid: ₹30,000</p>

            <p>Pending: ₹50,000</p>

            </div>
            """, unsafe_allow_html=True)

        st.success(
            "🍽️ Meal charges are included in your hostel fee. "
            "No additional payment is required."
        )


    # PROFILE

    elif menu == "My Profile":

        st.title("👤 My Profile")

        name = st.text_input(
            "Name",
            "Rahul Kumar"
        )

        student_id = st.text_input(
            "Student ID",
            "STU001"
        )

        phone = st.text_input(
            "Phone",
            "9876543210"
        )

        email = st.text_input(
            "Email",
            "student@example.com"
        )

        branch = st.text_input(
            "Branch",
            "Mechanical Engineering"
        )

        year = st.selectbox(
            "Year",
            [
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ],
            index=1
        )

        if st.button(
            "💾 Save Profile",
            type="primary"
        ):

            st.success(
                "Profile updated successfully!"
            )


    # ROOM

    elif menu == "Room":

        st.title("🏠 Room Details")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Hostel",
            "ABC College"
        )

        c2.metric(
            "Block",
            "A"
        )

        c3.metric(
            "Room",
            "A101"
        )

        st.subheader("🛏️ Bed Occupancy")

        st.success("Bed 1 — You")

        st.info("Bed 2 — Available")


    # FEE

    elif menu == "Hostel Fee":

        st.title("💰 Hostel Fee")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Total",
            "₹80,000"
        )

        c2.metric(
            "Paid",
            "₹30,000"
        )

        c3.metric(
            "Pending",
            "₹50,000"
        )

        st.success(
            "🍽️ Meal charges are included in the hostel fee."
        )

        amount = st.number_input(
            "Payment Amount",
            min_value=1,
            max_value=50000,
            value=1000
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
            "💳 Pay Now",
            type="primary"
        ):

            st.success(
                "Payment successful!"
            )

            st.write(
                "Transaction ID: TXN202610070001"
            )

            st.write(
                f"Amount: ₹{amount}"
            )

            st.write(
                f"Method: {method}"
            )


    # MEALS

    elif menu == "Meals":

        st.title("🍽️ Meal / Mess")

        st.success(
            "Meal charges are included in your hostel fee. "
            "No additional payment is required."
        )

        meals = {
            "🌅 Breakfast":
                "Idli, Sambar, Chutney",

            "☀️ Lunch":
                "Rice, Dal, Vegetable Curry",

            "🍪 Snacks":
                "Tea and Biscuits",

            "🌙 Dinner":
                "Chapati, Paneer Curry"
        }

        for meal, food in meals.items():

            with st.container(border=True):

                st.subheader(meal)

                st.write(food)

                if st.button(
                    "Book",
                    key=meal
                ):

                    st.success(
                        "Meal booked successfully!"
                    )


    # COMPLAINTS

    elif menu == "Complaints":

        st.title("🛠️ Raise Complaint")

        category = st.selectbox(
            "Category",
            [
                "Room",
                "Food",
                "Electricity",
                "Water",
                "WiFi",
                "Cleaning",
                "Security",
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

        if st.button(
            "Submit Complaint",
            type="primary"
        ):

            st.success(
                "Complaint submitted successfully!"
            )


    # LEAVE

    elif menu == "Leave":

        st.title("📝 Leave Request")

        start = st.date_input(
            "Start Date"
        )

        end = st.date_input(
            "End Date"
        )

        reason = st.text_area(
            "Reason"
        )

        destination = st.text_input(
            "Destination"
        )

        if st.button(
            "Apply Leave",
            type="primary"
        ):

            st.success(
                "Leave request submitted!"
            )


    # ANNOUNCEMENTS

    elif menu == "Announcements":

        st.title("📢 Announcements")

        st.info(
            "Hostel maintenance will be carried out "
            "this Sunday from 10 AM to 2 PM."
        )

        st.warning(
            "Hostel fee payment deadline is approaching."
        )


# =====================================================
# ADMIN
# =====================================================

else:

    with st.sidebar:

        st.title("🏢 Hostel Admin")

        st.success("👨‍💼 Administrator")

        menu = st.radio(
            "Admin Menu",
            [
                "Dashboard",
                "Students",
                "Rooms",
                "Fees",
                "Meals",
                "Complaints",
                "Leave",
                "Announcements"
            ]
        )

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.login = False
            st.session_state.role = ""

            st.rerun()


    # ADMIN DASHBOARD

    if menu == "Dashboard":

        st.markdown("""
        <div class="hero">

            <h1>👨‍💼 Admin Dashboard</h1>

            <p>
            Complete hostel control center
            </p>

        </div>
        """, unsafe_allow_html=True)

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "Students",
            "125"
        )

        c2.metric(
            "Rooms",
            "60"
        )

        c3.metric(
            "Occupied Beds",
            "108"
        )

        c4.metric(
            "Pending Fees",
            "₹12.5 L"
        )

        st.divider()

        st.subheader(
            "📊 Hostel Overview"
        )

        st.bar_chart({
            "Occupied": [108],
            "Available": [12]
        })


    # STUDENTS

    elif menu == "Students":

        st.title("🎓 Student Management")

        st.subheader(
            "Student List"
        )

        st.dataframe(
            [
                {
                    "Student ID": "STU001",
                    "Name": "Rahul Kumar",
                    "Branch": "Mechanical Engineering",
                    "Year": "2nd Year",
                    "Room": "A101",
                    "Bed": "Bed 1"
                },
                {
                    "Student ID": "STU002",
                    "Name": "Arjun Reddy",
                    "Branch": "CSE",
                    "Year": "2nd Year",
                    "Room": "A102",
                    "Bed": "Bed 1"
                }
            ],
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "✏️ Edit Student"
        )

        student = st.selectbox(
            "Select Student",
            [
                "STU001 - Rahul Kumar",
                "STU002 - Arjun Reddy"
            ]
        )

        name = st.text_input(
            "Student Name",
            "Rahul Kumar"
        )

        room = st.text_input(
            "Room",
            "A101"
        )

        bed = st.text_input(
            "Bed",
            "Bed 1"
        )

        fee = st.number_input(
            "Hostel Fee",
            value=80000
        )

        if st.button(
            "💾 Update Student",
            type="primary"
        ):

            st.success(
                f"{student} updated successfully!"
            )


    # ROOMS

    elif menu == "Rooms":

        st.title("🏠 Room Management")

        rooms = [
            ["A101", "A", "1", "Double", 2, "1 Occupied"],
            ["A102", "A", "1", "Double", 2, "0 Occupied"],
            ["A103", "A", "1", "Triple", 3, "1 Occupied"],
            ["B201", "B", "2", "Four Sharing", 4, "2 Occupied"]
        ]

        st.dataframe(
            rooms,
            column_config={
                "Room": "Room"
            },
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "✏️ Edit Room"
        )

        room = st.selectbox(
            "Room",
            [
                "A101",
                "A102",
                "A103",
                "B201"
            ]
        )

        room_type = st.selectbox(
            "Room Type",
            [
                "Single",
                "Double",
                "Triple",
                "Four Sharing"
            ]
        )

        beds = st.number_input(
            "Total Beds",
            1,
            10,
            2
        )

        status = st.selectbox(
            "Status",
            [
                "Available",
                "Occupied",
                "Maintenance"
            ]
        )

        if st.button(
            "💾 Save Room",
            type="primary"
        ):

            st.success(
                f"Room {room} updated successfully!"
            )

        st.divider()

        st.subheader(
            "➕ Add New Room"
        )

        new_room = st.text_input(
            "New Room Number"
        )

        if st.button(
            "Add Room"
        ):

            if new_room:

                st.success(
                    f"Room {new_room} added!"
                )

            else:

                st.error(
                    "Enter room number."
                )


    # FEES

    elif menu == "Fees":

        st.title("💰 Hostel Fee Management")

        st.info(
            "Hostel fee is a single combined fee. "
            "Meal charges must NOT be charged separately."
        )

        st.dataframe(
            [
                {
                    "Student": "STU001",
                    "Total": "₹80,000",
                    "Paid": "₹30,000",
                    "Pending": "₹50,000",
                    "Status": "Partially Paid"
                },
                {
                    "Student": "STU002",
                    "Total": "₹80,000",
                    "Paid": "₹80,000",
                    "Pending": "₹0",
                    "Status": "Paid"
                }
            ],
            use_container_width=True
        )


    # MEALS

    elif menu == "Meals":

        st.title("🍽️ Meal Management")

        st.success(
            "Meals are included in hostel fee."
        )

        st.subheader(
            "Edit Today's Menu"
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
            "💾 Save Menu",
            type="primary"
        ):

            st.success(
                "Meal menu updated!"
            )


    # COMPLAINTS

    elif menu == "Complaints":

        st.title("🛠️ Complaint Management")

        st.dataframe(
            [
                {
                    "ID": "C001",
                    "Student": "STU001",
                    "Category": "Room",
                    "Priority": "High",
                    "Status": "Submitted"
                },
                {
                    "ID": "C002",
                    "Student": "STU002",
                    "Category": "WiFi",
                    "Priority": "Medium",
                    "Status": "In Progress"
                }
            ],
            use_container_width=True
        )

        st.subheader(
            "Update Complaint"
        )

        complaint_status = st.selectbox(
            "Status",
            [
                "Submitted",
                "In Progress",
                "Resolved",
                "Closed"
            ]
        )

        if st.button(
            "Update Status"
        ):

            st.success(
                "Complaint updated!"
            )


    # LEAVE

    elif menu == "Leave":

        st.title("📝 Leave Management")

        st.dataframe(
            [
                {
                    "Student": "STU001",
                    "Start": "10-10-2026",
                    "End": "12-10-2026",
                    "Status": "Pending"
                }
            ],
            use_container_width=True
        )

        decision = st.selectbox(
            "Decision",
            [
                "Pending",
                "Approved",
                "Rejected"
            ]
        )

        if st.button(
            "Save Decision"
        ):

            st.success(
                f"Leave request {decision.lower()}."
            )


    # ANNOUNCEMENTS

    elif menu == "Announcements":

        st.title("📢 Announcement Management")

        title = st.text_input(
            "Announcement Title"
        )

        message = st.text_area(
            "Message"
        )

        priority = st.selectbox(
            "Priority",
            [
                "Normal",
                "Important",
                "Urgent"
            ]
        )

        if st.button(
            "📢
