# 🛍️ AI Shopping Recommender

An AI-powered shopping recommendation system built using **Streamlit**, **phidata**, and **HuggingFace/Groq LLMs**.  
Users can enter product preferences such as **type, color, features, and budget**, and the agent returns structured, reliable recommendations sourced from trusted e-commerce platforms.

---

## 🚀 Features

- 🧠 **LLM-powered recommendation agent** using phidata  
- 🎨 Simple and clean **Streamlit UI**  
- 🔍 Searches only trusted platforms (e.g., Daraz, Alibaba)  
- 📦 Returns product name, brand, price, key features, availability, and a direct product URL  
- ⏱️ Top 5 recommendations in a clean, structured format  
- 🔐 Uses `.env` file for API keys (excluded from repo)

---

## 📂 Project Structure

├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── .gitignore # Excludes .env and sensitive files
├── app_logo.jpg # App logo
└── README.md # Project documentation

## 🧑‍💻 Installation

### 1. Clone the repository

bash
git clone https://github.com/YOUR-USERNAME/ai-shopping-recommender.git
cd ai-shopping-recommender
Install dependencies
pip install -r requirements.txt
Create a .env file
Add your API key(s):

streamlit run app.py

