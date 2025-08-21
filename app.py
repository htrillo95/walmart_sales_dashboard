import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

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
    @media only screen and (max-width: 768px) {
        .desktop-preview { display: none; }
        .mobile-note { display: block !important; }
    }
    @media only screen and (min-width: 769px) {
        .desktop-preview { display: block; }
        .mobile-note { display: none !important; }
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("📊 Walmart Sales Insights")

# --- Summary ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📝 Summary")
st.markdown("""
<p class="section-description">
This interactive dashboard provides insights into Walmart’s weekly sales data.  
Explore trends related to holidays, fuel prices, and store performance.  
Built with Python (Streamlit + Pandas) • Visuals by Tableau • Code + Notebook included.
</p>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Key Metrics ---
average_sales = df['Weekly_Sales'].mean()
top_store = df.groupby("Store")["Weekly_Sales"].mean().idxmax()
top_store_sales = df.groupby("Store")["Weekly_Sales"].mean().max()
fuel_correlation = df['Weekly_Sales'].corr(df['Fuel_Price'])

correlation_label = "Negligible"
if fuel_correlation < -0.1:
    correlation_label = "Negative"
elif fuel_correlation > 0.1:
    correlation_label = "Positive"

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Weekly Sales", f"${average_sales:,.0f}")
col2.metric("Top Store", f"Store {top_store}", f"${top_store_sales:,.0f}")
col3.metric("Fuel Sales Correlation", f"{fuel_correlation:.2f}")

st.caption("Top Store = highest average weekly sales in dataset.")
st.caption("Fuel sales correlation ranges from -1 to +1. Values near 0 (e.g. 0.01) indicate no meaningful relationship.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Store Selector ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🔍 Explore Store Performance")
selected_store = st.selectbox("Select a store", sorted(df['Store'].unique()))
store_data = df[df['Store'] == selected_store]

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Avg Weekly Sales", f"${store_data['Weekly_Sales'].mean():,.0f}")
col2.metric("Max Weekly Sales", f"${store_data['Weekly_Sales'].max():,.0f}")
col3.metric("Min Weekly Sales", f"${store_data['Weekly_Sales'].min():,.0f}")

st.markdown("### 📈 Weekly Sales Trend")
st.line_chart(store_data[["Date", "Weekly_Sales"]].set_index("Date"))
st.markdown('</div>', unsafe_allow_html=True)

# --- Charts ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🎄 Holiday vs Non-Holiday Sales Performance")
st.markdown('<p class="section-description">Compare sales performance during holiday and non-holiday periods to understand seasonal trends and promotional effectiveness.</p>', unsafe_allow_html=True)
st.image("images/holiday_vs_nonholiday_sales.png", use_container_width=True, caption="Created in Tableau")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("⛽ Weekly Sales vs Fuel Price Correlation")
st.markdown('<p class="section-description">Analyze how fuel prices may impact weekly sales patterns across stores.</p>', unsafe_allow_html=True)
st.image("images/weekly_sales_vs_fuel_price.png", use_container_width=True, caption="Created in Tableau")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🏆 Top 10 Stores by Avg Weekly Sales")
st.markdown('<p class="section-description">Visualize top performing stores ranked by average weekly revenue.</p>', unsafe_allow_html=True)
st.image("images/top10_avg_weekly_sales_by_store.png", use_container_width=True, caption="Created in Tableau")
st.markdown('</div>', unsafe_allow_html=True)

# --- Downloads ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📂 Download Data & Notebook")
st.markdown('<p class="section-description">Access the full cleaned dataset and analysis notebook below. You can also preview them before downloading.</p>', unsafe_allow_html=True)

with open("data/walmart_sales_cleaned.csv", "rb") as file:
    st.download_button("📉 Download Cleaned CSV", file, "walmart_sales_cleaned.csv", "text/csv")

with open("notebook/Walmart_Sales_Insights.ipynb", "rb") as file:
    st.download_button("📔 Download Jupyter Notebook", file, "Walmart_Sales_Insights.ipynb", "application/octet-stream")

st.markdown('</div>', unsafe_allow_html=True)

# --- CSV Preview ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("👁️ Preview: Cleaned Dataset (First 50 Rows)")
st.dataframe(df.head(50))
st.markdown('</div>', unsafe_allow_html=True)

# --- 📖 Scrollable Notebook Preview ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📖 Notebook Preview")
st.markdown("""
<p class="section-description">
Scroll through the notebook directly below (desktop only).  
<a href="https://nbviewer.org/github/htrillo95/walmart_sales_dashboard/blob/main/notebook/Walmart_Sales_Insights.ipynb" target="_blank">Click here to open in a new tab</a>.
</p>
""", unsafe_allow_html=True)

# Responsive iframe and mobile fallback
st.markdown('<div class="desktop-preview">', unsafe_allow_html=True)
st.markdown("""
<div style="border: 1px solid #ccc; height: 600px; overflow-y: scroll;">
    <iframe src="https://nbviewer.org/github/htrillo95/walmart_sales_dashboard/blob/main/notebook/Walmart_Sales_Insights.ipynb"
            width="100%" height="1000" style="border:none;">
    </iframe>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="mobile-note section-description">', unsafe_allow_html=True)
st.info("Notebook preview may not display on some mobile devices. [Open in new tab](https://nbviewer.org/github/htrillo95/walmart_sales_dashboard/blob/main/notebook/Walmart_Sales_Insights.ipynb) to view.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Notebook Highlights ---
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🧪 Notebook Highlights")
st.markdown("""
<p class="section-description">
The Jupyter notebook provides a walkthrough of the analysis process:
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
st.markdown("---")
st.markdown(
    "<div style='text-align:center; font-style:italic;'>Dashboard created with Streamlit • Data analysis by <span style='white-space:nowrap;'>Hector T</span></div>",
    unsafe_allow_html=True
)
st.markdown("""
📌 Want to learn more about how this project was built?  
👉 Visit [my portfolio](https://hectortrillo.vercel.app) or check out [the GitHub repo](https://github.com/htrillo95/walmart_sales_dashboard)
""")