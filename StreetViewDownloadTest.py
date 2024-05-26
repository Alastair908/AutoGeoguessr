import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("API key not found. Make sure it is set in the .env file.")

def download_photosphere(location, heading, pitch, key, file_name):
    url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "size": "640x640",  # Max size is 640x640 for free tier
        "location": location,
        "heading": heading,
        "pitch": pitch,
        "key": key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {file_name}, status code: {response.status_code}")
        print(response.text)  # Print the response text for more details

# Verify that the API key is loaded correctly
print(f"Using API Key: {api_key}")

# Example usage
download_photosphere("46.414382,10.013988", 0, 0, api_key, "photosphere.jpg")

# List of locations to download photospheres from
locations = [
    "46.414382,10.013988",
    "48.858844,2.294351",
    # Add more locations as needed
]

for idx, location in enumerate(locations):
    file_name = f"photosphere_{idx}.jpg"
    download_photosphere(location, 0, 0, api_key, file_name)

