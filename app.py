import streamlit as st

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="COVID‑19 Dashboard", layout="wide")

# ---------------------------
# Header
# ---------------------------
st.markdown("## 📊 COVID‑19 Analytics Dashboard")
st.caption("A professional multi‑page dashboard built using multiple curated datasets from Kaggle.")
st.markdown("---")

# ---------------------------
# Title Section
# ---------------------------
st.title("🌍 Welcome to the COVID‑19 Multi‑Page Dashboard")
st.write(
    """
    This dashboard provides a comprehensive, multi‑level analysis of the COVID‑19 pandemic using 
    global, country‑level, and time‑series datasets.  
    Navigate through the pages using the sidebar to explore different analytical perspectives.
    """
)

# ---------------------------
# Quick Navigation Guide
# ---------------------------
st.markdown("### 🧭 Quick Navigation Guide")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(
        """
        **🌍 Global Overview**  
        - Worldwide KPIs  
        - Top 10 countries  
        - Cases by continent  
        """
    )

with col2:
    st.info(
        """
        **🇺🇳 Country Analysis**  
        - KPIs for selected country  
        - Multi‑country comparison  
        - Trends & global map  
        """
    )

with col3:
    st.info(
        """
        **📈 Global Trends**  
        - Worldwide time‑series  
        - New cases & deaths  
        - Growth rate analysis  
        """
    )

with col4:
    st.info(
        """
        **🔥 Global Heatmap**  
        - Country × Date heatmap  
        - Province‑level breakdown  
        - Hotspot detection  
        """
    )

st.markdown("---")

# ---------------------------
# Data Sources Section
# ---------------------------
st.markdown("### 📚 Data Sources")

st.success(
    """
    This dashboard uses multiple datasets from **Kaggle's COVID‑19 Data Repository**, including:

    - `covid_19_clean_complete.csv` — Country‑level daily data  
    - `worldometer_data.csv` — Latest global summary  
    - `day_wise.csv` — Global time‑series  
    - `full_grouped.csv` — Multi‑level (country → province) dataset  

    **Source:** https://www.kaggle.com/datasets/imdevskp/corona-virus-report  
    """
)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("Designed and developed by SaeedSFR — Powered by Streamlit & Plotly.")
