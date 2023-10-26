# Bike Share Toronto: Ride History Insights
The Bike Share website only lets you look at a limited number of past trips at a time in the history section. This automation is used to obtain your full trip history and visualize that data much more easily.

<img width="630" alt="pic" src="https://github.com/YaSleiMan/BikeShare_TO_RideHistoryInsights/assets/35861751/982206ab-8528-4c68-9886-94dc86f393b7">

# How to Use
1- Run the main.py function, this will open a GUI. Fill with login info and start/end dates and run. This will download all your trip data and then save it as txt file which will be used in the next steps

2- Run the Present_Data.py file, this should create 3 graphs and 3 heatmaps that summarize data such as:

    2.1- (Graph) During what times of the day do the trip start
    
    2.2- (Graph) How many rides are taken each month
    
    2.3- (Graph) How long are the rides
    
    2.4- (Heatmap) Where do the rides start
    
    2.5- (Heatmap) Where do the rides end
    
    2.6- (Heatmap) Where have the rides taken you
    
3- The files should be saved in the outputs folder. The graphs will display as pictures but the heatmaps are html and need to be viewed in your browser (tested with Chrome)

# Current Objectives:

- ~~The geocoder used for the heatmap is incorrectly placing some locations in other countries. Considering how many values currently have to be hardcoded perhaps another method of obtaining the coordinates should be used.~~ Major improvement to accuracy after figuring out (sorta) how to use the bike system's API to get data on all stations, it still isn't 100% accurate however due to the current query not giving data on stations that no longer exist, mitigated this issue partially by finding old dataset from 2019, this needs to be fully fixed however
- ~~The heat values associated with the coordinates may not be fully lining up, need to look into that.~~ ~~The values are lining up correctly but the number of times each station is visited can range dramatically so due to the scaling used only one point is highlighted red when zooming in while all the others seem blue despite still being visited a significant number of times.~~
- ~~A frontend UI could be interesting to add to this code, for the login info and start/end dates~~
- ~~Add a cost savings calculation function to estimate how much money was saved by riding bikes instead of using the TTC.~~ ~~Forgot to account for the cost of ebike rides, needs an update.~~
- Add statistics about: environmental benefits / calories burned / time saved / etc.
- ~~Line up the bars of the histogram correctly with the x-axis in the rides per month graph~~
- Make a website?
