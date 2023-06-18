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
# print(dataset[0])
# print(dataset[1])
# print(dataset[2])
# print(dataset[3])

# start_date ------------------------------------------------------------------------------------------------
# Rides per month / time of day / etc

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

# Obtain coordinates for each address using geocoding
from Location_to_Coordinates import location_to_coordinates
coordinates = location_to_coordinates(locations,visit_counts)
# print(coordinates)

# Create the base map using OpenStreetMap tiles
heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
# Add the heatmap layer to the base map
HeatMap(coordinates).add_to(heatmap_map)
heatmap_map.save('start_heatmap_map.html')

# station_name_end ------------------------------------------------------------------------------------------------
station_counter = Counter(list(map(str.strip, dataset[3])))
locations = list(station_counter.keys())
visit_counts = list(station_counter.values())

# Obtain coordinates for each address using geocoding
from Location_to_Coordinates import location_to_coordinates
coordinates = location_to_coordinates(locations,visit_counts)
# print(coordinates)

# Create the base map using OpenStreetMap tiles
heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
# Add the heatmap layer to the base map
HeatMap(coordinates).add_to(heatmap_map)
heatmap_map.save('end_heatmap_map.html')

# station_name_combined ------------------------------------------------------------------------------------------------
station_counter = Counter(list(map(str.strip, dataset[2]+dataset[3])))
locations = list(station_counter.keys())
visit_counts = list(station_counter.values())

# Obtain coordinates for each address using geocoding
from Location_to_Coordinates import location_to_coordinates
coordinates = location_to_coordinates(locations,visit_counts)
# print(coordinates)

# Create the base map using OpenStreetMap tiles
heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
# Add the heatmap layer to the base map
HeatMap(coordinates).add_to(heatmap_map)
heatmap_map.save('combined_heatmap_map.html')
