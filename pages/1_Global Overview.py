import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Header (shared style)
# ---------------------------
st.markdown("## 📊 COVID‑19 Analytics Dashboard")
st.caption("Professional multi‑page dashboard powered by Kaggle datasets")
st.markdown("---")

# ---------------------------
# Page Title
# ---------------------------
st.title("🌍 Global Overview")

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv("archive/worldometer_data.csv")
df.columns = [c.strip() for c in df.columns]

# ---------------------------
# KPI Section
# ---------------------------
st.subheader("Key Global Metrics")

total_cases = df["TotalCases"].sum()
total_deaths = df["TotalDeaths"].sum()
total_recovered = df["TotalRecovered"].sum()

mortality_rate = (total_deaths / total_cases) * 100 if total_cases > 0 else 0
recovery_rate = (total_recovered / total_cases) * 100 if total_cases > 0 else 0

# First row KPIs
col1, col2, col3 = st.columns(3)
col1.metric("🦠 Total Cases", f"{int(total_cases):,}")
col2.metric("💀 Total Deaths", f"{int(total_deaths):,}")
col3.metric("💚 Total Recovered", f"{int(total_recovered):,}")

# Second row KPIs
col4, col5 = st.columns(2)
col4.metric("⚠️ Mortality Rate", f"{mortality_rate:.2f}%")
col5.metric("✅ Recovery Rate", f"{recovery_rate:.2f}%")

st.markdown("---")

# ---------------------------
# Top 10 Countries by Cases
# ---------------------------
st.subheader("🏆 Top 10 Countries by Total Cases")

top10 = df.sort_values("TotalCases", ascending=False).head(10)

fig_bar = px.bar(
    top10,
    x="Country/Region",
    y="TotalCases",
    title="Top 10 Countries by Total Cases",
    color="TotalCases",
    color_continuous_scale="Reds",
)
st.plotly_chart(fig_bar, use_container_width=True)

# ---------------------------
# Cases by Continent
# ---------------------------
if "Continent" in df.columns:
    st.markdown("---")
    st.subheader("🌎 Cases by Continent")

    continent_df = (
        df.groupby("Continent")["TotalCases"]
        .sum()
        .reset_index()
        .sort_values("TotalCases", ascending=False)
    )

    fig_pie = px.pie(
        continent_df,
        names="Continent",
        values="TotalCases",
        title="Distribution of Cases by Continent",
        color="Continent",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# ---------------------------
# Full Table
# ---------------------------
st.markdown("---")
st.subheader("📄 Full Country Table")

st.dataframe(
    df.sort_values("TotalCases", ascending=False),
    use_container_width=True
)
