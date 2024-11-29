from config import get_api_key
from weather import get_weather

def main():
    api_key = get_api_key()

    # Check if API key was retrieved from the .env file
    if not api_key:
        print("Error: No API key found. Please check your .env file.")
        return 
    
    # Prompt the user for the city name
    city = input("Enter the city name: ").strip()
    
    # Fetch weather data for the provided city
    weather_data = get_weather(city, api_key)

    if weather_data:
        # Print the weather information if data is fetched successfully
        print("\nWeather Information:")
        print(f"Location: {weather_data['location']['name']}, {weather_data['location']['country']}")
        print(f"Temperature: {weather_data['current']['temp_c']}°C")
        print(f"Condition: {weather_data['current']['condition']['text']}")
    else:
        print("Could not fetch weather data. Please try again.")

# Ensure that this script runs only when executed directly
if __name__ == "__main__":
    main()
