import streamlit as st

st.set_page_config(page_title="StudyBuddy", page_icon=":open_book:")

# CSS styles
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<span class='title'>_STUDY_:blue[BUDDY] :open_book: </span>", unsafe_allow_html=True)

st.sidebar.success("select a page from the above")

st.subheader("Introducing _STUDY_:blue[BUDDY]: Cut Your Reading Time in Half !")

st.subheader("Unlock Your Potential:")
st.write("- Dive into Books, Research Papers, Articles, Lecture Notes, Resumes and More!")
st.write("- Summarize, Simplify, Get Answers and Generate Questions with Ease.")
st.write("- No Keywords Needed—Just Ask and Explore!")
st.write("- Seamless Translation for Multilingual Understanding.")

st.subheader("How It Works:")
st.write("1. Upload PDFs or Enter Website URLs.")
st.write("2. Ask Your Questions.")
st.write("3. Get Instant Answers!")

st.write(":blue[Discover the Power of Knowledge — Try STUDYBUDDY Today!]")