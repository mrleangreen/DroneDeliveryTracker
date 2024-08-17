from flask import Flask, render_template, request
import requests
import folium

app = Flask(__name__)

# Your Google Maps Geocoding API key
API_KEY = '984mil65vBjOSWEuEfvnq8NGKjHNAIW4r0BMv2vXLjw'

@app.route('/', methods=['GET', 'POST'])
def index():
    map_html = None
    if request.method == 'POST':
        from_address = request.form['from_address']
        to_address = request.form['to_address']
        
        # Get coordinates for the addresses
        from_coords = get_coordinates(from_address)
        to_coords = get_coordinates(to_address)
        
        # Generate the map with the route
        map_html = generate_map_route(from_coords, to_coords)
        
    return render_template('index.html', map_html=map_html)

def get_coordinates(address):
    response = requests.get(
        f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}'
    )
    data = response.json()
    if data['status'] == 'OK':
        return data['results'][0]['geometry']['location']
    return None

def generate_map_route(from_coords, to_coords):
    # Create a map centered at the midpoint between the two locations
    midpoint = [(from_coords['lat'] + to_coords['lat']) / 2, (from_coords['lng'] + to_coords['lng']) / 2]
    route_map = folium.Map(location=midpoint, zoom_start=12)
    
    # Add markers for "From" and "To" locations
    folium.Marker([from_coords['lat'], from_coords['lng']], popup='From Address').add_to(route_map)
    folium.Marker([to_coords['lat'], to_coords['lng']], popup='To Address').add_to(route_map)
    
    # Draw the route as a line
    folium.PolyLine(locations=[[from_coords['lat'], from_coords['lng']], [to_coords['lat'], to_coords['lng']]], color='blue').add_to(route_map)
    
    # Return the map as HTML
    return route_map._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
