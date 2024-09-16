import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from data import number

# Parse the phone number
check_number = phonenumbers.parse(number)

time = timezone.time_zones_for_number(check_number)
print("time:", time)
# Get the location of the phone number (country or city)
number_location = geocoder.description_for_number(check_number, "en")
print("Location:", number_location)

# Get the carrier of the phone number
number_carrier = carrier.name_for_number(check_number, "en")
print("Carrier:", number_carrier)

# Use OpenCage Geocode API to get latitude and longitude of the location
key = "50aa3091d69e4ec181e1ee39b526afba"  # Your OpenCage API key
geocoder = OpenCageGeocode(key)

# Query the location name from the phone number geocoder
query = str(number_location)
results = geocoder.geocode(query)

if results and len(results) > 0:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map centered at the location
    map_location = folium.Map(location=[lat, lng], zoom_start=9)

    # Add a marker at the location
    folium.Marker([lat, lng], popup=number_location).add_to(map_location)

    # Save the map to an HTML file
    map_location.save("location.html")
    print("Map saved as location.html")
else:
    print("Location not found in OpenCage Geocoder.")
