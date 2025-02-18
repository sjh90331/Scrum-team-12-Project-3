import requests
import pygal
from lxml import etree
from datetime import datetime
import webbrowser

def get_stock_data(symbol, function):
    url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&interval=5min&apikey=HHL99QZD0HC2O9HW'
    response = requests.get(url)
    data = response.json()
    
    return data

def process_data(data, start_date, end_date):
    time_series = data.get("Time Series (Daily)", {})
    #print(time_series)
    dates = []
    open_prices = []
    high_prices = []
    low_prices = []
    closing_prices = []
    print(start_date, end_date)
    for date, values in time_series.items():
        if start_date <= date <= end_date:
            print("YES ITS HERE")
            dates.append(date)
            open_prices.append(float(values['1. open']))  # Use '1. open' for open price
            high_prices.append(float(values['2. high']))   # Use '2. high' for high price
            low_prices.append(float(values['3. low']))     # Use '3. low' for low price
            closing_prices.append(float(values['4. close']))  # Use '4. close' for closing price
        # else:
        #     pass
            #print("Something wrong with dates my boy")

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

def stockMaker(stock_symbol, chart_type,function,start_date,end_date,strStartDate, strEndDate):
    #from main import varaibles
    """
    Stock symbol like IBM,
    Chart type like line or bar
    function like TIME_SERIES_DAILY or TIME_SERIES_WEEKLY
    Start date in yyyy-mm-dd format
    end date in yyyy-mm-dd format
    """
    print(" AAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    
    print("made it here")
    # User input section
    # stock_symbol = input("Enter the stock symbol: ")
    # chart_type = input("Enter the chart type (line/bar): ")
    # function = input("Enter the time series function (TIME_SERIES_DAILY, TIME_SERIES_WEEKLY, etc.): ")
    
    # start_date = input("Enter the beginning date (YYYY-MM-DD): ")
    # end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    # Validate date input
    #start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    #end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')
    
    if end_date < start_date:
        print("Error: The end date cannot be before the start date.")
    else:
        stock_data = get_stock_data(stock_symbol, function)
        dates, open_prices, high_prices, low_prices, closing_prices = process_data(stock_data, strStartDate, strEndDate)
        print(dates, open_prices, high_prices, low_prices, closing_prices)
        if dates and open_prices and high_prices and low_prices and closing_prices:
            chart_file = plot_data(dates, open_prices, high_prices, low_prices, closing_prices, chart_type)
            if chart_file:
                open_chart_in_browser(chart_file)
        else:
            # errorText = "No data available for the given date range."
            # varaibles.listOfInputs.clear()
            # varaibles.questionIndex=0
            # varaibles.stringEndDate = ''
            # varaibles.stringStartDate = ''
            print("No data available for the given date range.")
