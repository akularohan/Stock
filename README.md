# 📈 Stock Inference Platform for Indian Equities Using RAG

NiveshAi is a **Stock Inference Platform** built to provide AI-powered insights for Indian stock market equities.  
It leverages **RAG (Retrieval-Augmented Generation)** to analyze historical financial data scraped from **screener.in** — no paid APIs needed!

---

## 📹 Demo Video
[![Watch the Demo](http://img.youtube.com/vi/2Sv1xANnG_Q/maxresdefault.jpg)](https://youtu.be/2Sv1xANnG_Q)

---

## 🚀 Features
- 🕵️ **Web Scraping:** Fetches financial data from Screener.in (last 4 years of data).
- 🧠 **AI Analysis via RAG:**  
  Generates a comprehensive analysis:
  - Company performance
  - Risk factors
  - Key financial insights
- 🖥️ **Tech Stack:**
  - **Frontend:** React.js
  - **Backend:** FastAPI (Python)
  - **AI:** Uses Groq API (LLM powered)

- ✅ **Zero API Dependency for Stock Data:**  
  Scrapes data directly from publicly available sources.

---

## 📷 Screenshots

### 🔵 Dashboard UI
![Dashboard UI](assets/dashboard.png)

### 🟢 AI Inference Output
![AI Inference Example](assets/ai_output.png)

---

## 🛠️ Getting Started

### 1. Clone My Repository

# Clone my repo
git clone <repo-link>
cd <repo-folder>

### 2. Backend Setup
pip install -r requirements.txt
# Add your Groq API key in the configuration
python server.py

### 3. Frontend Setup
cd frontend
npm install
npm start

