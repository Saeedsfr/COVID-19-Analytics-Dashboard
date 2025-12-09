import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Header (shared style)
# ---------------------------
st.markdown("## 📊 COVID‑19 Analytics Dashboard")
st.caption("Professional multi‑page dashboard powered by Kaggle datasets")
st.markdown("---")

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv("archive/covid_19_clean_complete.csv")
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------
# Page Title
# ---------------------------
st.title("🇺🇳 Country Analysis")
st.caption("Detailed country-level trends, KPIs, and multi-country comparison.")
st.markdown("---")

# ---------------------------
# Sidebar Filters
# ---------------------------
countries = df["Country/Region"].unique()
selected_country = st.sidebar.selectbox("🌍 Select Country", sorted(countries))

st.sidebar.markdown("### 🌐 Compare Multiple Countries")
multi_countries = st.sidebar.multiselect(
    "Select Countries to Compare",
    options=sorted(countries),
    default=[selected_country]
)

min_date = df["Date"].min()
max_date = df["Date"].max()

date_range = st.sidebar.date_input(
    "📅 Select Date Range",
    [min_date, max_date]
)

if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

# ---------------------------
# Filter Data
# ---------------------------
mask = (df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))
filtered_df = df[mask]

country_df = filtered_df[filtered_df["Country/Region"] == selected_country]
compare_df = filtered_df[filtered_df["Country/Region"].isin(multi_countries)]

# ---------------------------
# KPI Section
# ---------------------------
st.subheader(f"📌 Key Metrics for {selected_country}")

if not country_df.empty:
    latest = country_df.sort_values("Date").iloc[-1]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🦠 Confirmed", f"{int(latest['Confirmed']):,}")
    col2.metric("💀 Deaths", f"{int(latest['Deaths']):,}")
    col3.metric("💚 Recovered", f"{int(latest['Recovered']):,}")

    mortality = (latest["Deaths"] / latest["Confirmed"] * 100) if latest["Confirmed"] > 0 else 0
    col4.metric("⚠️ Mortality Rate", f"{mortality:.2f}%")

    # Sidebar summary
    st.sidebar.markdown("### 📌 Country Summary")
    st.sidebar.info(
        f"""
        **Latest Date:** {latest['Date'].date()}  
        **Confirmed:** {int(latest['Confirmed']):,}  
        **Deaths:** {int(latest['Deaths']):,}  
        **Recovered:** {int(latest['Recovered']):,}  
        **Mortality Rate:** {mortality:.2f}%  
        """
    )
else:
    st.warning("No data available for the selected country and date range.")
    mortality = 0

# ---------------------------
# Insight Cards (Automatic Analysis)
# ---------------------------
st.markdown("---")
st.subheader("🔍 Automated Insights")

# Calculate last 7 days trend
last_week = country_df.sort_values("Date").tail(7)

trend_confirmed = last_week["Confirmed"].iloc[-1] - last_week["Confirmed"].iloc[0]
trend_deaths = last_week["Deaths"].iloc[-1] - last_week["Deaths"].iloc[0]
trend_recovered = last_week["Recovered"].iloc[-1] - last_week["Recovered"].iloc[0]

colA, colB, colC = st.columns(3)

# Confirmed trend
if trend_confirmed > 0:
    colA.success(f"📈 Cases increased by {trend_confirmed:,} in the last 7 days")
else:
    colA.info("✅ Cases are stable or decreasing")

# Deaths trend
if trend_deaths > 0:
    colB.error(f"⚰️ Deaths increased by {trend_deaths:,} in the last 7 days")
else:
    colB.info("💚 Deaths are stable or decreasing")

# Recovery trend
if trend_recovered > 0:
    colC.success(f"💚 Recoveries increased by {trend_recovered:,} in the last 7 days")
else:
    colC.warning("⚠️ Recoveries are not improving")

# ---------------------------
# Multi-Country Comparison
# ---------------------------
st.markdown("---")
st.subheader("📈 Multi‑Country Comparison")

if not compare_df.empty:
    fig_compare = px.line(
        compare_df.sort_values("Date"),
        x="Date",
        y="Confirmed",
        color="Country/Region",
        title="Confirmed Cases Over Time",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig_compare, use_container_width=True)
else:
    st.info("No data available for the selected date range and countries.")

# ---------------------------
# Trends Section
# ---------------------------
st.markdown("---")
st.subheader(f"📉 Trends in {selected_country}")

if not country_df.empty:
    # Area chart
    fig_area = px.area(
        country_df.sort_values("Date"),
        x="Date",
        y="Confirmed",
        title=f"📈 Cumulative Confirmed Cases — {selected_country}",
        color_discrete_sequence=["#FF4B4B"]
    )

    # Deaths chart
    fig_deaths = px.line(
        country_df,
        x="Date",
        y="Deaths",
        title="💀 Deaths Over Time",
        color_discrete_sequence=["#FF0000"]
    )

    # Recovered chart
    fig_recovered = px.line(
        country_df,
        x="Date",
        y="Recovered",
        title="💚 Recovered Over Time",
        color_discrete_sequence=["#00FF88"]
    )

    # Full-width area chart
    st.plotly_chart(fig_area, use_container_width=True)

    # Two-column layout
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_deaths, use_container_width=True)
    with col2:
        st.plotly_chart(fig_recovered, use_container_width=True)

else:
    st.info("No trend data available for this selection.")

# ---------------------------
# Global Map
# ---------------------------
st.markdown("---")
st.subheader("🗺️ Global Situation")

world_df = df.groupby("Country/Region")[["Confirmed", "Deaths"]].max().reset_index()

fig_map = px.choropleth(
    world_df,
    locations="Country/Region",
    locationmode="country names",
    color="Confirmed",
    title="🌍 Global Confirmed Cases",
    color_continuous_scale="Reds"
)

st.plotly_chart(fig_map, use_container_width=True)
