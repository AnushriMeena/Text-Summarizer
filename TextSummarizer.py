import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# API configuration
OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-4o"

# 🔹 Custom styling (ink blue: #0b3d91, white text)
st.markdown("""
    <style>
        .stApp {
            background-color: #f5f9ff;
        }
        .title {
            color: #0b3d91;
            font-size: 36px;
            font-weight: bold;
        }
        .stTextArea textarea {
            font-size: 15px !important;
        }
        button[kind="primary"] {
            background-color: #0b3d91 !important;
            color: white !important;
        }
        .stFileUploader label {
            color: white !important;
            background-color: #0b3d91;
            padding: 6px 12px;
            border-radius: 5px;
            display: inline-block;
        }
    </style>
""", unsafe_allow_html=True)

# 🔹 Title
st.markdown('<div class="title">Text Summarizer </div>', unsafe_allow_html=True)

# 🔹 Text input area with watermark
text_input = st.text_area("Enter text to summarize:", placeholder="Paste your paragraph here...")

# 🔹 File uploader
uploaded_file = st.file_uploader("Or upload a .txt file to summarize", type=["txt"])

# 🔹 File reading logic
file_text = ""
if uploaded_file is not None:
    file_text = uploaded_file.read().decode("utf-8")

# 🔹 Choose source text: file or manual
final_text = file_text if file_text.strip() else text_input

# 🔹 Button to trigger summarization
if st.button("Summarize"):
    if not api_key:
        st.error("API key not found. Please set OPENAI_API_KEY in your .env file.")
    elif not final_text.strip():
        st.warning("Please enter text or upload a file.")
    else:
        with st.spinner("Summarizing..."):
            payload = {
                "model": MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": (
                            "You are an expert summarizer. Read the user's input text "
                            "and extract the most important points in bullet format. "
                            "Keep it brief and clear."
                        )
                    },
                    {"role": "user", "content": final_text}
                ]
            }
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            try:
                response = requests.post(OPENAI_API_URL, headers=headers, json=payload)
                response.raise_for_status()
                summary = response.json()["choices"][0]["message"]["content"]

                st.subheader("📝 Summary Points:")
                st.markdown(summary)
            except Exception as e:
                st.error(f"Error: {e}")
