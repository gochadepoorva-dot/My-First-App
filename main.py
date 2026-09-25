import streamlit as st

# -------------------------------
# PAGE TITLE
# -------------------------------

st.title("✈️🌍 Travel Assistant")
st.caption("Your personal travel planner 🧳✨")

# -------------------------------
# DESTINATION
# -------------------------------

st.subheader("📍 Choose Your Destination")

destinations = [
    "Goa 🏖️",
    "Manali 🏔️",
    "Kashmir ❄️",
    "Kerala 🌴",
    "Jaipur 🏰",
    "Mumbai 🌆",
    "Delhi 🏛️",
    "Ooty 🌿"
]

destination = st.selectbox(
    "Where do you want to go?",
    destinations
)

# -------------------------------
# TRIP DURATION
# -------------------------------

days = st.number_input(
    "🗓️ How many days is your trip?",
    min_value=1,
    max_value=30,
    value=3
)

# -------------------------------
# TRAVEL TYPE
# -------------------------------

travel_type = st.selectbox(
    "🎯 What kind of trip do you want?",
    [
        "Adventure 🧗",
        "Relaxation 😌",
        "Family Trip 👨‍👩‍👧",
        "Romantic 💕",
        "Nature 🌿",
        "Cultural 🏛️"
    ]
)

# -------------------------------
# BUDGET
# -------------------------------

budget = st.selectbox(
    "💰 What is your budget?",
    [
        "Budget Friendly 💵",
        "Moderate 💳",
        "Luxury 💎"
    ]
)

# -------------------------------
# TRAVEL GUIDANCE
# -------------------------------

guidance = {
    "Goa 🏖️": "Enjoy beaches, water activities, sunsets and delicious food!",
    "Manali 🏔️": "Perfect for mountains, adventure activities and beautiful scenery.",
    "Kashmir ❄️": "Explore beautiful valleys, lakes and mountain landscapes.",
    "Kerala 🌴": "Enjoy backwaters, beaches, greenery and traditional food.",
    "Jaipur 🏰": "Explore forts, palaces, markets and Rajasthani culture.",
    "Mumbai 🌆": "Explore Marine Drive, Gateway of India, beaches and street food.",
    "Delhi 🏛️": "Visit historical monuments, museums and famous food streets.",
    "Ooty 🌿": "Relax in the hills and enjoy gardens, lakes and scenic views."
}

# -------------------------------
# PLAN TRIP BUTTON
# -------------------------------

if st.button("✨ Plan My Trip"):

    st.success("🎉 Your trip is ready to plan!")

    st.write("### ✈️ Your Trip Details")

    st.write("📍 Destination:", destination)
    st.write("🗓️ Duration:", days, "days")
    st.write("🎯 Trip Type:", travel_type)
    st.write("💰 Budget:", budget)

    st.info("💡 Travel Guidance: " + guidance[destination])

    st.write("### 🧳 General Travel Tips")

    st.write("✅ Carry your important documents.")
    st.write("✅ Check the weather before travelling.")
    st.write("✅ Keep medicines and basic essentials with you.")
    st.write("✅ Keep some emergency money.")
    st.write("✅ Respect local culture and places.")

    st.success("🌟 Have a wonderful trip! Happy travelling! ✈️🌍")

    st.balloons()