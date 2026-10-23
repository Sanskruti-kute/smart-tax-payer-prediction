import streamlit as st
import pandas as pd
import joblib

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Smart Tax Prediction System",
    page_icon="💼",
    layout="wide"
)

# =================================================
# DATASET
# =================================================

data = {
    "Age": [25, 35, 42, 28, 50, 30, 45, 38],
    "Income": [250000, 600000, 900000, 300000, 1200000, 450000, 800000, 700000],
    "Employment": [
        "Private", "Private", "Business", "Student",
        "Business", "Private", "Business", "Private"
    ],
    "Property": [
        "No", "Yes", "Yes", "No",
        "Yes", "No", "Yes", "Yes"
    ],
    "Previous_Tax_Filing": [
        "No", "Yes", "Yes", "No",
        "Yes", "Yes", "Yes", "Yes"
    ],
    "Tax_Status": [
        "Low", "Likely", "Likely", "Low",
        "Likely", "Low", "Likely", "Likely"
    ]
}

df = pd.DataFrame(data)

# =================================================
# LOAD MODEL
# =================================================

model = joblib.load("tax_model.pkl")
# PROFESSIONAL OPENING SCREEN

if "started" not in st.session_state:
    st.session_state.started = False

if not st.session_state.started:

    st.markdown(
        "<h1 style='text-align:center;'>💼</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align:center; color:#2563eb;'>SMART TAX PREDICTION</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center; font-size:20px; color:#64748b;'>"
        "Data Science & Machine Learning"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.info(
            "🤖 Intelligent Tax Status Prediction System\n\n"
            "Predict tax status using Machine Learning "
            "and taxpayer information."
        )

        st.write("")

        if st.button(
            "🚀  GET STARTED",
            use_container_width=True
        ):

            st.session_state.started = True
            st.rerun()

    st.write("")
    st.caption(
        "Python • Machine Learning • Streamlit"
    )

    st.stop()

# =================================================
# SESSION STATE
# =================================================

if "user_completed" not in st.session_state:
    st.session_state.user_completed = False

# =================================================
# PROFESSIONAL CSS
# =================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb !important;
}

.hero {
    background: linear-gradient(135deg, #0f172a, #2563eb) !important;
    padding: 50px 35px;
    border-radius: 22px;
    text-align: center;
    color: white !important;
    margin-bottom: 30px;
}

.hero h1 {
    color: white !important;
    font-size: 42px !important;
}

.hero p {
    color: white !important;
    font-size: 18px !important;
}

.section {
    background-color: white !important;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
}

.section h2,
.section h3,
.section p {
    color: #111827 !important;
}

label {
    color: #111827 !important;
    font-weight: 600 !important;
}

input {
    color: #111827 !important;
    background-color: white !important;
}

.stApp {
    background: #f5f7fb;
}

/* Input labels and text */
label,
.stTextInput label,
.stNumberInput label,
.stSelectbox label {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Input text */
input,
textarea {
    color: #111827 !important;
    background-color: #ffffff !important;
}

/* Selectbox text */
div[data-baseweb="select"] * {
    color: #111827 !important;
}

/* Input boxes */
div[data-baseweb="input"] {
    background-color: #ffffff !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #ffffff !important;
}
/* Main title */
.hero {
    background: linear-gradient(135deg, #0f172a, #2563eb);
    padding: 45px 35px;
    border-radius: 22px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.18);
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    color: #dbeafe;
}

/* Cards */
.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    text-align: center;
    box-shadow: 0 5px 18px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.card h2 {
    color: #2563eb;
    font-size: 30px;
    margin-bottom: 5px;
}

.card p {
    color: #64748b;
    font-size: 15px;
}

/* Section */
.section {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e5e7eb;
    margin-bottom: 25px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    padding: 30px;
    margin-top: 30px;
}
/* Fix text visibility */

.stApp,
.stApp p,
.stApp label,
.stApp span,
.stApp div {
    color: #111827;
}

h1, h2, h3, h4, h5, h6 {
    color: #111827 !important;
}

/* Keep hero text white */
.hero,
.hero h1,
.hero p {
    color: white !important;
}

/* Keep info boxes readable */
[data-testid="stAlert"] p,
[data-testid="stAlert"] span {
    color: #111827 !important;
}
/* FIX CONTINUE BUTTON */

.stButton > button {
    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 18px !important;
    font-weight: 600 !important;
    padding: 12px !important;
}

.stButton > button p {
    color: white !important;
}

.stButton > button:hover {
    background-color: #1d4ed8 !important;
    color: white !important;
}

/* SIDEBAR VISIBILITY FIX */

[data-testid="stSidebar"] {
    background-color: #ffffff !important;
}

[data-testid="stSidebar"] * {
    color: #111827 !important;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label {
    color: #111827 !important;
}

/* Navigation radio buttons */
[data-testid="stSidebar"] [role="radiogroup"] label {
    color: #111827 !important;
    font-weight: 600 !important;
}

/* Selected navigation item */
[data-testid="stSidebar"] [role="radiogroup"] label[data-checked="true"] {
    color: #2563eb !important;
}

</style>
""", unsafe_allow_html=True)

 # =================================================
# FIRST SCREEN - USER INFORMATION
# =================================================

if not st.session_state.user_completed:

    st.markdown("""
    <div class="hero">
        <h1>💼 Smart Tax Prediction System</h1>
        <p>Machine Learning Based Tax Status Prediction & Data Analysis</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
        <h2>👋 Welcome!</h2>
        <p>
        Welcome to the Smart Tax Prediction System.
        Please enter your basic information to continue to the dashboard.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("👤 User Information")

    col1, col2 = st.columns(2)

    with col1:

        user_name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        user_age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=18
        )

    with col2:

        user_email = st.text_input(
            "Email Address",
            placeholder="Enter your email"
        )

        user_city = st.text_input(
            "City",
            placeholder="Enter your city"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "🚀 Continue to Dashboard",
        use_container_width=True
    ):

        if user_name.strip() == "":
            st.warning("⚠️ Please enter your name.")

        elif user_email.strip() == "":
            st.warning("⚠️ Please enter your email address.")

        elif user_city.strip() == "":
            st.warning("⚠️ Please enter your city.")

        else:

            st.session_state.user_completed = True
            st.session_state.user_name = user_name
            st.session_state.user_age = user_age
            st.session_state.user_email = user_email
            st.session_state.user_city = user_city

            st.success("✅ Information saved successfully!")

            st.rerun()

    st.stop()       
# =================================================
# MAIN APPLICATION
# =================================================

else:

    # -------------------------------------------------
    # SIDEBAR
    # -------------------------------------------------

    st.sidebar.markdown("## 💼 Smart Tax Prediction")

    st.sidebar.write(
        f"Welcome, **{st.session_state.user_name}** 👋"
    )

    st.sidebar.write("---")

    page = st.sidebar.radio(
        "Navigation",
        [
            "📊 Dashboard",
            "🔮 Tax Prediction",
            "📘 About Project"
        ]
    )

    st.sidebar.write("---")

    if st.sidebar.button("🔄 Change User"):

        st.session_state.user_completed = False
        st.rerun()

    # =================================================
    # DASHBOARD
    # =================================================

    if page == "📊 Dashboard":

        st.markdown("""
        <div class="hero">
            <h1>📊 Dashboard</h1>
            <p>Smart Tax Prediction System Overview</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader(
            f"Welcome back, {st.session_state.user_name} 👋"
        )

        st.write(
            "Explore taxpayer data, analytics and machine learning performance."
        )

        # Dashboard cards

        total_taxpayers = len(df)
        average_income = df["Income"].mean()
        likely_count = (df["Tax_Status"] == "Likely").sum()

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="card">
                <h2>{total_taxpayers}</h2>
                <p>👥 Total Taxpayers</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="card">
                <h2>₹{average_income:,.0f}</h2>
                <p>💰 Average Income</p>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="card">
                <h2>{likely_count}</h2>
                <p>⚠️ Likely Tax Status</p>
            </div>
            """, unsafe_allow_html=True)

        # Analytics

        st.subheader("📈 Data Analysis")

        chart1, chart2 = st.columns(2)

        with chart1:

            st.markdown(
                '<div class="section"><h3>💰 Income Distribution</h3>',
                unsafe_allow_html=True
            )

            st.bar_chart(
                df.set_index("Age")["Income"]
            )

            st.markdown("</div>", unsafe_allow_html=True)

        with chart2:

            st.markdown(
                '<div class="section"><h3>👥 Tax Status Distribution</h3>',
                unsafe_allow_html=True
            )

            status_count = df["Tax_Status"].value_counts()

            st.bar_chart(status_count)

            st.markdown("</div>", unsafe_allow_html=True)

        chart3, chart4 = st.columns(2)

        with chart3:

            st.markdown(
                '<div class="section"><h3>💼 Employment Analysis</h3>',
                unsafe_allow_html=True
            )

            employment_count = df["Employment"].value_counts()

            st.bar_chart(employment_count)

            st.markdown("</div>", unsafe_allow_html=True)

        with chart4:

            st.markdown(
                '<div class="section"><h3>🏠 Property Ownership</h3>',
                unsafe_allow_html=True
            )

            property_count = df["Property"].value_counts()

            st.bar_chart(property_count)

            st.markdown("</div>", unsafe_allow_html=True)

        # Model Performance

        st.subheader("🎯 Model Performance")

        p1, p2 = st.columns(2)

        with p1:

            st.metric(
                "Model Accuracy",
                "100.0%"
            )

        with p2:

            st.info(
                "Test Samples: 2\n\n"
                "Both test predictions were correct."
            )

        # Confusion Matrix

        st.subheader("📊 Confusion Matrix")

        cm = [[1, 0],
              [0, 1]]

        st.dataframe(
            pd.DataFrame(
                cm,
                index=["Likely", "Low"],
                columns=["Likely", "Low"]
            ),
            use_container_width=True
        )

        st.caption(
            "Note: Accuracy is based on a very small test set of 2 samples."
        )

    # =================================================
    # TAX PREDICTION
    # =================================================

    elif page == "🔮 Tax Prediction":

        st.markdown("""
        <div class="hero">
            <h1>🔮 Tax Status Prediction</h1>
            <p>Enter taxpayer details to predict tax status</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("📋 Taxpayer Details")

        left, right = st.columns(2)

        with left:

            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=25
            )

            income = st.number_input(
                "Annual Income (₹)",
                min_value=0,
                value=500000,
                step=10000
            )

            employment = st.selectbox(
                "Employment Type",
                ["Private", "Business", "Student"]
            )

        with right:

            property_status = st.selectbox(
                "Property Ownership",
                ["No", "Yes"]
            )

            previous_tax = st.selectbox(
                "Previous Tax Filing",
                ["No", "Yes"]
            )

        employment_map = {
            "Business": 0,
            "Private": 1,
            "Student": 2
        }

        property_map = {
            "No": 0,
            "Yes": 1
        }

        tax_map = {
            "No": 0,
            "Yes": 1
        }

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🔍 Predict Tax Status",
            use_container_width=True
        ):

            input_data = pd.DataFrame(
                [[
                    age,
                    income,
                    employment_map[employment],
                    property_map[property_status],
                    tax_map[previous_tax]
                ]],
                columns=[
                    "Age",
                    "Income",
                    "Employment",
                    "Property",
                    "Previous_Tax_Filing"
                ]
            )

            prediction = model.predict(input_data)

            st.markdown("<br>", unsafe_allow_html=True)

            if prediction[0] == 1:

                st.success(
                    "✅ Prediction Result: TAX STATUS IS LOW"
                )

            else:

                st.warning(
                    "⚠️ Prediction Result: TAX STATUS IS LIKELY"
                )

    # =================================================
    # ABOUT PROJECT
    # =================================================

    elif page == "📘 About Project":

        st.markdown("""
        <div class="hero">
            <h1>📘 About Project</h1>
            <p>Data Science & Machine Learning Application</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("🎯 Project Objective")

        st.write(
            "The Smart Tax Prediction System is a Machine Learning "
            "based web application developed to predict a taxpayer's "
            "tax status using basic personal and financial information."
        )

        st.subheader("🧠 Machine Learning Model")

        st.write(
            "The project uses a Decision Tree Classifier to predict "
            "the tax status of a taxpayer."
        )

        st.subheader("📋 Input Features")

        features = [
            "Age",
            "Annual Income",
            "Employment Type",
            "Property Ownership",
            "Previous Tax Filing"
        ]

        for feature in features:
            st.write("• " + feature)

        st.subheader("🛠️ Technologies Used")

        a1, a2, a3 = st.columns(3)

        with a1:
            st.info(
                "🐍 Python\n\nProgramming Language"
            )

        with a2:
            st.info(
                "🤖 Scikit-learn\n\nMachine Learning"
            )

        with a3:
            st.info(
                "🌐 Streamlit\n\nWeb Application"
            )

        st.subheader("📌 Project Benefits")

        st.write(
            "• User-friendly interface\n"
            "• Data visualization dashboard\n"
            "• Machine Learning prediction\n"
            "• Quick prediction results\n"
            "• Suitable for academic demonstration"
        )

        st.subheader("⚠️ Project Limitation")

        st.write(
            "This project is an academic Machine Learning demonstration. "
            "It does not calculate official tax liability or replace "
            "professional/government tax assessment."
        )

# =================================================
# FOOTER
# =================================================

st.markdown("""
<div class="footer">
    💼 Smart Tax Prediction System
    <br>
    Data Science & Machine Learning Project
</div>
""", unsafe_allow_html=True)