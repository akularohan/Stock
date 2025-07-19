# 📈 Stock Inference Platform for Indian Equities Using RAG

**NiveshAi** — a comprehensive and intelligent **AI-Powered Stock Inference Platform** purpose-built for the Indian equities market.  
It harnesses the advanced capabilities of **Retrieval-Augmented Generation (RAG)** to generate precise and contextual insights by analyzing historical financial data scraped directly from **Screener.in** — ensuring **zero reliance on paid APIs or third-party data providers**.

Designed for investors, analysts, and financial researchers, **NiveshAi** delivers a robust analytical framework to assess company performance, identify potential risks, and extract critical financial insights. By combining state-of-the-art AI with reliable data sources, the platform facilitates informed, data-driven investment decisions with speed and accuracy.

---

## 📹 Demo Video
[![Watch the Demo](http://img.youtube.com/vi/2Sv1xANnG_Q/maxresdefault.jpg)](https://youtu.be/2Sv1xANnG_Q)

---

## 🚀 Key Features

- 🕵️ **Web Scraping:**  
  - Efficient extraction of up to **4 years of financial data** directly from **Screener.in**, removing dependency on paid APIs.

- 🧠 **AI-Powered Analysis (RAG Framework):**  
  - Generates comprehensive, contextual insights including:
    - Historical company performance
    - Potential risk factors
    - Key financial indicators and trends

- 💻 **Modern Tech Stack:**  
  - **Frontend:** Developed using **React.js** for a responsive and dynamic interface  
  - **Backend:** Powered by **FastAPI (Python)** for scalable, high-performance APIs  
  - **AI Model:** Integrated via the **Groq API**, utilizing advanced LLM capabilities

- ✅ **API-Free Stock Data Acquisition:**  
  - Enables direct data scraping from publicly available and verified sources, ensuring complete autonomy from third-party APIs.

---

## 📷 Screenshots

### 🟢 AI Inference Output
<img width="1892" height="724" alt="AI Output" src="https://github.com/user-attachments/assets/38031288-cc85-472f-9c06-949083320642" />
<img width="1893" height="367" alt="AI Output" src="https://github.com/user-attachments/assets/d35e91a9-4b6b-4086-add4-7a0c9c8a81b8" />

---

## 🛠️ Getting Started

### 1. Clone the Repository
git clone https://github.com/akularohan/Stock_Inference_Platform_for_Indian_Equities_using_RAG_.git

cd Stock_Inference_Platform_for_Indian_Equities_using_RAG_

### 2. Create the .env File
In the project root directory, create a .env file and add your Groq LLM API key:  

LLM_API_KEY=your_groq_api_key

### 3. Backend Setup
pip install -r requirements.txt

python server.py

### 4. Frontend Setup
cd frontend

npm install

npm start



