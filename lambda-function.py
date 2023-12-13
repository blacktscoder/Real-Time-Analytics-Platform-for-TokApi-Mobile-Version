import http.client
import json
import urllib.parse  # Add this import

def fetch_data_from_api(location_id):
    conn = http.client.HTTPSConnection("tokapi-mobile-version.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "#",
        'X-RapidAPI-Host': "tokapi-mobile-version.p.rapidapi.com"
    }

    # Use urllib.parse.quote to properly encode the city code in the URL
    encoded_city_code = urllib.parse.quote(location_id)
    
    conn.request("GET", f"/v1/location/{location_id}", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def process_data(location_id):
    api_response = fetch_data_from_api(location_id)
    process_result(api_response)

def process_result(data):
    # Extract and print relevant information (city code, formatted address, video count)
    response_data = json.loads(data)
    city_code = response_data.get("city_code", "")
    formatted_address = response_data.get("formatted_address", "")
    video_count = response_data.get("video_count", 0)

    print(f"City Code: {city_code}")
    print(f"Formatted Address: {formatted_address}")
    print(f"Video Count: {video_count}")

# Test the function with a sample city code
sample_city_code = "22535796485353377"
process_data(sample_city_code)
