''''
 The application should:

    Ask the user to enter the stock symbol for the company they want data for.
    Ask the user for the chart type they would like.
    Ask the user for the time series function they want the api to use.
    Ask the user for the beginning date in YYYY-MM-DD format.
    Ask the user for the end date in YYYY-MM-DD format.
        The end date should not be before the begin date
    > Generate a graph and open in the user’s default browser.

    API KEY: 19Z62OVAZ1XYL8JR

pip install pygal //graphing mod
pip install lxml // for chart to be rendered
pip install requests
'''

import requests
from datetime import datetime

def date_check(date): # checked, works
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])

    # Year Validation
    if not (2005 <= year <= 2025):
        print("No data available.")
        return False

    # Month Validation
    if month not in range(1, 13):
        print("Month is invalid.")
        return False

    # numDays(Month)
    if month in [1, 3, 5, 7, 8, 10, 12]:  # Months with 31 days
        if day > 31:
            print("Day is invalid.")
            return False
    elif month in [4, 6, 9, 11]:  # Months with 30 days
        if day > 30:
            print("Day is invalid.")
            return False
    elif month == 2:  # February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Leap year
            if day > 29:
                print("Day is invalid.")
                return False
        else:  # Non-leap year
            if day > 28:
                print("Day is invalid.")
                return False
    return True

def checkTime(time): # checked, works
    time = time.replace(";", "")

    # year input to month input
    if len(time) == 2:
        time += "0000"

    if len(time) != 6 or not time.isdigit():
        print("Invalid format. Please enter time as HH-MM-SS or HHMMSS.")
        return None

    hour = int(time[0:2])
    minute = int(time[2:4])
    second = int(time[4:6])

    if not (0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
        print("Please enter a valid time")
        return None

    return f"{hour:02d}:{minute:02d}:{second:02d}"  # Format as HH:MM:SS, unsure if needed

def calculate_days(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        # Calculate delta(days)
        days_difference = (end - start).days

        return f"{abs(days_difference)}day"

    except ValueError:
        print("Invalid date format. Please enter YYYY-MM-DD.")
        return None

def calculate_weeks(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        # Calculate the delta(days) and convert to weeks
        days_difference = (end - start).days
        weeks = abs(days_difference / 7)

        return f"{weeks:.2f}week"  # Format with 2 decimal places

    except ValueError:
        print("Invalid date format. Please enter YYYY-MM-DD.")
        return None

def calculate_months(start_date, end_date):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        # Calculate delta(months)
        years_difference = end.year - start.year
        months_difference = (years_difference * 12) + (end.month - start.month)

        return f"{abs(months_difference)}month"

    except ValueError:
        print("Invalid date format. Please enter YYYY-MM-DD.")
        return None

def get_input():
    # Prompt user for stock symbol, make sure it's not blank.
    stock_symbol = input("Please enter the stock symbol you are looking for (e.g. GOOG, AAPL): ").upper().strip()
    while not stock_symbol:
        print("The stock symbol cannot be blank.")
        stock_symbol = input("Please enter the stock symbol you are looking for (e.g. GOOG, AAPL): ").upper().strip()

    # Prompt user for chart type, either 1 or 2.
    print("Chart Types\n---------------\n1. Bar\n2. Line")
    chart_type = input("Please enter the chart you'd like (1, 2): ")
    while chart_type not in ["1", "2"]:
        print("Please enter 1 or 2.")
        chart_type = input("Please enter the chart you'd like (1, 2): ")
        while chart_type not in ["1", "2"]:
            print("Please enter 1 or 2.")
            chart_type = input("Please enter the chart you'd like (1, 2): ")

    if (chart_type == "1"):
        chart_type = "Bar"
    else:
        chart_type = "Line"

    # Prompt user for time series, either 1, 2, 3, or 4.
    print("Please select the time series of the chart you want to generate")
    print("------------------------------------------------------")
    print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
    time_series = input("Enter time series option (1, 2, 3, 4): ")
    while time_series not in ["1", "2", "3", "4"]:
        print("Please enter 1, 2, 3, or 4.")
        time_series = input("Enter time series option (1, 2, 3, 4): ")

    # Handle Intraday
    interval = None
    if time_series == "1":
        start_date = input("Please enter the day (YYYY-MM-DD): ")
        interval = "60min"
        date_check(start_date)

    # Handle Daily, Weekly, or Monthly
    else:
        start_date = input("Please enter the start date (YYYY-MM-DD): ")
        end_date = input("Please enter the end date (YYYY-MM-DD): ")
        
        # Validate input dates
        date_check(start_date)
        date_check(end_date)

        # Make sure end date is after start date, if not re-ask.
        while end_date < start_date:
            print("Error: End date cannot be before start date.")
            end_date = input("Please enter the end date (YYYY-MM-DD): ")
        if time_series == "2":
            calculate_days(start_date, end_date)
        elif time_series == "3":
            calculate_weeks(start_date, end_date)
        else:
            calculate_months(start_date, end_date)

    # Build and print the API URL
    api_url = build_alphavantage_url(stock_symbol, time_series, interval, "19Z62OVAZ1XYL8JR")
    print(api_url)

def build_alphavantage_url(symbols, time_series, interval, apikey):
    base_url = "https://www.alphavantage.co/query?"

    if time_series == "1":
        function_name = "TIME_SERIES_INTRADAY"
    elif time_series == "2":
        function_name = "TIME_SERIES_DAILY"
    elif time_series == "3":
        function_name = "TIME_SERIES_WEEKLY"
    else:
        function_name = "TIME_SERIES_MONTHLY"

    params = {
        "function": function_name,
        "symbol": symbols,
        "apikey": apikey
    }

    if function_name in ["TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", "TIME_SERIES_MONTHLY"]:
        params["outputsize"] = "full"

    if function_name == "TIME_SERIES_INTRADAY" and interval:
        params["interval"] = interval

    url_parts = [f"{key}={value}" for key, value in params.items()]
    full_url = base_url + "&".join(url_parts)
    return full_url

def main():
    get_input()
    
    while True:
        get_input()
        new = input("Would you like to view more stock data? Press 'y' to continue: ").lower()
        if new != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
