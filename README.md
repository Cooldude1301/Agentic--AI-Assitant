# 🚀 Agentic AI Assistant

Agentic AI Assistant is a modern Streamlit application that provides three core Natural Language Processing (NLP) functionalities powered by OpenAI:

- 📄 **Summarization**  
- 🌍 **Translation**  
- 😊 **Sentiment Analysis**

The app features a **futuristic robotic-blue UI**, card-style blocks, animations (progress bars, spinners, metrics), and a recruiter-ready dashboard design.

---

## ✨ Features

- **Summarization**: Condense long text into concise summaries.  
- **Translation**: Translate text into multiple languages (with custom language option).  
- **Sentiment Analysis**: Classify text as Positive, Negative, or Neutral.  
- **Interactive UI**: Card-style blocks, hover animations, progress bars, and spinners.  
- **Robotic Blue Background**: Futuristic wallpaper for a polished look.  

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/agentic-ai-assistant.git
   cd agentic-ai-assistant

2. **Create a Virtual environment**:
    python -m venv .venv
    source .venv/bin/activate   # On macOS/Linux
    .venv\Scripts\activate      # On Windows

3. **Install Dependencies**:
    pip install -r requirements.txt

---

🔑 Setup Secrets

Streamlit uses a secrets.toml file to store API keys securely.

Create a .streamlit folder in your project root.

Inside it, create a secrets.toml file:

---

📂 Project Structure

    agentic-ai-assistant/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Python dependencies
└── .streamlit/
    └── secrets.toml      # API key storage

---

📜 License

This project is licensed under the MIT License.

---

✅ With this README, plus your `requirements.txt` and `.streamlit/secrets.toml`, you have everything needed to run and share your project.  

Would you like me to also prepare a **requirements.txt** and a **sample `.streamlit/secrets.toml`** file so you can copy-paste them directly?












#### App Interace from Folder 03
![Streamlit Snowflake Dashboard](https://github.com/Cooldude1301/Avalanche_Sentilytics/blob/main/GenAI-Advanced_RAG_Chatbot/GenAI-RAG%20chatbot%201/assets/deploy-to-streamlit-in-snowflake-2.png)
![Streamlit Snowflake Dashboard](https://github.com/Cooldude1301/Avalanche_Sentilytics/blob/main/GenAI-Advanced_RAG_Chatbot/GenAI-RAG%20chatbot%202/assets/Integrating%20RAG%20Chatbot%20with%20Data.png)

By using inbuild libraries/snowflake packages with altair & bar - For people using trial account.
![Streamlit Snowflake Dashboard](https://github.com/Cooldude1301/Avalanche_Sentilytics/blob/main/GenAI-Advanced_RAG_Chatbot/GenAI-RAG%20chatbot%202/assets/Streamlit%20app%20-%20with%20altair%20(Not%20use%20Plotly%20or%20matplotlib)%20-%20For%20Trial%20Account.png)
---

## 🛠️ Setup & Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Cooldude1301/fast-prototyping-of-genai-apps-with-streamlit] or [https://github.com/Cooldude1301/Avalanche_Sentilytics]
    ```

2.  **Install Dependencies:**
    Each folder contains its specific logic. Ensure you have the necessary libraries installed:
    ```bash
    pip install streamlit pandas snowflake-snowpark-python matplotlib altair
    ```

3.  **Snowflake Configuration:**
    For the Data Assistant, ensure your `.streamlit/secrets.toml` is configured with your Snowflake credentials (do not commit this file to GitHub!).

---
*Disclaimer: This project was built as part of the DeepLearning.AI course curriculum.*
