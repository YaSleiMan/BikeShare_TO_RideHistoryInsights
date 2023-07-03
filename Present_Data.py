from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from collections import Counter
import folium
from folium.plugins import HeatMap

def present_data():
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

    # Generate Graphs and Heatmaps
    time_of_day(dataset[0])
    rides_per_month(dataset[0])
    ride_durations(dataset[1])
    station_name_start(dataset[2])
    station_name_end(dataset[3])
    station_name_combined(dataset[2]+dataset[3])

def time_of_day(dataset):
    # Time of day
    datetime_time = [datetime.strptime(time.strip(), '%m-%d-%Y %H:%M:%S').time() for time in dataset]
    numeric_durations = [(dt.hour * 3600) + (dt.minute * 60) + dt.second for dt in datetime_time]
    mean = np.mean(numeric_durations)
    std_dev = np.std(numeric_durations)
    min = np.min(numeric_durations)
    max = np.max(numeric_durations)

    # Generate data points following a normal distribution
    num_points = 1000
    data_points = np.random.normal(mean, std_dev, num_points)
    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(numeric_durations, bins=24*3, density=True, alpha=0.6, label='Histogram')
    # Overlay the Gaussian curve
    x_values = np.linspace(0, 24*3600, num_points)
    y_values = stats.norm.pdf(x_values, mean, std_dev)
    plt.plot(x_values, y_values, 'r-', label='Gaussian Curve')
    plt.xticks([0,6*3600,12*3600,18*3600,24*3600],['0:00','6:00','12:00','18:00','24:00'])
    # Average
    plt.axvline(mean, color='g', linestyle='--', linewidth=2, label='Average')

    plt.xlabel('Time of Day')
    plt.ylabel('Frequency')
    plt.title('Trip Start Times\n\
     # of trips: '+str(len(dataset))+' / Average: '+str(timedelta(seconds=round(float(mean)))).split(", ")[-1]+'\n\
     Earliest Ride: '+str(timedelta(seconds=round(float(min)))).split(", ")[-1]+' / Latest Ride: '+str(timedelta(seconds=round(float(max)))).split(", ")[-1])
    plt.legend()
    plt.savefig('Outputs/TimeOfDayHist.png')
    plt.show()
    plt.close()

def rides_per_month(dataset):
    datetime_months = [datetime.strptime(time.strip(), '%m-%d-%Y %H:%M:%S').month for time in dataset]
    numeric_durations = datetime_months

    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(numeric_durations, bins=12, label='Histogram',width=0.85)
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December']
    plt.xticks(np.linspace(1, 12, 12),months,rotation=45)

    starting_month = numeric_durations[0]
    plt.axvline(x=starting_month, color='r', linestyle='--', label='Starting Month\n2022 (right) / 2023 (left)')

    plt.xlabel('Months')
    plt.ylabel('Frequency')
    plt.title('Rides per Month\n# of trips: '+str(len(dataset)))
    plt.legend()
    plt.savefig('Outputs/RidesPerMonthHist.png')
    plt.show()
    plt.close()

def ride_durations(dataset):
    datetime_durations = [datetime.strptime(time.strip(), '%H:%M:%S').time() for time in dataset]
    numeric_durations = [(dt.hour * 3600) + (dt.minute * 60) + dt.second for dt in datetime_durations]
    mean = np.mean(numeric_durations)
    std_dev = np.std(numeric_durations)
    min = np.min(numeric_durations)
    max = np.max(numeric_durations)
    total = str(timedelta(seconds=round(float(sum(numeric_durations)))))

    # Generate data points following a normal distribution
    num_points = 1000
    data_points = np.random.normal(mean, std_dev, num_points)
    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.hist(numeric_durations, bins=50*2, density=True, alpha=0.6, label='Histogram')
    # Overlay the Gaussian curve
    x_values = np.linspace(np.min(numeric_durations), np.max(numeric_durations), num_points)
    y_values = stats.norm.pdf(x_values, mean, std_dev)
    plt.plot(x_values, y_values, 'r-', label='Gaussian Curve')
    plt.xticks([0,6*60,12*60,18*60,24*60,30*60,36*60,42*60],['0:00','6:00','12:00','18:00','24:00','30:00','36:00','42:00'])
    # Average
    plt.axvline(mean, color='g', linestyle='--', linewidth=2, label='Average')

    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.title('Trip Durations\n\
     # of trips: '+str(len(dataset))+' / Total Ride Time: '+total+' / Average: '+str(timedelta(seconds=round(float(mean)))).split(", ")[-1]+'\n\
     Shortest Ride: '+str(timedelta(seconds=round(float(min)))).split(", ")[-1]+' / Longest Ride: '+str(timedelta(seconds=round(float(max)))).split(", ")[-1])
    plt.legend()
    plt.savefig('Outputs/RidesDurationsHist.png')
    plt.show()
    plt.close()

def station_name_start(dataset):
    station_counter = Counter(list(map(str.strip, dataset)))
    locations = list(station_counter.keys())
    visit_counts = list(station_counter.values())
    z_scores = (visit_counts - np.mean(visit_counts)) / np.std(visit_counts)
    threshold = 2
    outlier_indices = np.where(np.abs(z_scores) > threshold)[0]
    outliers = [visit_counts[i] for i in outlier_indices]
    for i in range(len(visit_counts)):
        if z_scores[i]>threshold:
            visit_counts[i] = min(outliers)
    # print(min(outliers))
    # print(visit_counts)

    # Obtain coordinates for each address using geocoding
    from Location_to_Coordinates import location_to_coordinates
    coordinates = location_to_coordinates(locations,visit_counts)
    # print(coordinates)

    # Create the base map using OpenStreetMap tiles
    heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
    # Add the heatmap layer to the base map
    HeatMap(coordinates).add_to(heatmap_map)
    heatmap_map.save('Outputs/start_heatmap_map.html')

def station_name_end(dataset):
    # station_name_end ------------------------------------------------------------------------------------------------
    station_counter = Counter(list(map(str.strip, dataset)))
    locations = list(station_counter.keys())
    visit_counts = list(station_counter.values())
    z_scores = (visit_counts - np.mean(visit_counts)) / np.std(visit_counts)
    threshold = 2
    outlier_indices = np.where(np.abs(z_scores) > threshold)[0]
    outliers = [visit_counts[i] for i in outlier_indices]
    for i in range(len(visit_counts)):
        if z_scores[i] > threshold:
            visit_counts[i] = min(outliers)
    # print(min(outliers))
    # print(visit_counts)

    # Obtain coordinates for each address using geocoding
    from Location_to_Coordinates import location_to_coordinates
    coordinates = location_to_coordinates(locations,visit_counts)
    # print(coordinates)

    # Create the base map using OpenStreetMap tiles
    heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
    # Add the heatmap layer to the base map
    HeatMap(coordinates).add_to(heatmap_map)
    heatmap_map.save('Outputs/end_heatmap_map.html')

def station_name_combined(dataset):
    station_counter = Counter(list(map(str.strip, dataset)))
    locations = list(station_counter.keys())
    visit_counts = list(station_counter.values())
    z_scores = (visit_counts - np.mean(visit_counts)) / np.std(visit_counts)
    threshold = 2
    outlier_indices = np.where(np.abs(z_scores) > threshold)[0]
    outliers = [visit_counts[i] for i in outlier_indices]
    for i in range(len(visit_counts)):
        if z_scores[i] > threshold:
            visit_counts[i] = min(outliers)
    # print(min(outliers))
    # print(visit_counts)

    # Obtain coordinates for each address using geocoding
    from Location_to_Coordinates import location_to_coordinates
    coordinates = location_to_coordinates(locations,visit_counts)
    # print(coordinates)

    # Create the base map using OpenStreetMap tiles
    heatmap_map = folium.Map(location=coordinates[0][0:2], zoom_start=12, tiles='OpenStreetMap')
    # Add the heatmap layer to the base map
    HeatMap(coordinates).add_to(heatmap_map)
    heatmap_map.save('Outputs/combined_heatmap_map.html')


#-----------------------------------------------------
# Test the code
# present_data()
#-----------------------------------------------------