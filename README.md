<div align="center">

# 🌾 AgroAI – The Smart Selling Advisor

### *From मेहनत to Profit: AI-Powered Market Intelligence for Farmers*

<br>

![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)
![Streamlit](https://img.shields.io/badge/Streamlit-Backend-FF4B4B?style=for-the-badge&logo=streamlit)
![Scikit](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram)

<br>

![n8n](https://img.shields.io/badge/n8n-Automation-EA4AAA?style=for-the-badge)
![LLM](https://img.shields.io/badge/GenAI-LLM-black?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

</div>

---

<div align="center">

### 🔗 Navigation

[The Problem](#-the-problem) • 
[Our Solution](#-our-solution) • 
[Tech Stack](#-tech-stack) • 
[Features](#-key-features) • 
[Architecture](#-end-to-end-architecture) • 
[Business Model](#-business-model)

</div>

---

## 🚨 The Problem

Indian farmers face price uncertainty at the most critical decision point: **selling**.

- 86% are small farmers → highly sensitive to price drops  
- Mandi price information is fragmented  
- Farmers sell immediately after harvest (lowest prices)  
- Tools are not beginner-friendly or multilingual  

### Core Questions:
- ❓ When should I sell?  
- ❓ Where should I sell?  

---

## 💡 Our Solution

AgroAI is an **AI Smart Selling Advisor** that predicts prices and gives action signals.

- 📈 Predicts upcoming mandi prices  
- 🤖 Recommends **SELL / HOLD / WAIT**  
- 📍 Suggests best nearby mandi  
- 🌍 Supports bilingual usage  

### 🎯 Outcome:
- Better timing  
- Better mandi choice  
- Better profit  

---

## 🧰 Tech Stack

<div align="center">

![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=flat-square)
![Vite](https://img.shields.io/badge/Vite-Build-purple?style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-Backend-red?style=flat-square)
![Scikit](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-Core-blue?style=flat-square)
![Telegram](https://img.shields.io/badge/Telegram-Chatbot-2CA5E0?style=flat-square)
![n8n](https://img.shields.io/badge/n8n-Automation-pink?style=flat-square)
![LLM](https://img.shields.io/badge/LLM-GenAI-black?style=flat-square)

</div>

---

## 🚀 Key Features

### 1️⃣ Real-Time + Historical Intelligence
- Uses mandi trends  
- High-frequency updates  
- Seasonal pattern analysis  

### 2️⃣ Local Mandi Price Prediction
- Crop-state forecasting  
- Visual price comparison  
- AI recommendation engine  

### 3️⃣ Multilingual Accessibility
- Hindi + English  
- Farmer-friendly UI  

### 4️⃣ Profit Optimization
- Arbitrage detection  
- Distance-aware pricing  
- Revenue estimation  

---

## ✅ What AgroAI Can Do Today

- 📅 7-day price forecast  
- 📊 Performance metrics (R², MAE, RMSE)  
- 📈 Trend charts (30-day + forecast)  
- ⚠️ Risk classification  
- 💰 Revenue estimation  

---




## ⚙️ End-to-End Architecture

```mermaid
flowchart TD
    classDef box fill:#EDE7F6,stroke:#7E57C2,stroke-width:1px;

    A[Agmarknet Data]:::box --> B[Preprocessing]:::box
    B --> C[Feature Engineering]:::box
    C --> D[RandomForest Models]:::box
    D --> E[Model Storage<br/>pkl + metadata]:::box
    E --> F[Prediction Engine<br/>7 day forecast]:::box
    F --> G[Decision Logic<br/>SELL HOLD WAIT]:::box
    G --> H[Arbitrage + Risk + Revenue]:::box

    H --> I[Streamlit Backend 8501]:::box
    H --> J[React Frontend 5173]:::box

    J --> K[Farmer Decision Support]:::box
```


## 🧠 USP Snapshot

- ✅ AI-based decision making  
- ✅ Actionable insights (not just data)  
- ✅ Farmer-first design  
- ✅ Multilingual accessibility  

---

## 💼 Business Model

### Freemium Model
- Free basic advisory
- Premium insights & analytics

### B2G / B2F
- Govt partnerships
- Institutional integrations

---

## 📈 Impact

- 📉 Reduce distress selling  
- 📈 Increase farmer income  
- 🤝 Build trust with explainable AI  
- 🌍 Improve accessibility  

---

## 🔮 Future Scope

- 📱 WhatsApp integration  
- 🌐 Advanced analytics dashboard  
- 📊 More crops & mandi coverage  

---

## ⚡ Local Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
streamlit run app.pyFrontend
cd frontend
npm install
npm run dev
📂 Project Structure
project/
├── backend/
├── frontend/
├── models/
├── data/
├── app.py
└── requirements.txt
## 📚 Reference Notes

> Grounded in real-world farmer challenges and designed for actionable, data-driven decision making.

Problem framing and strategy points in this README are aligned with your presentation deck themes, including:

- Farmer distress-selling context  
- Crop price decision intelligence  
- Mandi comparison and profitability focus  
- Accessibility-first product direction  
