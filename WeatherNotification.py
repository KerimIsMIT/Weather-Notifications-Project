import requests
from plyer import notification 
#Using the Opean-Meto Geocoding API to get the latitude and longitude of the city
city = input("Choose a city: ")
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_params).json()
#Now we are extracting the Current Weather Data 
if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_res = requests.get(weather_url, params=weather_params).json()

    if "current_weather" in weather_res:
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]
        weather_info = f"{city}: {temp}'C, Wind {wind} km/h "
        print("Weather: ", weather_info)
        
        notification.notify(
        title = "Wheater Update",
        message = weather_info,
        timeout = 5
    )
    else:
        print("Weather data not found")
else:
    print("Sadly, This city was not found. Try again!!")
