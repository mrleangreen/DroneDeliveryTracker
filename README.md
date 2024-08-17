# DroneDeliveryTracker
An Application That Tracks Paackages In Transit

Authors:
Tyler H
Devanna W
Project Overview
Drone Delivery Tracker is a Python-based web application that allows users to track the delivery route of a package using their "From" and "To" addresses. The application utilizes the Google Maps Geocoding API to convert addresses into coordinates and displays the delivery route on a map using the Folium library.

Features
User Input for Addresses: Users can input both the "From" and "To" addresses to visualize the route between them.
Dynamic Map Rendering: The application generates a map with the specified route, displaying markers for the starting and destination points.
Google Maps Integration: The app leverages the Google Maps Geocoding API to convert user-entered addresses into coordinates.
Flask Framework: A lightweight web application framework that handles routing and dynamic content rendering.
Requirements
Python 3.6+
Flask (Python web framework)
Requests (HTTP library for Python)
Folium (library for generating interactive maps)
Google Maps API Key
Installation
1. Clone the Repository
bash

git clone https://github.com/mrleangreen/drone-delivery-tracker.git
cd drone-delivery-tracker
3. Set Up the Virtual Environment
bash
   
python3 -m venv venv
source venv/bin/activate   # On Windows: .\venv\Scripts\activate
3. Install the Required Python Packages
bash

pip install -r requirements.txt
4. Configure the Google Maps API Key
Obtain a Google Maps API key from the Google Cloud Console.
Replace the API_KEY in the app.py file with your actual API key:
python

API_KEY = '984mil65vBjOSWEuEfvnq8NGKjHNAIW4r0BMv2vXLjw'
Usage
Run the Flask Application

bash

flask run
The application will be available at http://127.0.0.1:5000/.

Access the Web Interface

Open a web browser and go to http://127.0.0.1:5000/.
Enter the "From" and "To" addresses in the provided form.
Click "Track" to view the delivery route on the map.
Project Structure
php
Copy code
drone-delivery-tracker/
├── app.py                # Main Flask application file
├── requirements.txt      # List of required Python packages
├── templates/
│   └── index.html        # HTML template for the web interface
└── static/
    ├── css/              # CSS files for styling (if any)
    ├── js/               # JavaScript files (if any)
    └── images/           # Images used in the app (if any)
Troubleshooting
Perpetual Loading: Ensure that the API key is correctly configured and that the Flask server is running.
API Errors: If you encounter issues with the Google Maps API, double-check the API key and ensure that the API is enabled in your Google Cloud Console.
Contributions
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

License
This project is licensed under the MIT License - see the LICENSE file for details.
