import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()
EUROPEANA_API_KEY = os.getenv("EUROPEANA_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_europeana_data(query):
    url = f"https://api.europeana.eu/record/v2/search.json?wskey={EUROPEANA_API_KEY}&query={query}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def main():
    city = "Paris"
    weather_data = fetch_weather_data(city)
    print("OpenWeatherMap Data:", weather_data)

    weather_condition = weather_data.get("weather", [{}])[0].get("main", "Unknown")
    print(f"\nSearching Europeana for cultural artifacts related to '{weather_condition}'...")


    europeana_data = fetch_europeana_data(weather_condition)
    print("\nEuropeana Data:", europeana_data)  


    combined_data = {
        "Weather Data": weather_data,
        "Europeana Data": europeana_data.get("items", [])
    }
    

    filtered_data = {key: value for key, value in combined_data.items() if 'apikey' not in key.lower()}


    with open("weather_europeana_data.json", "w") as f:
        json.dump(filtered_data, f, indent=4)
    print("\nData saved to weather_europeana_data.json")

if __name__ == "__main__":
    main()
