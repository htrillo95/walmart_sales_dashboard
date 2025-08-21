import streamlit as st
import pandas as pd

# --- Data ---
df = pd.read_csv("data/walmart_sales_cleaned.csv")
df["Date"] = pd.to_datetime(df["Date"])

# --- Config ---
st.set_page_config(page_title="Walmart Sales Insights", page_icon="📊", layout="wide")

# --- Styles ---
st.markdown("""
<style>
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .card {
        background-color: #f0f4f8;
        padding: 30px 25px;
        margin-bottom: 40px;
        border-radius: 12px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    }
    .section-description {
        color: #6b7280;
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    .section-heading {
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Header & Summary ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("📊 Walmart Sales Insights")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📝 Summary")
st.markdown("""
<p class="section-description">
This dashboard analyzes Walmart's weekly sales data with respect to holidays, fuel prices, and store's performance. Visualizations were created in Tableau, and insights are presented to help identify patterns that could inform promotional strategies and inventory planning.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Key Metrics ---
average_sales = df['Weekly_Sales'].mean()
top_store = df.groupby("Store")["Weekly_Sales"].mean().idxmax()
top_store_sales = df.groupby("Store")["Weekly_Sales"].mean().max()
fuel_correlation = df['Weekly_Sales'].corr(df['Fuel_Price'])

# Interpret correlation
if fuel_correlation < -0.1:
    correlation_label = "Negative"
elif fuel_correlation > 0.1:
    correlation_label = "Positive"
else:
    correlation_label = "Negligible"

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Weekly Sales", f"${average_sales:,.0f}")
col2.metric("Top Store", f"Store {top_store}", f"${top_store_sales:,.0f}")
col3.metric("Fuel Sales Correlation", f"{fuel_correlation:.2f}")

st.caption("Top Store = highest average weekly sales in dataset.")
st.caption("Fuel sales correlation ranges from -1 to +1. Values near 0 (e.g. 0.01) indicate no meaningful relationship.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Explore Store Performance ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🔍 Explore Store Performance")

selected_store = st.selectbox("Select a store", sorted(df['Store'].unique()))
store_data = df[df['Store'] == selected_store]

# KPIs
store_avg = store_data['Weekly_Sales'].mean()
store_max = store_data['Weekly_Sales'].max()
store_min = store_data['Weekly_Sales'].min()

st.markdown("### 📍 Store Performance Highlights")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Weekly Sales", f"${store_avg:,.0f}")
col2.metric("Max Weekly Sales", f"${store_max:,.0f}")
col3.metric("Min Weekly Sales", f"${store_min:,.0f}")

# Dynamic Chart
st.markdown("### 📈 Weekly Sales Trend")
st.line_chart(store_data[["Date", "Weekly_Sales"]].set_index("Date"))
st.markdown('</div>', unsafe_allow_html=True)

# --- Chart 1: Holiday vs Non-Holiday ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎄 Holiday vs Non-Holiday Sales Performance")
st.markdown('<p class="section-description">Compare sales performance during holiday and non-holiday periods to understand seasonal trends and promotional effectiveness.</p>', unsafe_allow_html=True)
st.image("images/holiday_vs_nonholiday_sales.png", use_container_width=True, caption="Created in Tableau")
st.markdown('</div>', unsafe_allow_html=True)

# --- Chart 2: Weekly Sales vs Fuel ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("⛽ Weekly Sales vs Fuel Price Correlation")
st.markdown('<p class="section-description">Analyze how fuel prices may impact weekly sales patterns across stores.</p>', unsafe_allow_html=True)
st.image("images/weekly_sales_vs_fuel_price.png", use_container_width=True, caption="Created in Tableau")
st.markdown('</div>', unsafe_allow_html=True)

# --- Chart 3: Top 10 Stores ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🏆 Top 10 Stores by Avg Weekly Sales")
st.markdown('<p class="section-description">Visualize top performing stores ranked by average weekly revenue.</p>', unsafe_allow_html=True)
st.image("images/top10_avg_weekly_sales_by_store.png", use_container_width=True, caption="Created in Tableau")
st.markdown('</div>', unsafe_allow_html=True)

# --- Notebook & CSV Downloads ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📂 Download Data & Notebook")
st.markdown('<p class="section-description">Access the full cleaned dataset and analysis notebook below. You can also preview them before downloading.</p>', unsafe_allow_html=True)

# Download buttons
with open("data/walmart_sales_cleaned.csv", "rb") as file:
    st.download_button(
        label="📉 Download Cleaned CSV",
        data=file,
        file_name="walmart_sales_cleaned.csv",
        mime="text/csv"
    )

with open("notebook/Walmart_Sales_Insights.ipynb", "rb") as file:
    st.download_button(
        label="📔 Download Jupyter Notebook",
        data=file,
        file_name="notebook/Walmart_Sales_Insights.ipynb",
        mime="application/octet-stream"
    )

st.markdown('</div>', unsafe_allow_html=True)

# --- Scrollable CSV Preview ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("👁️ Preview: Cleaned Dataset (First 50 Rows)")
st.dataframe(df.head(50))
st.markdown('</div>', unsafe_allow_html=True)

# --- Scrollable Notebook Preview ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("👁️ Preview: Raw Notebook Code")
with open("notebook/Walmart_Sales_Insights.ipynb", "r", encoding="utf-8") as f:
    notebook_code = f.read()
st.code(notebook_code[:10000], language="json")  # clip long notebooks
st.markdown('</div>', unsafe_allow_html=True)

# --- Notebook Write-Up ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🧪 Notebook Highlights")
st.markdown("""
<p class="section-description">
The Jupyter notebook provides a reproducible walkthrough of the analysis process:
</p>
<ul class="section-description">
    <li>📂 Load and inspect raw data</li>
    <li>🧼 Clean nulls, fix datatypes</li>
    <li>📊 Analyze sales trends across time and stores</li>
    <li>🎄 Compare holiday vs non-holiday sales</li>
    <li>⛽ Explore fuel price correlation</li>
    <li>🏆 Rank stores by average weekly performance</li>
</ul>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Footer ---
st.markdown('</div>', unsafe_allow_html=True)  # close .main-container
st.markdown("---")
st.markdown("*Dashboard created with Streamlit • Data analysis by [Hector T]*")