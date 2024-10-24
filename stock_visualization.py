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

def process_data(data, start_date, end_date):
    time_series = data.get("Time Series (Daily)", {})
    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    closing_prices = []
    
    for date, values in time_series.items():
        if start_date <= date <= end_date:
            dates.append(date)
            open_prices.append(float(values['1. open']))  # Use '1. open' for open price
            high_prices.append(float(values['2. high']))   # Use '2. high' for high price
            low_prices.append(float(values['3. low']))     # Use '3. low' for low price
            closing_prices.append(float(values['4. close']))  # Use '4. close' for closing price

    return dates, open_prices, high_prices, low_prices, closing_prices

def plot_data(dates, open_prices, high_prices, low_prices, closing_prices, chart_type):
    if chart_type.lower() == 'line':
        line_chart = pygal.Line(title='Stock Price', x_title='Date', y_title='Price')
        
        line_chart.x_labels = dates  # Set the x-axis labels to the dates
        line_chart.add('Open', open_prices)
        line_chart.add('High', high_prices)
        line_chart.add('Low', low_prices)
        line_chart.add('Close', closing_prices)

        line_chart_file = 'stock_price_chart.svg'
        line_chart.render_to_file(line_chart_file)
    elif chart_type.lower() == 'bar':
        bar_chart = pygal.Bar(title='Stock Price', x_title='Date', y_title='Price')
        
        bar_chart.x_labels = dates  # Set the x-axis labels to the dates
        bar_chart.add('Open', open_prices)
        bar_chart.add('High', high_prices)
        bar_chart.add('Low', low_prices)
        bar_chart.add('Close', closing_prices)

        line_chart_file = 'stock_price_chart.svg'
        bar_chart.render_to_file(line_chart_file)
    else:
        print("Unsupported chart type.")
        return None
    
    return line_chart_file

def open_chart_in_browser(file_name):
    webbrowser.open(file_name)

def stockMaker(stock_symbol, chart_type,function,start_date,end_date):
    """
    Stock symbol like IBM,
    Chart type like line or bar
    function like TIME_SERIES_DAILY or TIME_SERIES_WEEKLY
    Start date in yyyy-mm-dd format
    end date in yyyy-mm-dd format
    """
    # User input section
    # stock_symbol = input("Enter the stock symbol: ")
    # chart_type = input("Enter the chart type (line/bar): ")
    # function = input("Enter the time series function (TIME_SERIES_DAILY, TIME_SERIES_WEEKLY, etc.): ")
    
    # start_date = input("Enter the beginning date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Validate date input
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    
    if end_date_obj < start_date_obj:
        print("Error: The end date cannot be before the start date.")
    else:
        stock_data = get_stock_data(stock_symbol, function)
        dates, open_prices, high_prices, low_prices, closing_prices = process_data(stock_data, start_date, end_date)
        
        if dates and open_prices and high_prices and low_prices and closing_prices:
            chart_file = plot_data(dates, open_prices, high_prices, low_prices, closing_prices, chart_type, stock_symbol)
            if chart_file:
                open_chart_in_browser(chart_file)
        else:
            print("No data available for the given date range.")
