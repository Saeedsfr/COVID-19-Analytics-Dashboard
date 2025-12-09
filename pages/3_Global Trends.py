import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Shared Header
# ---------------------------
st.markdown("## 📊 COVID‑19 Analytics Dashboard")
st.caption("Professional multi‑page dashboard powered by Kaggle datasets")
st.markdown("---")

# ---------------------------
# Page Title
# ---------------------------
st.title("📈 Global Trends Over Time")
st.caption("Worldwide evolution of confirmed cases, deaths, recoveries, and daily changes.")
st.markdown("---")

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv("archive/day_wise.csv")
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------
# KPI Section
# ---------------------------
st.subheader("🌍 Global Summary Metrics")

latest = df.iloc[-1]

col1, col2, col3, col4 = st.columns(4)
col1.metric("🦠 Total Confirmed", f"{int(latest['Confirmed']):,}")
col2.metric("💀 Total Deaths", f"{int(latest['Deaths']):,}")
col3.metric("💚 Total Recovered", f"{int(latest['Recovered']):,}")

mortality_rate = (latest["Deaths"] / latest["Confirmed"]) * 100 if latest["Confirmed"] > 0 else 0
col4.metric("⚠️ Mortality Rate", f"{mortality_rate:.2f}%")

st.markdown("---")

# ---------------------------
# Global Cumulative Trends
# ---------------------------
st.subheader("📉 Global Cumulative Metrics Over Time")

fig_global = px.line(
    df,
    x="Date",
    y=["Confirmed", "Deaths", "Recovered"],
    title="🌍 Global COVID‑19 Metrics Over Time",
    labels={"value": "Count", "variable": "Metric"},
    color_discrete_map={
        "Confirmed": "#FF4B4B",
        "Deaths": "#FF0000",
        "Recovered": "#00FF88"
    }
)
st.plotly_chart(fig_global, use_container_width=True)

st.markdown("---")

# ---------------------------
# New Cases & New Deaths (Two‑Column Layout)
# ---------------------------
st.subheader("📊 Daily New Cases & Deaths")

col1, col2 = st.columns(2)

with col1:
    fig_new_cases = px.line(
        df,
        x="Date",
        y="New cases",
        title="🆕 New Cases Per Day",
        color_discrete_sequence=["#FFA500"]
    )
    st.plotly_chart(fig_new_cases, use_container_width=True)

with col2:
    fig_new_deaths = px.line(
        df,
        x="Date",
        y="New deaths",
        title="⚰️ New Deaths Per Day",
        color_discrete_sequence=["#FF0000"]
    )
    st.plotly_chart(fig_new_deaths, use_container_width=True)

st.markdown("---")

# ---------------------------
# Growth Rate Charts
# ---------------------------
st.subheader("📈 Growth Rate Trends")

if "Growth rate" in df.columns:
    fig_growth = px.line(
        df,
        x="Date",
        y="Growth rate",
        title="📈 Daily Growth Rate (%)",
        color_discrete_sequence=["#4B7BFF"]
    )
    st.plotly_chart(fig_growth, use_container_width=True)

st.markdown("---")

# ---------------------------
# Raw Data Table
# ---------------------------
st.subheader("📄 Raw Data Preview")
st.dataframe(df.head(30), use_container_width=True)
