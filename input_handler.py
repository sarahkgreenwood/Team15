def get_stock_symbol():
    symbol = input("Please enter the stock symbol you are looking for (e.g. GOOG, AAPL): ").upper().strip()
    while not symbol:
        print("The stock symbol cannot be blank.")
        symbol = input("Please enter the stock symbol you are looking for (e.g. GOOG, AAPL): ").upper().strip()
    return symbol

def get_chart_type():
    print("Chart Types\n---------------\n1. Bar\n2. Line")
    chart_type = input("Please enter the chart you'd like (1, 2): ")
    while chart_type not in ["1", "2"]:
        print("Please enter 1 or 2.")
        chart_type = input("Please enter the chart you'd like (1, 2): ")
    return "Bar" if chart_type == "1" else "Line"

def get_time_series():
    print("Please select the time series of the chart you want to generate")
    print("------------------------------------------------------")
    print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
    choice = input("Enter time series option (1, 2, 3, 4): ")
    while choice not in ["1", "2", "3", "4"]:
        print("Please enter 1, 2, 3, or 4.")
        choice = input("Enter time series option (1, 2, 3, 4): ")
    return choice
