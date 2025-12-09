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
st.title("🔥 Global Heatmap & Multi‑Level Analysis")
st.caption("Explore hotspots, country-level heatmaps, and province-level breakdowns.")
st.markdown("---")

# ---------------------------
# Load Data
# ---------------------------
df = pd.read_csv("archive/full_grouped.csv")
df["Date"] = pd.to_datetime(df["Date"])

# ---------------------------
# Month Filter (Default = Last 3 Months)
# ---------------------------
df["YearMonth"] = df["Date"].dt.to_period("M")
months = sorted(df["YearMonth"].unique())

# انتخاب پیش‌فرض: سه ماه آخر
default_start_index = max(0, len(months) - 3)

selected_months = st.sidebar.multiselect(
    "📅 Select Months",
    months,
    default=months[default_start_index:]
)

# فیلتر دیتاست بر اساس ماه‌های انتخاب‌شده
df = df[df["YearMonth"].isin(selected_months)]

if df.empty:
    st.error("No data available for the selected months.")
    st.stop()

# ---------------------------
# Metric Selector
# ---------------------------
metric = st.sidebar.selectbox(
    "📌 Select Metric",
    ["Confirmed", "Deaths", "Recovered", "Active"]
)

# ---------------------------
# Clean Data: Remove zero-only dates
# ---------------------------
daily_sum = df.groupby("Date")[metric].sum()
valid_dates = daily_sum[daily_sum > 0].index
df = df[df["Date"].isin(valid_dates)]

# ---------------------------
# Clean Data: Remove countries with no meaningful data
# ---------------------------
country_max = df.groupby("Country/Region")[metric].max()
valid_countries = country_max[country_max > 50].index
df = df[df["Country/Region"].isin(valid_countries)]

if df.empty:
    st.error("No usable data after cleaning zero-only countries.")
    st.stop()

# ---------------------------
# Limit to Top N Countries
# ---------------------------
top_n = st.sidebar.slider("Top N countries for heatmap", 10, 60, 30, 5)

country_max = df.groupby("Country/Region")[metric].max().sort_values(ascending=False)
top_countries = country_max.head(top_n).index
df_top = df[df["Country/Region"].isin(top_countries)]

if df_top.empty:
    st.error("No data available for selected filters.")
    st.stop()

# ---------------------------
# Global Heatmap
# ---------------------------
st.subheader("🌎 Global Heatmap (Daily Cases by Country)")
st.caption(
    f"Showing top {top_n} countries with highest {metric} values "
    f"from the last {len(selected_months)} months."
)

pivot = df_top.pivot_table(
    index="Date",
    columns="Country/Region",
    values=metric,
    aggfunc="sum"
).fillna(0)

# حذف کشورهایی که ۸۰٪ داده‌شان صفر است
zero_ratio = (pivot == 0).mean()
pivot = pivot.loc[:, zero_ratio < 0.8]

if pivot.empty:
    st.error("All countries filtered out due to excessive zero values.")
    st.stop()

fig_heatmap = px.imshow(
    pivot.T,
    aspect="auto",
    color_continuous_scale="Reds",
    title=f"🔥 Cleaned Global Heatmap — {metric}",
    labels={"x": "Date", "y": "Country"},
)

fig_heatmap.update_coloraxes(colorbar_title="Cases", cmin=0)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")

# ---------------------------
# Country-Level Trend
# ---------------------------
countries = sorted(df["Country/Region"].unique())
selected_country = st.sidebar.selectbox("🌍 Select Country for Detailed View", countries)

st.subheader(f"📈 {selected_country} — Daily {metric}")

country_df = df[df["Country/Region"] == selected_country]

if country_df.empty or country_df[metric].sum() == 0:
    st.warning("⚠️ No valid data available for this country.")
else:
    fig_country = px.line(
        country_df,
        x="Date",
        y=metric,
        title=f"{selected_country} — {metric} Over Time",
        color_discrete_sequence=["#FF4B4B"]
    )
    st.plotly_chart(fig_country, use_container_width=True)

    st.markdown("---")

    # ---------------------------
    # Province-Level Breakdown
    # ---------------------------
    st.subheader(f"🗺️ Province-Level Breakdown — {selected_country}")

    if "Province/State" in country_df.columns and country_df["Province/State"].nunique() > 1:
        latest_date = country_df["Date"].max()
        latest = country_df[country_df["Date"] == latest_date]

        if latest[metric].sum() == 0:
            st.warning("⚠️ No valid province-level data available for this country.")
        else:
            fig_province = px.bar(
                latest,
                x="Province/State",
                y=metric,
                title=f"{selected_country} — {metric} by Province/State (Latest Date: {latest_date.date()})",
                color=metric,
                color_continuous_scale="Reds"
            )
            st.plotly_chart(fig_province, use_container_width=True)
    else:
        st.info("ℹ️ No province-level breakdown available for this country.")

st.markdown("---")

# ---------------------------
# Raw Data
# ---------------------------
st.subheader("📄 Raw Data Preview (Filtered)")
st.dataframe(df_top.head(30), use_container_width=True)
