import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price App

Stock **closing price** and ***volume*** graph for Google
""")

# Check out "towardsdatascience.com" article: How to get stock data using python
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
# get historical prices for his ticker
tickerDF = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDF.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDF.Volume)