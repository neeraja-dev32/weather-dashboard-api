import requests
import csv

while True:
    city = input("\nEnter city (or exit) :")
    
    if city.lower() == "exit":
        break
     
    
    
    url = f"https://wttr.in/{city}?format=j1"

    try:

      response = requests.get(url, timeout =5)


      weather_data = response.json()
    
    except Exception:
    
         print("weather data unavailable")
    
         print("Please enter valid city name")

         continue
 
     

    print("\n===== WEATHER REPORT =====")

    print(
    "Temparature:",
    weather_data["current_condition"][0]["temp_C"],
    "℃"
    )

    print(
    "Humidity:",
    weather_data["current_condition"][0]["humidity"],
    "%"
    )

    print(
    "Wind Speed:",
    weather_data["current_condition"][0]["windspeedKmph"],
    "km/h"
    )

    print(
    "Weather:",
    weather_data["current_condition"][0]["weatherDesc"][0]["value"]
    )

    print(
     "Feels Like:",
     weather_data["current_condition"][0]["FeelsLikeC"],
     "℃"
     )

    print(
     "Visibility:",
     weather_data["current_condition"][0]["visibility"],
     "km"
     )

    print(
    "Updated At:",
    weather_data["current_condition"][0]["observation_time"]
    )

    print(
    "Country:",
    weather_data["nearest_area"][0]["country"][0]["value"]
    )

    print(
    "Sunrise:",
    weather_data["weather"][0]["astronomy"][0]["sunrise"]
    )

    print (
     "Sunset:",
     weather_data["weather"][0]["astronomy"][0]["sunset"]
     )
    print(
     "\nTomorrow Forecast:"
   
     )
    print(
     weather_data["weather"][1]["hourly"][0]["weatherDesc"][0]["value"]
     )

     

with open("weather_report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["city", "Country", "Temperature", "Humidity", "Wind", "Weather", "Feels Like", "Tomorrow Forecast"])
    writer.writerow([
        city,

         weather_data["nearest_area"][0]["country"][0]["value"],
         weather_data["current_condition"][0]["temp_C"],
         weather_data["current_condition"][0]["humidity"],
         weather_data["current_condition"][0]["windspeedKmph"],
         weather_data["current_condition"][0]["weatherDesc"][0]["value"],
         weather_data["current_condition"][0]["FeelsLikeC"],
         weather_data["weather"][1]["hourly"][0]["weatherDesc"][0]["value"]
    ])
print("\nCSV Saved")
 
