# 🌾 AgriVisionAI

### AI-Powered Smart Agriculture Assistant using Machine Learning, Gemini AI & Weather API

AgriVisionAI is an intelligent agriculture assistant developed using **Python** and **Streamlit** that helps farmers, researchers, and agriculture enthusiasts analyze crop production data, predict suitable crops, access real-time weather information, generate AI-powered farming advice, and download professional crop reports.

---

## 📸 Project Preview

![AgriVisionAI Dashboard](images/home.png)

---

## 🚀 Features

### 🌱 Crop Recommendation System
- Predicts the most suitable crop based on soil and environmental conditions.
- Uses trained Machine Learning models for accurate recommendations.

### 🤖 AI Farming Advisor (Gemini API)
- Integrated with **Google Gemini API**.
- Provides intelligent farming guidance.
- Answers agriculture-related queries.
- Suggests best farming practices, fertilizers, irrigation methods, and crop care.

### 🌦 Live Weather Forecast
- Integrated with **OpenWeather API**.
- Displays:
  - Temperature
  - Humidity
  - Wind Speed
  - Weather Conditions
- Helps farmers plan irrigation and cultivation.

### 📊 Advanced Analytics Dashboard
Interactive visualizations including:

- Crop Production Trends
- State-wise Production Analysis
- Top Producing States
- Crop Distribution
- Production Comparison
- Pie Charts
- Bar Charts
- Line Charts

### 📄 Smart Report Generator
Generate professional crop reports based on:

- State
- Crop
- Year

The report includes:

- Production statistics
- Cultivated area
- Yield analysis
- Crop summary
- Recommendations
- PDF download support

### 📈 Interactive Dashboard
Provides quick insights through:

- KPIs
- Charts
- Production statistics
- Historical crop trends

---

# 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- Google Gemini API
- OpenWeather API
- ReportLab (PDF Generation)

---

# 📂 Project Structure

```
AgriVisionAI/
│
├── assets/
├── datasets/
├── models/
├── pages/
│   ├── Dashboard.py
│   ├── Crop_Prediction.py
│   ├── AI_Advisor.py
│   ├── Advanced_Analytics.py
│   ├── Weather.py
│   └── Reports.py
│
├── services/
│   ├── gemini_service.py
│   └── weather_service.py
│
├── utils/
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/upskillcampus.git
```

Go inside the project

```bash
cd AgriVisionAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🔑 API Integration

## Google Gemini API

Used for:

- AI Farming Guidance
- Crop Advisory
- Intelligent Recommendations
- Agricultural Question Answering

API Key is stored securely using:

```
.streamlit/secrets.toml
```

---

## OpenWeather API

Used for:

- Live Weather Forecast
- Temperature
- Humidity
- Wind Speed
- Weather Conditions

---

# 📊 Dataset

Crop Production Dataset containing:

- State
- District
- Crop
- Season
- Area
- Production
- Year

Used for:

- Crop Prediction
- Analytics
- Reports
- Dashboard

---

# 📄 Report Generation

The application can generate downloadable PDF reports containing:

- Crop Details
- State Information
- Production Statistics
- Area Under Cultivation
- Yield Summary
- AI-based Recommendations
- Report Generation Date

---

# 🎯 Future Enhancements

- Satellite Image Analysis
- Disease Detection using Deep Learning
- Voice-enabled AI Assistant
- Multilingual Support
- Market Price Prediction
- Fertilizer Recommendation System
- SMS Alerts
- Mobile Application

---

# 👩‍💻 Developed By

**Maskeen Luthra**

Final Internship Project

Upskill Campus
