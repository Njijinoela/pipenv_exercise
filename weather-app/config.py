from dotenv import dotenv_values

def get_api_key():
    """
    Retrieve the API key from the .env file.
    Returns:
        str: The API key if found, otherwise None.
    """
    # Load environment variables from the .env file
    config = dotenv_values(".env")
    
    # Retrieve the API key from the loaded configuration
    api_key = config.get("WEATHER_API_KEY")
    
    # Check if the API key is missing
    if not api_key:
        print("Error: API key not found. Please check your .env file.")
    
    return api_key
