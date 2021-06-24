# Setup and imports

import requests
import json

# Credit: Professor Rossetti 
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# Introduce the user to the app

print("-------------------------------------------------------")
print("           Welcome to the Flight Finder App!           ")
print("-------------------------------------------------------")
print("                                                       ")
print("                Lets find you a flight!                ")
print("                                                       ")

# Collect user inputs

origin_input_value = input("Please Input Departing Airport:")
destination_input_value = input("Please Input Destination Airport:")
year_input_value = input("Please Input Departure Year (yyyy):")
month_input_value = input("Please Input Departure Month (mm):")
day_input_value= input("Please Input Departure Day (dd):")

## FOR EASIER RUNNING DURING TESTING

# origin_input_value = "SFO"
# destination_input_value = "JFK"
# year_input_value = "2021"
# month_input_value = "08"
# day_input_value= "01"

# Clean up the inputs
country_input = "US"
currency_input = "USD"
origin_input = origin_input_value
destination_input = destination_input_value
date_input = year_input_value+"-"+month_input_value+"-"+day_input_value


url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/{country}/{currency}/en-US/{origin}-sky/{destination}-sky/{date}".format(country=country_input, currency=currency_input, origin=origin_input,destination=destination_input,date=date_input)

querystring = {"inboundpartialdate":date_input}

# We'll need to include an API variable here via the .env thing
headers = {
    'x-rapidapi-key': "e5eb6fe9efmshdc31df18adcf9acp183317jsndafb7aac79e2",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)



raw_data = json.loads(response.text)
# print(type(raw_data))
try:
  
    cheapest_airline = raw_data["Carriers"][0]["Name"]
    cheapest_price = to_usd(raw_data["Quotes"][1]["MinPrice"])
    cheapest_direct = raw_data["Quotes"][1]["Direct"]
    if cheapest_direct == True:
        if True: cheapest_direct = "Yes"
        if False: cheapest_direct = "No"
    print("-------------------------------------------------------")
    print("                                                       ")
    print("Cheapest Flight Available:")
    print("Airline:",cheapest_airline)
    print("Price:",cheapest_price)
    print("Is Direct:",cheapest_direct)
except IndexError:
    print("-------------------------------------------------------")
    print("                                                       ")
    print("Please Review Inputs")
