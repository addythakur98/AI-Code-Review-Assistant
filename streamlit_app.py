import streamlit as st
from app.reviewer import review_code


st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 AI Code Review Assistant")

st.markdown(
    "Analyze your code for **bugs, security issues, performance problems, "
    "and code-quality improvements** using AI."
)


# Language selection
language = st.selectbox(
    "Programming Language",
    ["C++", "Python", "Java"]
)


# Code editor
code = st.text_area(
    "Paste your code",
    height=450,
    placeholder="Paste your code here..."
)


col1, col2 = st.columns(2)

with col1:
    review_button = st.button(
        "🔍 Review Code",
        use_container_width=True
    )

with col2:
    clear_button = st.button(
        "🗑️ Clear",
        use_container_width=True
    )


if clear_button:
    st.rerun()


if review_button:

    if not code.strip():
        st.warning("Please enter some code first.")

    else:

        numbered_code = "\n".join(
            f"{i + 1}: {line}"
            for i, line in enumerate(code.splitlines())
        )

        with st.spinner("Analyzing your code..."):

            review = review_code(
                numbered_code,
                language
            )

        if review.startswith("ERROR:"):
            st.error(review)

        else:
            st.divider()

            st.subheader("📋 Code Review")

            st.markdown(review)