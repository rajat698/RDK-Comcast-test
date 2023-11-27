import requests
from datetime import datetime, timezone

API_key = "31ad51abcb9c543b6a9133f96f427dfc"

favourites = []

def utc_to_ampm(timestamp):

    # Convert UTC timestamp to a datetime object
    utc = datetime.utcfromtimestamp(timestamp).replace(tzinfo=timezone.utc)

    # Format the datetime object to AM/PM format
    result = utc.strftime("%I:%M:%S %p")

    return result

def display_weather(city):
    MAIN_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=imperial"
    response = requests.get(MAIN_URL).json()

    try:
        weather_data = f'''\nDescription: {response['weather'][0]['description']}
Temperature: {response['main']['temp']} 
Feels like: {response['main']['feels_like']} 
Minumum: {response['main']['temp_min']} 
Maximum: {response['main']['temp_max']} 

Pressure: {response['main']['pressure']} 
Humidity: {response['main']['humidity']} %

Visibility: {response['visibility']} 
Wind Speed: {response['wind']['speed']} 
Wind Degree: {response['wind']['deg']} 

Sunrise: {utc_to_ampm(response['sys']['sunrise'])} UTC 
Sunset: {utc_to_ampm(response['sys']['sunset'])} UTC'''
        return weather_data
    
    except:
        return "Invalid/Incorrect city name"

def add_favourites(city):
    if city in favourites:
        return "City already exists in favorites"
    
    favourites.append(city)
    return f"\nUpdated Favourites List: {favourites}\n"

def remove_favourites(city):
    favourites.remove(city)
    return f"Updated Favourites List: {favourites}\n"

def main():
    print('''Welcome to Rajat's CLI Weather APP
          
Enter name of a city to see the current weather
OR
Press 1 to add a city to favourites
OR
Press 2 to display favourites
OR
Press 3 to remove a city from favourites
OR
Enter 'exit' to exit the application
          
Note - Imperial system is used for units''')

    while True:
        user_input = input("\n")

        if user_input == "1":

            if len(favourites) == 3:
                print("\nNumber of favorite cities cannot exceed 3\n")

            else:
                city = input("Please enter the city you want to add to favorites:\n")
                print(add_favourites(city))

        elif user_input == "2":
            for city in favourites:
                print("\n", city)
                print(display_weather(city))

        elif user_input == "3":
            city = input("Please enter the city you want to remove from favorites:\n")
            print(remove_favourites(city))

        elif user_input == "exit":
            break

        else:
            print(display_weather(user_input) if user_input not in '123' else "Invalid choice, please enter a valid city or option.")

if __name__ == "__main__":
    main()