import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Walmart Sales Insights",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for centered container and styling
st.markdown("""
<style>
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .chart-section {
        margin-bottom: 40px;
        padding: 20px;
        border-radius: 10px;
        background-color: #f8f9fa;
    }
    .section-title {
        color: #1f2937;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 15px;
    }
    .section-description {
        color: #6b7280;
        font-size: 16px;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    img {
        image-rendering: auto;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.title("📊 Walmart Sales Insights")
st.markdown("<br>", unsafe_allow_html=True)

# Chart 1
st.markdown('<div class="chart-section">', unsafe_allow_html=True)
st.subheader("🎄 Holiday vs Non-Holiday Sales Performance")
st.markdown('<p class="section-description">Compare sales performance during holiday and non-holiday periods to understand seasonal trends and promotional effectiveness.</p>', unsafe_allow_html=True)
st.image("holiday_vs_nonholiday_sales.png", use_column_width="auto", caption="Created in Tableau Desktop Public Edition")
st.markdown("</div>", unsafe_allow_html=True)

# Chart 2
st.markdown('<div class="chart-section">', unsafe_allow_html=True)
st.subheader("⛽ Weekly Sales vs Fuel Price Correlation")
st.markdown('<p class="section-description">Analyze the relationship between fuel prices and weekly sales to identify potential economic impacts on consumer spending patterns.</p>', unsafe_allow_html=True)
st.image("weekly_sales_vs_fuel_price.png", use_column_width="auto", caption="Created in Tableau Desktop Public Edition")
st.markdown("</div>", unsafe_allow_html=True)

# Chart 3
st.markdown('<div class="chart-section">', unsafe_allow_html=True)
st.subheader("🏆 Top 10 Stores by Average Weekly Sales")
st.markdown('<p class="section-description">Identify the highest-performing stores based on average weekly sales, highlighting locations with exceptional performance.</p>', unsafe_allow_html=True)
st.image("top10_avg_weekly_sales_by_store.png", use_column_width="auto", caption="Created in Tableau Desktop Public Edition")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("*Dashboard created with Streamlit • Data analysis by [Your Name]*")