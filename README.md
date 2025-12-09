# 📊 COVID‑19 Analytics Dashboard

A professional, multi‑page COVID‑19 analytics dashboard built with **Streamlit** and **Plotly**, powered by multiple curated datasets from Kaggle.  
This project demonstrates end‑to‑end data exploration, interactive visualizations, and BI‑style insights on the global COVID‑19 pandemic.

---

## 🚀 Features

### ✅ Multi‑page dashboard structure
- 🏠 Home (Landing Page)
- 🌍 Global Overview
- 🇺🇳 Country Analysis
- 📈 Global Trends
- 🔥 Global Heatmap & Multi‑Level Analysis

### ✅ Global Overview
- Worldwide KPIs (confirmed, deaths, recovered)
- Mortality & recovery rates
- Top 10 countries by total cases
- Cases by continent
- Full sortable country table

### ✅ Country Analysis
- Country‑level KPIs with auto‑calculated mortality rate
- Sidebar filters for country & date range
- Multi‑country comparison
- Trend charts for confirmed, deaths, recovered
- Global choropleth map
- Automated insight cards (7‑day trend analysis)

### ✅ Global Trends
- Global cumulative time‑series
- New cases & new deaths per day
- Growth rate visualization
- KPI snapshot for latest date

### ✅ Global Heatmap (Cleaned)
- Cleaned global heatmap (countries × dates)
- Focus on top N countries with meaningful data
- Month filter (default: last 3 months)
- Country‑level time‑series
- Province/State breakdown (if available)

---

## 📂 Project Structure

```
.
├── app.py
├── README.md
├── requirements.txt
├── archive/
│   ├── covid_19_clean_complete.csv
│   ├── worldometer_data.csv
│   ├── day_wise.csv
│   ├── full_grouped.csv
│   └── ...
├── pages/
│   ├── 1_Global Overview.py
│   ├── 2_Country Analysis.py
│   ├── 3_Global Trends.py
│   └── 4_Global Heatmap.py
└── .streamlit/
    └── config.toml
```

---

## 📚 Data Sources

This dashboard uses multiple datasets from **Kaggle's COVID‑19 Data Repository**:

- `covid_19_clean_complete.csv` — Country‑level daily data  
- `worldometer_data.csv` — Latest global summary  
- `day_wise.csv` — Global time‑series  
- `full_grouped.csv` — Multi‑level (country → province) dataset  

**Source:**  
https://www.kaggle.com/datasets/imdevskp/corona-virus-report

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI & multi‑page app)
- **Pandas** (data manipulation)
- **Plotly Express** (interactive visualizations)

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Saeedsfr/COVID-19-Analytics-Dashboard.git
cd COVID-19-Analytics-Dashboard
```

### 2️⃣ Create a virtual environment (optional)

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, generate it:

```bash
pip freeze > requirements.txt
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🧭 Pages Overview

### 🏠 Home  
Introduction, navigation guide, and data source information.

### 🌍 Global Overview  
High‑level KPIs, top 10 countries, continent distribution.

### 🇺🇳 Country Analysis  
Detailed metrics, trends, comparisons, and global map.

### 📈 Global Trends  
Time‑series view of global confirmed, deaths, recovered, and daily changes.

### 🔥 Global Heatmap  
Cleaned heatmap focusing on top countries and recent months.

---

## 🎯 Purpose

This project was built as a **portfolio‑grade analytics dashboard** to demonstrate:

- Data cleaning & preprocessing  
- Multi‑page analytical workflows  
- BI‑style visuals & automated insights  
- Professional Streamlit app design  

---

## 🙋‍♂️ Author

Designed and developed by **SaeedSFR**  
Powered by **Streamlit** & **Plotly**
