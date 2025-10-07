import requests

api_key = "3ea066166268d6d42fb739da5ef0c254"
user_input = input("Enter city: ")

try:
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
    data = weather_data.json()
    print(data)

    if data.get("cod") != 200:
        print("City not found or error occurred.")

    else:
        country = data['sys']['country']
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        wind = data['wind']['speed']
        coord1 = data['coord']['lon']
        coord2 = data['coord']['lat']

        print("------------------------------------------------")
        print(f"Country: {country}")
        print(f"The weather in {user_input} is: {weather}")
        print(f"The temperature in {user_input} is: {temp}ºC")
        print(f"Wind Speed: {round(wind)}")
        print(f"Longitude: {coord1}")
        print(f"Latitude: {coord2}")
        print("------------------------------------------------")

except Exception as e:
    print("Error:", e)

finally:
    print("Execution Successfully...")