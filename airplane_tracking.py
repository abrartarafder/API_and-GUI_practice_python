import requests
# because the API shows up to 100 different flights -- range is 101 (Starts at 0 ends at 100 (not including 101))
params = {
  'access_key': '_________________________________'
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

name = input("Enter an Airline name: ")
for i in range(101):
    given_name = api_response['data'][i]['airline']['name']
    departure_airport = api_response['data'][i]['departure']['airport']
    arrival_airport = api_response['data'][i]['arrival']['airport']
    flight_number = api_response['data'][i]['flight']['number']
    given_code = api_response['data'][i]['airline']['iata']

    if name == given_name:
        print(f'\nDeparture Airport: {departure_airport}\nArrival Airport: {arrival_airport}\nFlight Number: {given_code}{flight_number}')
