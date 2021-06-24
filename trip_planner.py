import requests
import json

# Introduce the user to the app

print("---------------------------------")
print("Welcome to the Flight Finder App!")
print("---------------------------------")

print("Lets find you a flight!")

# Collect user inputs

origin_input_value = input("Please Input Departing Airport:")
destination_input_value = input("Please Input Destination Airport:")
year_input_value = input("Please Input Departure Year (yyyy):")
month_input_value = input("Please Input Departure Month (mm):")
day_input_value= input("Please Input Departure Day (dd):")

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

print("-------------------------------------------------------")
print("                                                       ")
print("Cheapest Flight Available:")
print(response.text)
#print(response.text["Quotes"])

#j =json.loads(response.text)
#print(json.dumps(j, indent =2))