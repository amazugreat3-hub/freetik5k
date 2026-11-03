import streamlit as st
import time

st.set_page_config(
    page_title="FreeTik 5K",
    page_icon="🚀",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: #080812;
    color: white;
}
h1 {
    color: #ff2d75;
    text-align: center;
}
.stButton>button {
    background: #ff2d75;
    color: white;
    border-radius: 12px;
    width: 100%;
    height: 45px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 FreeTik 5K")
st.caption("Your TikTok Creator Growth Platform")

st.divider()

st.subheader("👤 Join FreeTik")

profile = st.text_input(
    "Enter your TikTok profile URL",
    placeholder="https://www.tiktok.com/@username"
)

if st.button("Join FreeTik"):

    if "tiktok.com/@" in profile:

        st.session_state.profile = profile
        st.session_state.registered = True

        st.success("Welcome to FreeTik 5K!")

    else:
        st.error("Enter a valid TikTok profile URL.")

if st.session_state.get("registered", False):

    st.divider()

    st.header("🎯 Your Dashboard")

    st.write("TikTok Profile:", st.session_state.profile)

    st.metric("Follower Campaign Target", "5,000")

    st.metric("Free Likes Campaign", "Available")

    st.subheader("🏆 Complete 5 Easy Tasks")

    tasks = [
        "Explore your creator dashboard",
        "Choose your content category",
        "Create a video idea",
        "Choose five relevant hashtags",
        "Set your posting schedule"
    ]

    if "completed" not in st.session_state:
        st.session_state.completed = []

    for i, task in enumerate(tasks):

        if st.checkbox(task, key=f"task_{i}"):
            if i not in st.session_state.completed:
                st.session_state.completed.append(i)

    completed = len(st.session_state.completed)

    st.progress(completed / 5)

    st.write(f"Tasks completed: {completed}/5")

    if completed == 5:

        st.balloons()

        st.success(
            "Congratulations! You've unlocked "
            "your 5,000-follower campaign target!"
        )

        st.info(
            "Your account is eligible for genuine "
            "creator-promotion opportunities. "
            "Follower delivery is not guaranteed."
        )

st.divider()

st.caption("FreeTik 5K © 2026")