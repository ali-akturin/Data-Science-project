import yfinance as yf
import streamlit as st
import pandas as pd
import os
os.environ['NUMEXPR_MAX_THREADS'] = '16'
os.environ['NUMEXPR_NUM_THREADS'] = '8'
import numexpr
st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Netflix!

""")

tickerSymbol = 'NFLX'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period= '1d', start='2010-5-31', end='2020-5-31')
st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume

""")
st.line_chart(tickerDf.Volume)
