import streamlit as st
from tone_engine import generate_response

# App Title
st.title("🌍 LinguaTone AI")
st.subheader("Learn Language with Tone Awareness")

# Tone Selection
tone = st.selectbox(
    "Choose your tone:",
    ["Professional", "Personal"]
)

# User Input
user_input = st.text_input("Enter your sentence or question:")

# Generate Response Button
if st.button("Generate Response"):
    if user_input:
        response, explanation = generate_response(user_input, tone)

        # Display Response
        st.write("### 🤖 Chatbot Response:")
        st.success(response)

        # Display Explanation
        st.write("### 💡 Tone Explanation:")
        st.info(explanation)
    else:
        st.warning("Please enter some text!")
