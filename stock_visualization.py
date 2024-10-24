import requests
import pygal
from lxml import etree
from datetime import datetime
import webbrowser

def get_stock_data(symbol, function):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval=5min&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

