from flask import Flask, render_template, request
import requests
import folium

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    map_html = None
    if request.method == 'POST':
        tracking_number = request.form['tracking_number']
        # Get tracking data from API
        tracking_data = get_tracking_data(tracking_number)
        # Generate map route
        map_html = generate_map_route(tracking_data)
    return render_template('index.html', map_html=map_html)

def get_tracking_data(tracking_number):
    # Use requests to get data from your chosen package tracking API
    # Example (pseudo-code):
    response = requests.get(f'https://api.yourtrackingapi.com/{tracking_number}')
    return response.json()

def generate_map_route(tracking_data):
    # Create a map centered around the starting location
    start_location = tracking_data['locations'][0]['coordinates']
    map_route = folium.Map(location=start_location, zoom_start=10)
    # Add waypoints for each location in the tracking data
    for location in tracking_data['locations']:
        folium.Marker(location['coordinates'], popup=location['description']).add_to(map_route)
    # Save map as HTML
    return map_route._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
