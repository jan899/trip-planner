# Setup and imports

import requests
import json

# import dot-env and load the user name from the .env file 

import os
from dotenv import load_dotenv 
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
RAPID_API_KEY = os.getenv("RAPID_API_KEY", default="OOPS, please set env var called 'RAPID_API_KEY'")
RAPID_HOST = os.getenv("RAPID_HOST", default="OOPS, please set env var called 'RAPID_HOST'")

    # RAPID_API_KEY = str(RAPID_API_KEY)
    # RAPID_HOST = str(RAPID_HOST)

# Credit: Professor Rossetti 
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


#new function

def fetch_flight_data(departure_airport_code, arrival_airport_code, departure_date):

    country_input = "US"
    currency_input = "USD"


    url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/{country}/{currency}/en-US/{origin}-sky/{destination}-sky/{date}".format(country=country_input, currency=currency_input, origin=departure_airport_code,destination=arrival_airport_code,date=departure_date)

    querystring = {"inboundpartialdate":departure_date}

    headers = {
        'x-rapidapi-key': RAPID_API_KEY,
        'x-rapidapi-host': RAPID_HOST
        }

    # print(headers)
    # print(type(headers))

    response = requests.request("GET", url, headers=headers, params=querystring)



    raw_data = json.loads(response.text)
    return raw_data

if __name__ == "__main__":

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
    #country_input = "US"
    #currency_input = "USD"
    #origin_input = origin_input_value
    #destination_input = destination_input_value
    date_input = year_input_value+"-"+month_input_value+"-"+day_input_value


    #url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/{country}/{currency}/en-US/{origin}-sky/{destination}-sky/{date}".format(country=country_input, currency=currency_input, origin=origin_input,destination=destination_input,date=date_input)
    #
    #querystring = {"inboundpartialdate":date_input}
    #
    ## We'll need to include an API variable here via the .env thing
    #headers = {
    #    'x-rapidapi-key': "e5eb6fe9efmshdc31df18adcf9acp183317jsndafb7aac79e2",
    #    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    #    }
    #
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #
    #
    #
    #raw_data = json.loads(response.text)
    raw_data = fetch_flight_data(origin_input_value, destination_input_value, date_input)
    # print(type(raw_data))

    try:
    
        cheapest_airline = raw_data["Carriers"][0]["Name"]
        cheapest_price = to_usd(raw_data["Quotes"][0]["MinPrice"])
        cheapest_direct = raw_data["Quotes"][0]["Direct"]
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

    # Sending email 

    user_wants_email = input("Would the customer like an emailed receipt [y/n]: ")

    if user_wants_email == "y":

        CLIENT_ADDRESS = input("PLEASE INPUT CLIENT ADDRESS: ")

        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))

        subject = "Your Flight Information:"

        html_content = f"""
        <h3>Hello this is your flight </h3>
        <p>Date: {date_input} </p>
        <p>Airline: {cheapest_airline} </p>
        <p>Price: {cheapest_price} </p>
        <p>Direct: {cheapest_direct} </p>
        """

        # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
        # ... but we can customize the `to_emails` param to send to other addresses
        message = Mail(from_email=SENDER_ADDRESS, to_emails=CLIENT_ADDRESS, subject=subject, html_content=html_content)

        try:
            response = client.send(message)

            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            print(response.body)
            print(response.headers)

        except Exception as err:
            print(type(err))
            print(err)
    else: 
        print("No problem! No email sent!")