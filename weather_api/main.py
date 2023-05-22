import requests

API_END = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "d608ff52bf98b712f4136d89f339e83e"
LAT = 26.765844
LONG = 83.364944
parameter = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(API_END, params=parameter)

data = response.json()["hourly"][:12]

will_rain = False

for hour in data:
    weather = hour["weather"]
    for data in weather:
        ID = data["id"]
        if ID < 600:
            will_rain = True


if will_rain:
    print("Bring your Umbrella.")
else:
    print(data["description"])
