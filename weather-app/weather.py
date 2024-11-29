import requests

def get_weather(city, api_key):
    """
    Fetch weather data for a given city from the WeatherAPI.

    Args:
        city (str): The name of the city for which to fetch weather.
        api_key (str): The API key to authenticate the request.

    Returns:
        dict: The weather data in JSON format, or None if the request fails.
    """
    # Construct the URL for the API request using the city and API key
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    try:
        # Make a GET request to the WeatherAPI
        response = requests.get(base_url)
        
        # Raise an exception for HTTP errors (e.g., 404 or 500)
        response.raise_for_status()
        
        # Return the parsed JSON response
        return response.json()
    
    except requests.exceptions.RequestException as e:
        # Print an error message if the request fails
        print(f"Error fetching weather data: {e}")
        return None
