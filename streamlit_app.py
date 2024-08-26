import streamlit as st

# Streamlit app
st.header("AI Interview Cheatsheet")
st.sidebar.header("AI Interview Preparation")

# Input Position
position = st.sidebar.text_input("Position")

# Input Company
company = st.sidebar.text_input("Company")

# Input JD
jd = st.sidebar.text_area("Paste JD here")

if st.sidebar.button("Submit"):
    if jd and position and company:
        st.markdown(open("cheatsheet.md", "r").read())
        st.sidebar.text("Number of cheatsheets generated: ")
    else:
        st.warning("Please provide Position, Company, and JD.")