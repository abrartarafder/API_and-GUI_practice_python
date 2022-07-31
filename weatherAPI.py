import requests

API_KEY = "d1403350853d332c2c1ed59dd3fcf327"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
# q --> query -- city because we want to get info based on the city

response = requests.get(request_url)

# response successful --> status code ==> 200 when response is successful
if response.status_code == 200:
    data = response.json()
    # print(data)

    country = data['sys']['country']
    print(f'\nCountry: {country}')

    weather = data['weather'][0]['description']
    print(f'Description: {weather}')

    # printing the temperature
    temperature = round(data['main']['temp'] - 273.15)
    print((f'Temperature: {temperature}°C'))

    feels_like = round(data['main']['feels_like'] - 273.15)
    print((f'Feels Like: {feels_like}°C'))

    min_temp = round(data['main']['temp_min'] - 273.15)
    print((f'Minimum temperature today: {min_temp}°C'))

    max_temp = round(data['main']['temp_max'] - 273.15)
    print((f'Maximum temperature today: {max_temp}°C\n'))

else:
    print("Error")
