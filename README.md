# TorontoBikeShare_RideHistoryQuery
The Bike Share website only lets you look at a limited number of past trips at a time in the history section. This automation is used to obtain your full trip history and visualize that data much more easily.

# How to Use
1- Fill the login info and start/end dates in the Selenium_GetData.py file and run. This will download all your trip data and then save it as txt file which will be used in the next steps

2- Run the Present_Data.py file, this should create 3 graphs and 3 heatmaps that summarize data such as:

    2.1- (Graph) During what times of the day do the trip start
    
    2.2- (Graph) How many rides are taken each month
    
    2.3- (Graph) How long are the rides
    
    2.4- (Heatmap) Where do the rides start
    
    2.5- (Heatmap) Where do the rides end
    
    2.6- (Heatmap) Where have the rides taken you
    
3- The files should all show up in the outputs folder. The graphs as pictures and the heatmap as html that can be viewed in your browser (tested with Chrome)
