import requests
from twilio.rest import Client

OWM_Endpoint = ""  # Get your own api key at https://home.openweathermap.org/users/sign_in
api_key = ""
MY_LAT = -23.489560
MY_LONG = -48.413990
account_sid = ""  # Get at https://www.twilio.com/try-twilio
auth_token = ""  # Get at https://www.twilio.com/try-twilio
twilio_number = "" # Get at https://www.twilio.com/try-twilio
your_cell_number = ""

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

will_rain = False

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "It's going to rain today. Remember to bring an umbrella!",
        from = "",
        to = ""
    )




