/* The application should:

    Ask the user to enter the stock symbol for the company they want data for.
    Ask the user for the chart type they would like.
    Ask the user for the time series function they want the api to use.
    Ask the user for the beginning date in YYYY-MM-DD format.
    Ask the user for the end date in YYYY-MM-DD format.
        The end date should not be before the begin date
    Generate a graph and open in the user’s default browser.
*/

print("Stock Data Visualizer /n -------------------------------------------------");
print("Enter the stock symbol you are looking for: "):
symbol = input();

if (symbol = notnull) {
  print("Chart Types /n ------------------");
  print("1. Bar");
  print("2. Line"); // probably make this; for i in symbol, i = "." + chartname.
  print("Enter the chart type you want ("/*i, i++*/"): ";
  chart = input();
    if (chart > 2) {
        print("Enter a (1, 2) for a chart type");
    }

  if (chart = notnull) {
    print("Select the Time Series of the chart you want to Generate /n ----------------------------------------------");
    print("1." + null); //same thing as comment before. Intraday, Daily, Weekly, Monthly
    print("Enter time series option ("/*i, i++*/"): ";
    timeseries = input();

    if (timeseries = notnull) {
      print("Enter the start Date (YYYY-MM-DD): ");
      startday = input();
        /*Error: Start date cannot be later than End date. Enter the dates again."*/
      print("Enter the end Date (YYYY-MM-DD): ");
      endday = input();

      print("Would you like to view more stock data? Press 'y' to continue: ")
      /*somehow witchcraft a file stock graph and print it to the console*/
      if_y = input();

      if (if_y == 'y') {
        /*restart*/
      }
    }
  }
}
