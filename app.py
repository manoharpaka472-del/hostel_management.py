import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="Smart Hostel Management System",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(
            circle at 15% 20%,
            rgba(30, 120, 255, 0.25),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 20%,
            rgba(150, 60, 255, 0.25),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #07111f,
            #0b1830,
            #111936,
            #070d18
        );

    color: white;
}

/* Background grid */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;

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

    background-size: 40px 40px;

    pointer-events: none;
}

/* Main container */
.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Hero */
.hero {
    position: relative;

    padding: 55px 45px;
    margin-bottom: 30px;

    border-radius: 30px;

    background:
        radial-gradient(
            circle at 80% 20%,
            rgba(150,70,255,0.30),
            transparent 35%
        ),
        radial-gradient(
            circle at 20% 80%,
            rgba(0,190,255,0.20),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            rgba(30,55,100,0.95),
            rgba(25,20,60,0.90)
        );

    border: 1px solid rgba(255,255,255,0.15);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.45);

    overflow: hidden;
}

/* 3D building */
.hero::after {
    content: "🏢";

    position: absolute;

    right: 7%;
    top: 20px;

    font-size: 150px;

    opacity: 0.18;

    filter:
        drop-shadow(
            0 20px 20px
            rgba(0,0,0,0.6)
        );
}

/* Hero title */
.hero-title {
    font-size: clamp(36px, 5vw, 65px);

    font-weight: 800;

    line-height: 1.05;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #6bc9ff,
            #b28cff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Hero subtitle */
.hero-subtitle {
    margin-top: 18px;

    max-width: 700px;

    font-size: 18px;

    line-height: 1.7;

    color: rgba(235,245,255,0.75);
}

/* Cards */
.card {
    min-height: 170px;

    padding: 25px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.11),
            rgba(255,255,255,0.035)
        );

    border: 1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 15px 40px rgba(0,0,0,0.30);

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-8px);

    box-shadow:
        0 25px 60px rgba(0,0,0,0.45);
}

.card-icon {
    font-size: 40px;
}

.card-title {
    margin-top: 12px;

    color: rgba(255,255,255,0.65);

    font-size: 14px;

    font-weight: 600;
}

.card-value {
    margin-top: 5px;

    color: white;

    font-size: 28px;

    font-weight: 800;
}

/* Section heading */
.section-title {
    margin-top: 30px;
    margin-bottom: 20px;

    font-size: 27px;

    font-weight: 800;

    color: white;
}

.section-title span {
    color: #65c8ff;
}

/* Buttons */
.stButton > button {
    width: 100%;

    min-height: 48px;

    border-radius: 12px;

    border: 1px solid rgba(255,255,255,0.15);

    background:
        linear-gradient(
            135deg,
            #267cff,
            #7046e8
        );

    color: white;

    font-weight: 700;

    transition: 0.25s;
}

.stButton > button:hover {
    transform: translateY(-3px);

    box-shadow:
        0 12px 30px
        rgba(80,100,255,0.35);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #0a162a,
            #070d1c
        );

    border-right:
        1px solid
        rgba(255,255,255,0.10);
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Footer */
.footer {
    text-align: center;

    margin-top: 60px;

    padding: 25px;

    color: rgba(255,255,255,0.45);

    font-size: 13px;
}

/* Mobile */
@media(max-width: 768px) {

    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 35px 25px;
    }

    .hero-title {
        font-size: 38px;
    }

    .hero::after {
        font-size: 80px;
    }

    .hero-subtitle {
        font-size: 15px;
    }

}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SESSION
# ---------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "role" not in st.session_state:
    st.session_state.role = None


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <h2 style="text-align:center;">
        🏢 Smart Hostel
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Student Portal",
            "Admin Portal",
            "About"
        ]
    )

    st.session_state.page = page


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                Smart Hostel<br>
                Management System
            </div>

            <div class="hero-subtitle">
                Manage rooms, hostel fees, meals,
                complaints, maintenance, leave requests
                and hostel operations from one modern platform.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="section-title">
            Everything You Need <span>In One Place</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🏠</div>
                <div class="card-title">ROOM MANAGEMENT</div>
                <div class="card-value">Smart</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">💳</div>
                <div class="card-title">HOSTEL FEES</div>
                <div class="card-value">Easy</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🍽️</div>
                <div class="card-title">MEAL BOOKING</div>
                <div class="card-value">Free</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            """
            <div class="card">
                <div class="card-icon">🔐</div>
                <div class="card-title">SECURITY</div>
                <div class="card-value">Secure</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="section-title">
            Choose Your <span>Portal</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="card">

            <div class="card-icon">🎓</div>

            <h2>Student Portal</h2>

            <p>
            View your room, hostel fee, meals,
            complaints, maintenance, leave and
            announcements.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Open Student Portal",
            key="student_home"
        ):
            st.session_state.page = "Student Portal"
            st.rerun()

    with col2:

        st.markdown(
            """
            <div class="card">

            <div class="card-icon">👨‍💼</div>

            <h2>Admin Portal</h2>

            <p>
            Manage students, rooms, fees, payments,
            meals, complaints, maintenance and reports.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Open Admin Portal",
            key="admin_home"
        ):
            st.session_state.page = "Admin Portal"
            st.rerun()


# ---------------------------------------------------------
# STUDENT PORTAL
# ---------------------------------------------------------

elif st.session_state.page == "Student Portal":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                Student Portal 🎓
            </div>

            <div class="hero-subtitle">
                Manage your hostel life from one dashboard.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "Dashboard",
            "Hostel Fee",
            "Meals"
        ]
    )

    with tab1:

        st.markdown(
            '<div class="section-title">Student <span>Dashboard</span></div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        data = [
            ("🏠", "ROOM", "A-101"),
            ("🛏️", "BED", "Bed 1"),
            ("💰", "FEE", "₹80,000"),
            ("🔔", "NOTIFICATIONS", "3")
        ]

        for column, item in zip(
            [col1, col2, col3, col4],
            data
        ):

            with column:

                icon, title, value = item

                st.markdown(
                    f"""
                    <div class="card">

                        <div class="card-icon">
                            {icon}
                        </div>

                        <div class="card-title">
                            {title}
                        </div>

                        <div class="card-value">
                            {value}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.markdown(
            '<div class="section-title">Quick <span>Actions</span></div>',
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.button(
                "📝 Apply Leave",
                key="leave",
                use_container_width=True
            )

        with c2:
            st.button(
                "🔧 Request Maintenance",
                key="maintenance",
                use_container_width=True
            )

        with c3:
            st.button(
                "📢 View Announcements",
                key="announcement",
                use_container_width=True
            )

    with tab2:

        st.markdown(
            '<div class="section-title">Hostel <span>Fee</span></div>',
            unsafe_allow_html=True
        )

        st.info(
            "Your hostel fee includes accommodation, "
            "utilities, maintenance and mess/meal facility."
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Hostel Fee",
                "₹80,000"
            )

        with col2:
            st.metric(
                "Paid",
                "₹50,000"
            )

        with col3:
            st.metric(
                "Pending",
                "₹30,000"
            )

        st.markdown("### Make Payment")

        amount = st.number_input(
            "Payment Amount",
            min_value=1,
            max_value=30000,
            value=10000
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
            "💳 Pay Hostel Fee"
        ):

            st.success(
                f"Payment request created for ₹{amount:,} using {method}."
            )

            st.info(
                "Demo payment mode. Connect Razorpay/Stripe "
                "or another gateway for real payments."
            )

    with tab3:

        st.markdown(
            '<div class="section-title">Meal <span>Booking</span></div>',
            unsafe_allow_html=True
        )

        st.success(
            "🍽️ Meal charges are included in your hostel fee. "
            "No additional payment is required."
        )

        st.markdown("### Today's Menu")

        col1, col2, col3, col4 = st.columns(4)

        meals = [
            ("🌅", "Breakfast", "Idli + Sambar"),
            ("☀️", "Lunch", "Rice + Dal + Curry"),
            ("🍪", "Snacks", "Tea + Biscuits"),
            ("🌙", "Dinner", "Chapati + Curry")
        ]

        for column, meal in zip(
            [col1, col2, col3, col4],
            meals
        ):

            with column:

                icon, name, food = meal

                st.markdown(
                    f"""
                    <div class="card">

                        <div class="card-icon">
                            {icon}
                        </div>

                        <h3>{name}</h3>

                        <p>{food}</p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button(
                    f"Book {name}",
                    key=name
                ):
                    st.success(
                        f"{name} booked successfully!"
                    )


# ---------------------------------------------------------
# ADMIN PORTAL
# ---------------------------------------------------------

elif st.session_state.page == "Admin Portal":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                Admin Portal 👨‍💼
            </div>

            <div class="hero-subtitle">
                Control hostel operations from one dashboard.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Hostel <span>Overview</span></div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    admin_data = [
        ("🎓", "Students", "245"),
        ("🏠", "Rooms", "80"),
        ("🛏️", "Occupied Beds", "220"),
        ("💰", "Fee Collected", "₹1.65 Cr")
    ]

    for column, item in zip(
        [col1, col2, col3, col4],
        admin_data
    ):

        with column:

            icon, title, value = item

            st.markdown(
                f"""
                <div class="card">

                    <div class="card-icon">
                        {icon}
                    </div>

                    <div class="card-title">
                        {title}
                    </div>

                    <div class="card-value">
                        {value}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Management <span>Modules</span></div>',
        unsafe_allow_html=True
    )

    modules = [
        "🎓 Students",
        "🏠 Rooms",
        "🛏️ Room Allocation",
        "💰 Hostel Fees",
        "💳 Payments",
        "🍽️ Meal Management",
        "📝 Leave Requests",
        "🔧 Maintenance",
        "📢 Complaints",
        "🔄 Room Change",
        "📣 Announcements",
        "📊 Reports"
    ]

    columns = st.columns(4)

    for i, module in enumerate(modules):

        with columns[i % 4]:

            if st.button(
                module,
                key=f"module_{i}",
                use_container_width=True
            ):
                st.success(
                    f"{module} module selected."
                )

    st.markdown(
        '<div class="section-title">Occupancy <span>Overview</span></div>',
        unsafe_allow_html=True
    )

    chart_data = {
        "Hostel": [
            "Block A",
            "Block B",
            "Block C",
            "Block D"
        ],
        "Occupied": [
            58,
            50,
            55,
            57
        ],
        "Available": [
            12,
            10,
            15,
            13
        ]
    }

    import pandas as pd

    df = pd.DataFrame(chart_data)

    st.bar_chart(
        df.set_index("Hostel")
    )


# ---------------------------------------------------------
# ABOUT
# ---------------------------------------------------------

elif st.session_state.page == "About":

    st.markdown(
        """
        <div class="hero">

            <div class="hero-title">
                About The System
            </div>

            <div class="hero-subtitle">
                A modern digital platform for hostel
                administration and student services.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ### 🏢 Smart Hostel Management System

        This platform is designed to manage:

        - 🎓 Student registration
        - 🔐 Student/Admin login
        - 🏠 Hostel and room management
        - 🛏️ Bed allocation
        - 💰 Hostel fee management
        - 💳 Payment records
        - 🍽️ Meal booking
        - 📝 Leave requests
        - 📢 Complaints
        - 🔧 Maintenance
        - 🔄 Room change requests
        - 📣 Announcements
        - 🔔 Notifications
        - 📊 Reports and analytics

        **Important fee rule:**

        The hostel fee is a combined fee.

        Accommodation + utilities + maintenance +
        mess/meal facility are included.

        **Students do not pay a separate meal charge.**
        """
    )

    st.success(
        "🍽️ Meal charges are included in your hostel fee. "
        "No additional payment is required."
    )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Smart Hostel Management System © 2026
        <br>
        Modern • Secure • Student Friendly
    </div>
    """,
    unsafe_allow_html=True
)
