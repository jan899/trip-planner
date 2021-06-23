# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template, jsonify

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


