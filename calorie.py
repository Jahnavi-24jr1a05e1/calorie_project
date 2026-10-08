import streamlit as st

st.set_page_config(
    page_title="Calorie Calculator",
    page_icon="🔥",
    layout="centered"
)

st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 25px;
}

.result {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    background-color: #f1f5f9;
}

.calories {
    font-size: 38px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🔥 Calorie Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Calculate your estimated daily calorie requirement</div>',
    unsafe_allow_html=True
)

st.markdown("---")

st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=20
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=20.0,
        max_value=250.0,
        value=60.0,
        step=0.5
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=165.0,
        step=0.5
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

st.markdown("---")

st.subheader("🏃 Activity Level")

activity = st.selectbox(
    "Select your activity level",
    [
        "Sedentary - Little or no exercise",
        "Lightly Active - Exercise 1-3 days/week",
        "Moderately Active - Exercise 3-5 days/week",
        "Very Active - Exercise 6-7 days/week",
        "Extra Active - Hard exercise or physical job"
    ]
)

activity_factors = {
    "Sedentary - Little or no exercise": 1.2,
    "Lightly Active - Exercise 1-3 days/week": 1.375,
    "Moderately Active - Exercise 3-5 days/week": 1.55,
    "Very Active - Exercise 6-7 days/week": 1.725,
    "Extra Active - Hard exercise or physical job": 1.9
}

st.markdown("---")

st.subheader("🎯 Your Goal")

goal = st.selectbox(
    "Select your goal",
    [
        "Maintain Weight",
        "Lose Weight",
        "Gain Weight"
    ]
)

if st.button("🔥 Calculate Calories", use_container_width=True):

    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_factor = activity_factors[activity]

    daily_calories = bmr * activity_factor

    if goal == "Lose Weight":
        target_calories = daily_calories - 500
    elif goal == "Gain Weight":
        target_calories = daily_calories + 300
    else:
        target_calories = daily_calories

    st.success("✅ Calculation Completed!")

    st.markdown("## 📊 Your Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🔥 BMR",
            f"{bmr:.0f} kcal/day"
        )

    with col2:
        st.metric(
            "⚡ Daily Requirement",
            f"{daily_calories:.0f} kcal/day"
        )

    st.markdown("---")

    st.markdown(
        f"""
        <div class="result">
            <div>🎯 Recommended Daily Calories</div>
            <div class="calories">{target_calories:.0f} kcal</div>
            <div>per day</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    if goal == "Lose Weight":
        st.info(
            "💡 Your target is approximately 500 kcal below "
            "your estimated maintenance requirement."
        )

    elif goal == "Gain Weight":
        st.info(
            "💡 Your target is approximately 300 kcal above "
            "your estimated maintenance requirement."
        )

    else:
        st.info(
            "💡 This target is designed to approximately "
            "maintain your current weight."
        )

    st.caption(
        "⚠️ This is an estimate for general informational purposes "
        "and is not medical advice."
    )