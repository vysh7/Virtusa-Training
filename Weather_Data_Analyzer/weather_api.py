import requests

API_KEY = "your_api_key"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"]
        }
    return None
