import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("GOOGLE_API_KEY not found. Please add it to your .env file.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.5-flash")

st.set_page_config(
    page_title="GenAI Multi Tool",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 GenAI Multi-Tool App")
st.write("Build AI tools using Python + Google Gemini")

def generate_response(prompt):
    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.7
            }
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"

option = st.sidebar.selectbox(
    "Choose Tool",
    [
        "Resume Generator",
        "LinkedIn Post",
        "Business Idea"
    ]
)

if option == "Resume Generator":

    st.header("📄 AI Resume Generator")

    name = st.text_input("Enter Your Name")
    role = st.text_input("Target Job Role")
    skills = st.text_area("Skills (comma separated)")

    if st.button("Generate Resume"):

        if not name or not role or not skills:
            st.warning("Please fill all the fields.")
        else:
            prompt = f"""
            Create a professional ATS-friendly resume.

            Name: {name}
            Target Role: {role}
            Skills: {skills}

            Include:
            - Professional Summary
            - Technical Skills
            - Education
            - Projects
            - Certifications
            - Strengths
            """

            with st.spinner("Generating Resume..."):
                result = generate_response(prompt)

            st.success("Resume Generated Successfully!")
            st.text_area("Generated Resume", result, height=450)

elif option == "LinkedIn Post":

    st.header("💼 AI LinkedIn Post Generator")

    topic = st.text_input("Enter Topic")

    if st.button("Generate Post"):

        if not topic:
            st.warning("Please enter a topic.")
        else:
            prompt = f"""
            Act as a LinkedIn content expert.

            Write a viral LinkedIn post on {topic}.

            Include:
            - Strong hook
            - Short paragraphs
            - Professional tone
            - Storytelling
            - Emojis
            - Call to action
            - 5 hashtags
            """

            with st.spinner("Generating Post..."):
                result = generate_response(prompt)

            st.success("Post Generated Successfully!")
            st.text_area("Generated Post", result, height=400)

elif option == "Business Idea":

    st.header("💡 AI Business Idea Generator")

    interest = st.text_input("Enter Your Interest")

    if st.button("Generate Ideas"):

        if not interest:
            st.warning("Please enter your interest.")
        else:
            prompt = f"""
            Generate 5 AI-based business ideas for someone interested in {interest}.

            For each idea provide:
            - Business Name
            - Problem
            - Target Customers
            - Revenue Model
            - Required Tools
            - Startup Cost
            """

            with st.spinner("Generating Ideas..."):
                result = generate_response(prompt)

            st.success("Ideas Generated Successfully!")
            st.text_area("Generated Ideas", result, height=450)

st.markdown("---")
st.markdown(
    "<center>Built with ❤️ using Streamlit & Google Gemini</center>",
    unsafe_allow_html=True
)