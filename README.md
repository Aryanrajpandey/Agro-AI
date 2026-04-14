# 🌾 AgroAI – Smart Selling Advisor

> From Data → Decisions → Profit  
> AI-powered market intelligence for smarter crop selling.

---

## 🧠 Tech Stack

![React](https://img.shields.io/badge/Frontend-React-blue)
![Vite](https://img.shields.io/badge/Build-Vite-purple)
![Streamlit](https://img.shields.io/badge/Backend-Streamlit-red)
![Python](https://img.shields.io/badge/Core-Python-yellow)
![Scikit](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![LLM](https://img.shields.io/badge/GenAI-LLM-black)
![n8n](https://img.shields.io/badge/Automation-n8n-pink)
![Telegram](https://img.shields.io/badge/Bot-Telegram-blue)

---

## 🔗 Quick Links

- [Problem](#-the-problem)
- [Solution](#-our-solution)
- [Tech Stack](#-tech-stack)
- [Features](#-key-features)
- [Architecture](#-architecture)
- [Business Model](#-business-model)

---

## 🚨 The Problem

Indian farmers face **price uncertainty at selling time**:

- 📉 Small farmers suffer heavy losses from price drops  
- 📊 Lack of real-time mandi insights  
- ⏳ Sell immediately after harvest (lowest prices)  
- 🌐 Tools are not local-language friendly  

### Core Questions:
- When should I sell?
- Where should I sell?

---

## 💡 Our Solution

AgroAI provides **AI-powered selling decisions**:

- 📈 Predicts crop prices (short-term)
- 🧠 Recommends: **SELL / HOLD / WAIT**
- 📍 Suggests best mandi location
- 🌍 Supports multilingual users

### 🎯 Outcome:
- Better timing  
- Better price  
- Higher profit  

---

## 🧰 Tech Stack

| Layer        | Technology |
|-------------|-----------|
| Frontend     | React + Vite |
| Backend      | Streamlit |
| ML Model     | Scikit-learn |
| Language     | Python |
| Automation   | n8n |
| GenAI Layer  | LLM |
| Chatbot      | Telegram Bot |

---

## 🚀 Key Features

### 1️⃣ Real-Time + Historical Intelligence
- Uses mandi trends
- Seasonal pattern detection

### 2️⃣ Price Prediction
- Crop + State specific forecasting
- Visual comparison charts

### 3️⃣ Multilingual Support
- Hindi + English interface
- Farmer-friendly UX

### 4️⃣ Profit Optimization
- Arbitrage detection
- Transport-aware logic
- Revenue calculator

---

## ✅ What AgroAI Can Do

- 📅 7-day price prediction
- 📊 Performance metrics (R2, RMSE)
- 📈 Trend analysis (30 days)
- ⚠️ Risk level prediction (High/Medium/Low)
- 💰 Revenue estimation

---

## ⚙️ Architecture
Agmarknet Data
↓
Preprocessing
↓
Feature Engineering
↓
Random Forest Models
↓
Prediction Engine
↓
Decision Logic (SELL/HOLD/WAIT)
↓
Frontend + Backend
↓
Farmer Decision Support
---

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
