import streamlit as st
import openai

# Set page layout
st.set_page_config(page_title="Lunexa - AI Mood Journal", layout="centered")
st.title("Lunexa")
st.subheader("Your AI-powered mental wellness companion")
st.markdown("---")

# Set up OpenAI client using v1+ SDK
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Daily mood check-in
st.header("Daily Mood Check-In")
input_mode = st.radio("Choose input method:", ("Text", "Voice (coming soon)"))

if input_mode == "Text":
    user_input = st.text_area("How are you feeling today?", height=150)
    if st.button("Analyze My Mood"):
        if user_input.strip() == "":
            st.warning("Please enter something to analyze.")
        else:
            with st.spinner("Analyzing your mood..."):
                try:
                    response = openai.chat.completions.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "You are a compassionate mental health assistant. Analyze the emotional tone of the user's journal and give a mood score from 1 (very low) to 10 (very positive)."},
                            {"role": "user", "content": user_input}
                        ]
                    )
                    output = response.choices[0].message.content
                    st.success("Here's your mood analysis:")
                    st.write(output)
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Voice input will be available soon. Stay tuned!")

st.markdown("---")
st.header("Mood History")
st.info("Mood tracking and charts coming soon in the next version.")
st.markdown("---")
st.caption("Built with love and AI for your mental wellness.")
