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
    end_date = input("Please enter the end date (YYYY-MM-DD): ")

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