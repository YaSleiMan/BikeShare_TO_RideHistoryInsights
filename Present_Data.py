from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from collections import Counter
from wordcloud import WordCloud
import folium
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
import requests

# Read the text file and convert it into a list of lists
dataset = []
with open('list_file.txt', 'r') as file:
    for line in file:
        elements = line.strip().split(',')
        dataset.append(elements)
print(dataset[0])
print(dataset[1])
print(dataset[2])
print(dataset[3])

# start_date ------------------------------------------------------------------------------------------------


# durations ------------------------------------------------------------------------------------------------
# datetime_durations = [datetime.strptime(time.strip(), '%H:%M:%S').time() for time in dataset[1]]
# numeric_durations = [(dt.hour * 3600) + (dt.minute * 60) + dt.second for dt in datetime_durations]
# mean = np.mean(numeric_durations)
# std_dev = np.std(numeric_durations)
# min = np.min(numeric_durations)
# max = np.max(numeric_durations)
#
# # Generate data points following a normal distribution
# num_points = 1000
# data_points = np.random.normal(mean, std_dev, num_points)
# # Plot the histogram
# plt.hist(numeric_durations, bins=50, density=True, alpha=0.6, label='Histogram')
# # Overlay the Gaussian curve
# x_values = np.linspace(np.min(numeric_durations), np.max(numeric_durations), num_points)
# y_values = stats.norm.pdf(x_values, mean, std_dev)
# plt.plot(x_values, y_values, 'r-', label='Gaussian Curve')
# # Average
# plt.axvline(mean, color='g', linestyle='--', linewidth=2, label='Average')
#
# plt.xlabel('Time')
# plt.ylabel('Frequency')
# plt.title('Trip Durations\n\
#  # of trips: '+str(len(dataset[1]))+' / Average: '+str(timedelta(seconds=round(float(mean)))).split(", ")[-1]+'\n\
#  Shortest Ride: '+str(timedelta(seconds=round(float(min)))).split(", ")[-1]+' / Longest Ride: '+str(timedelta(seconds=round(float(max)))).split(", ")[-1])
# plt.legend()
# plt.show()

# station_name_start ------------------------------------------------------------------------------------------------
station_counter = Counter(list(map(str.strip, dataset[2])))
locations = list(station_counter.keys())
visit_counts = list(station_counter.values())

coordinate_dict = {
    "Fort York Blvd / Garrison Rd":"43.63739613451603, -79.40612171600311",
    "Kew Beach Ave / Kenilworth Ave":"43.66633047663169, -79.30140222538206"
}

# Obtain coordinates for each address using geocoding
geolocator = Nominatim(user_agent='heatmap_example')
coordinates = []
check = 0
for location, visit_count in zip(locations,visit_counts):
    # Cleanup
    if location.endswith(' - SMART'):
        location = location[:-len(' - SMART')]
    # Find coordinates
    coordinate = geolocator.geocode(location)
    print('the coordinate for '+str(location)+' are '+str(coordinate))
    # Try Again
    if coordinate is None:
        try:
            parts = location.split('/')
            location = (parts[1] + " / " + parts[0]).strip()
            coordinate = geolocator.geocode(location)
            # print('the coordinate for ' + str(location) + ' are ' + str(coordinate))
        except:
            pass
    # Hard code the coordinates
    if coordinate is None:
        try:
            coordinate = coordinate_dict[location]
            check = 1
            # print('the coordinate for ' + str(location) + ' are ' + str(coordinate))
        except:
            pass
    # Exit
    if coordinate is not None:
        if check == 0:
            # print(str(coordinate.latitude)+" / "+str(coordinate.longitude))
            # coordinates.append((coordinate.latitude, coordinate.longitude,visit_count))
        elif check == 1:
            check = 0
            coordinate_latitude = float(coordinate.split(',')[0].trim())
            coordinate_longitude = float(coordinate.split(',')[1].trim())
            coordinates.append((coordinate_latitude, coordinate_longitude, visit_count))

# Create the base map using OpenStreetMap tiles
heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
# Add the heatmap layer to the base map
HeatMap(coordinates).add_to(heatmap_map)
heatmap_map.save('heatmap_map.html')

# station_name_end ------------------------------------------------------------------------------------------------

