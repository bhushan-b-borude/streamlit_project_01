import yfinance as yf
import streamlit as st
import pandas as pd

st.write('''
# Simple Stock Price App

Shown are the stock ***closing price*** and ***volume*** of Google!
''')


start_date = st.sidebar.date_input('Start Date', pd.datetime(2010,5,31))
end_date = st.sidebar.date_input('End Date', pd.datetime(2020,5,31))

ticker_symbol = 'GOOGL'
ticker_data = yf.Ticker(ticker_symbol)
tickerdf = ticker_data.history(period='1d', start=start_date, end=end_date)

st.header('Closing Price')
st.line_chart(tickerdf.Close)
st.header('Volume')
st.line_chart(tickerdf.Volume)