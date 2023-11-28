import requests
from timeFormatter import time_formatter

#Define OpenWeather API Key
API_key = "31ad51abcb9c543b6a9133f96f427dfc"

#Initialize a favorite cities list
favourites = []

# Retrieves current weather data for given city from OpenWeatherMap API and returns formatted string
def display_weather(city):

    #Defining the API URL
    MAIN_URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=imperial"
    response = requests.get(MAIN_URL).json()

    #Return weather data
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

Sunrise: {time_formatter(response['sys']['sunrise'])} UTC 
Sunset: {time_formatter(response['sys']['sunset'])} UTC'''
        return weather_data

    #Error in case the city name entered is not correct
    except:
        return "Invalid/Incorrect city name"

# Adds a city to the favorites list if it does not already exist
def add_favourites(city):

    #Return error if city already exists in favorites
    if city in favourites:
        return "City already exists in favorites"

    #Add a city to the favorites list if it does not already exist
    favourites.append(city)
    return f"\nUpdated Favourites List:\n{', '.join(map(str, favourites))}"

# Removes a city from the favorites list
def remove_favourites(city):
    if city not in favourites:
        return "City not in favorites list"
    
    favourites.remove(city)
    return f"\nUpdated Favourites List:\n{', '.join(map(str, favourites))}"

#Main function to run the weather app
def main():
    #Intro message
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

    #Infinite while loop to keep the app running until manually exited
    while True:
        user_input = input("\n")

        #Handle adding favourites
        if user_input == "1":

            #Check if favourite list is full before adding
            if len(favourites) == 3:
                print("\nNumber of favorite cities cannot exceed 3\n")

            else:
                city = input("Please enter the city you want to add to favorites:\n")
                print(add_favourites(city))

        #Handle displaying favourites
        elif user_input == "2":

            if len(favourites) == 0:
                print("\nFavourites list is empty\n")

            else:
                for city in favourites:
                    print("\n", city)
                    print(display_weather(city))

        #Handle removing favourites
        elif user_input == "3":
            if len(favourites) == 0:
                print("\nFavourites list is empty\n")
            else:
                city = input("Please enter the city you want to remove from favorites:\n")
                print(remove_favourites(city))

        #Handle exiting the app
        elif user_input == "exit":
            break
        
        #Handle rest of the inputs (display city weather)
        else:
            print(display_weather(user_input) if user_input not in '123' else "Invalid choice, please enter a valid city or option.")

#Driver code to call main function
if __name__ == "__main__":
    main()