# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template, jsonify
from app.trip_planner import fetch_flight_data, to_usd

#from app.weather_service import get_hourly_forecasts

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    #return "About Me"
    return render_template("about.html")

@home_routes.route("/home/results", methods=["POST"])
def r():
    print("RESULTS...")
    #return "About Me"
    
    
    #if request.method == "GET":
    #   print("URL PARAMS:". dict(request.args))
    results_data = dict(request.form)

    departure_airport_code = results_data.get("departure_airport_code")
    arrival_airport_code = results_data.get("arrival_airport_code")
    departure_date = results_data.get("departure_date")

    

       
    try:
        
        raw_data = fetch_flight_data(departure_airport_code, arrival_airport_code, departure_date)
        
        cheapest_airline = raw_data["Carriers"][0]["Name"]
        cheapest_price = to_usd(raw_data["Quotes"][0]["MinPrice"])
        cheapest_direct = raw_data["Quotes"][0]["Direct"]
        if cheapest_direct == True:
            cheapest_direct = "Yes"
        else:    
            cheapest_direct = "No"
        return render_template("trip_results.html",departure_airport_code=departure_airport_code,arrival_airport_code=arrival_airport_code,departure_date=departure_date, cheapest_airline=cheapest_airline, cheapest_price=cheapest_price, cheapest_direct=cheapest_direct)
    except IndexError:
        return render_template("error_page_noflights.html")
    except KeyError:
        return render_template("error_page_invalid.html")
    


#@home_routes.route("/hello")
#def hello_world():
#    print("HELLO...", dict(request.args))
#    # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
#    # ... which will return None instead of throwing an error if key is not present
#    # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
#    name = request.args.get("name") or "World"
#    message = f"Hello, {name}!"
#    return message
#    #return render_template("hello.html", message=message)

# web_app/routes/weather_routes.py




#weather_routes = Blueprint("weather_routes", __name__)
#
#@weather_routes.route("/weather/forecast.json")
#def weather_forecast_api():
#    print("WEATHER FORECAST (API)...")
#    print("URL PARAMS:", dict(request.args))
#
#    country_code = request.args.get("country_code") or "US"
#    zip_code = request.args.get("zip_code") or "20057"
#
#    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
#    if results:
#        return jsonify(results)
#    else:
#        return jsonify({"message":"Invalid Geography. Please try again."}), 404


