from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

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

# start_date ------------------------------------------------------------


# durations ------------------------------------------------------------
datetime_durations = [datetime.strptime(time.strip(), '%H:%M:%S').time() for time in dataset[1]]
numeric_durations = [(dt.hour * 3600) + (dt.minute * 60) + dt.second for dt in datetime_durations]
mean = np.mean(numeric_durations)
print(mean)
std_dev = np.std(numeric_durations)

# Generate data points following a normal distribution
num_points = 1000
data_points = np.random.normal(mean, std_dev, num_points)
# Plot the histogram
plt.hist(numeric_durations, bins=50, density=True, alpha=0.6, label='Histogram')
# Overlay the Gaussian curve
x_values = np.linspace(np.min(numeric_durations), np.max(numeric_durations), num_points)
y_values = stats.norm.pdf(x_values, mean, std_dev)
plt.plot(x_values, y_values, 'r-', label='Gaussian Curve')
# Average
plt.axvline(mean, color='g', linestyle='--', linewidth=2, label='Average')

plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Trip Durations\n # of trips: '+str(len(dataset[1]))+' / Average: '+str(timedelta(seconds=round(float(mean)))).split(", ")[-1])
plt.legend()
plt.show()

# station_name_start ------------------------------------------------------------


# station_name_end ------------------------------------------------------------

