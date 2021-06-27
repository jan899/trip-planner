from app.trip_planner import fetch_flight_data 

from datetime import datetime, timedelta

departure_airport_code_test = "SFO"
arrival_airport_code_test = "JFK"
tomorrow = datetime.today() + timedelta(days=1)  
departure_date_test = tomorrow.strftime('%Y-%m-%d') 

print(tomorrow)


def test_fetch():
    result = fetch_flight_data(departure_airport_code_test,arrival_airport_code_test,departure_date_test)
    assert len(result) > 0 




