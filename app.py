import os
import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="Agentic AI Assistant", page_icon="🤖", layout="wide")


# --- Load API key from Streamlit secrets vault ---
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --- Helper: Token Counter ---
def count_tokens(text):
    return len(text.split())

# --- Tool Functions ---
def summarizer(text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"Summarize the following text."},
            {"role":"user","content":text}
        ]
    )
    return response.choices[0].message.content

def translator(text, target_lang):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":f"Translate the following text to {target_lang}."},
            {"role":"user","content":text}
        ]
    )
    return response.choices[0].message.content

def sentiment_analysis(text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system","content":"Classify the sentiment of the text as Positive, Negative, or Neutral."},
            {"role":"user","content":text}
        ]
    )
    return response.choices[0].message.content

# --- Header ---
st.markdown("<h1 style='text-align:center;'>🚀 Agentic AI Assistant</h1>", unsafe_allow_html=True)
st.write("Choose a block below to perform Summarization, Translation, or Sentiment Analysis. (Max 200 tokens per query)")

# --- Dashboard Blocks ---
col1, col2, col3 = st.columns(3)

# --- Summarizer Block ---
with col1:
    st.markdown("<div class='block-container'>", unsafe_allow_html=True)
    st.subheader("📄 Summarize")
    text = st.text_area("Enter text:", key="summarize_input")
    token_count = count_tokens(text)
    st.progress(min(token_count, 200) / 200)
    st.caption(f"Tokens used: {token_count}/200")
    if st.button("Summarize", key="summarize_button"):
        if text.strip():
            if token_count > 200:
                st.error("❌ Too long! Please limit to 200 tokens.")
            else:
                with st.spinner("⚡ Summarizing..."):
                    result = summarizer(text)
                st.metric("Summary Preview", result[:50] + "...")
                st.write(result)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Translator Block ---
with col2:
    st.markdown("<div class='block-container'>", unsafe_allow_html=True)
    st.subheader("🌍 Translate")
    text = st.text_area("Enter text:", key="translate_input")
    lang = st.selectbox(
        "Choose target language:",
        ["French", "Spanish", "German", "Hindi", "Japanese", "Chinese", "Arabic", "Italian", "Custom"]
    )
    if lang == "Custom":
        lang = st.text_input("Enter custom language (e.g., 'Portuguese')", key="custom_lang")

    token_count = count_tokens(text)
    st.progress(min(token_count, 200) / 200)
    st.caption(f"Tokens used: {token_count}/200")
    if st.button("Translate", key="translate_button"):
        if text.strip() and lang:
            if token_count > 200:
                st.error("❌ Too long! Please limit to 200 tokens.")
            else:
                with st.spinner("🌐 Translating..."):
                    result = translator(text, lang)
                st.metric("Translation Preview", result[:50] + "...")
                st.write(result)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Sentiment Analysis Block ---
with col3:
    st.markdown("<div class='block-container'>", unsafe_allow_html=True)
    st.subheader("😊 Sentiment Analysis")
    text = st.text_area("Enter text:", key="sentiment_input")
    token_count = count_tokens(text)
    st.progress(min(token_count, 200) / 200)
    st.caption(f"Tokens used: {token_count}/200")
    if st.button("Analyze Sentiment", key="sentiment_button"):
        if text.strip():
            if token_count > 200:
                st.error("❌ Too long! Please limit to 200 tokens.")
            else:
                with st.spinner("🔍 Analyzing sentiment..."):
                    result = sentiment_analysis(text)
                st.metric("Sentiment", result)
                st.write(result)
    st.markdown("</div>", unsafe_allow_html=True)
