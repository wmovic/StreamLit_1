import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price APP


""")

tickerSymbol = "AAPL"
tickerData = yf.Ticker(tickerSymbol)

tickerDF=tickerData.history(period='1d',start='2010-5-31',end='2022-11-22')
st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
