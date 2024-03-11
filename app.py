import streamlit as st
import yfinance as yf 
import pandas as pd

st.write("""
 # Simple de preços de ações    
  mostram o preço de **fechamento** das ações e o **volume** do Google
""")

tickerSymbol = {
    'Apple Inc.': 'AAPL',
    'Amazon.com Inc.': 'AMZN',
    'Microsoft Corporation': 'MSFT',
    'Alphabet Inc.': 'GOOGL',
    'Meta Platforms Inc.': 'FB',
    'Tesla Inc.': 'TSLA',
    'JPMorgan Chase & Co.': 'JPM',
    'Johnson & Johnson': 'JNJ',
    'Visa Inc.': 'V',
    'Walmart Inc.': 'WMT',
    'Nvidia Corporation': 'NVDA',
    'Alibaba Group Holding Limited': 'BABA',
    'Berkshire Hathaway Inc.': 'BRK.B',
    'Mastercard Incorporated': 'MA',
    'Procter & Gamble Company': 'PG',
    'Verizon Communications Inc.': 'VZ',
    'Netflix Inc.': 'NFLX',
    'The Walt Disney Company': 'DIS',
    'Salesforce.com Inc.': 'CRM',
    'PayPal Holdings Inc.': 'PYPL',
    'Google': 'GOOGL'
}

selected_name = st.selectbox('Selecione uma empresa:', list(tickerSymbol.keys()))
selected_symbol = tickerSymbol[selected_name]

tickerData = yf.Ticker(selected_symbol)

tickerDF = tickerData.history(period='id', start='2010-5-31', end='2024-3-11')

st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)
