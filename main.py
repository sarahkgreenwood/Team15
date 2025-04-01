''''
 The application should:

    Ask the user to enter the stock symbol for the company they want data for.
    Ask the user for the chart type they would like.
    Ask the user for the time series function they want the api to use.
    Ask the user for the beginning date in YYYY-MM-DD format.
    Ask the user for the end date in YYYY-MM-DD format.
        The end date should not be before the begin date
    Generate a graph and open in the user’s default browser.

    API KEY: 19Z62OVAZ1XYL8JR
'''

def date_check(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[8:10])

    # Year Validation
    if not (2004 <= year <= 2026):
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
    elif month == 2:  # February (leap year check)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Leap year
            if day > 29:
                print("Day is invalid.")
                return False
        else:  # Non-leap year
            if day > 28:
                print("Day is invalid.")
                return False

    # If everything is fine
    print("Date is valid.")
    return True

def get_user_input():
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

    # Prompt user for time series, either 1, 2, 3, or 4.
    print("Please select the time series of the chart you want to generate")
    print("------------------------------------------------------")
    print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
    time_series = input("Enter time series option (1, 2, 3, 4): ")
    while time_series not in ["1", "2", "3", "4"]:
        print("Please enter 1, 2, 3, or 4.")
        time_series = input("Enter time series option (1, 2, 3, 4): ")

    # Prompt user for both start date and end date.
    start_date = input("Please enter the start date (YYYY-MM-DD): ")
    date_check(start_date)
    end_date = input("Please enter the end date (YYYY-MM-DD): ")
    date_check(end_date)
 
    # Make sure end date is after start date, if not re-ask.
    while end_date < start_date:
        print("Error: End date cannot be before start date.")
        end_date = input("Please enter the end date (YYYY-MM-DD): ")
    
    return stock_symbol, chart_type, time_series, start_date, end_date
    
def main():
    user_data = get_user_input()
    print(user_data)

if __name__ == "__main__":
    main()
