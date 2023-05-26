import streamlit as st
import pandas as pd
import numpy as pd
import yfinance as yf
import datetime

st.title('Stock Analysis')
ticker_symbol = st.text_input('Stock Ticker', 'MSFT')
ticker = yf.Ticker(ticker_symbol)
st.write(f'Stock analysis for {ticker_symbol}')


col1, col2= st.columns(2)

with col1:
   st.header("Start Date")
   sd = st.date_input(
       "Analysis Start Date",
       datetime.date(2019, 1, 1))

with col2:
   st.header("End Date")
   ed = st.date_input(
       "Analysis Start Date",
       datetime.date(2022, 1, 1))

# get historical market data
hist = ticker.history(period="1d",
                    start = f'{sd}',
                    end = f'{ed}')

st.write(f" Viewing info for {ticker}")

st.write(hist)

col1, col2= st.columns(2)

with col1:
   st.header("Volume Analysis")
   st.line_chart(hist['Volume'])

with col2:
    st.header("Price Analysis")
    st.line_chart(hist['Close'])
    

