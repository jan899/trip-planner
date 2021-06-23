import requests

country_input = "US"
currency_input = "USD"
origin_input = "JFK"
destination_input = "SFO"
date_input = "2021-06-24"

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/{country}/{currency}/en-US/{origin}-sky/{destination}-sky/{date}".format(country=country_input, currency=currency_input, origin=origin_input,destination=destination_input,date=date_input)

querystring = {"inboundpartialdate":"2021-06-24"}

headers = {
    'x-rapidapi-key': "e5eb6fe9efmshdc31df18adcf9acp183317jsndafb7aac79e2",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

#print(response.text)
print(response("Quotes"))
