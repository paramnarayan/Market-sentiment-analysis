import streamlit as st
from main import news_sentiment,gen_report


st.set_page_config(page_title="Market Sentiment Analysis")
st.title("Market Sentiment Analysis Dashboard")

@st.cache_data(ttl=3600)
def get_cached_report():
    return gen_report()
if st.button("Generate Market Sentiment Report"):
    with st.spinner("Fetching news and generating report..."):
        
        report = get_cached_report()
        st.success(report)