import json
import pandas as pd
import requests

def location_to_coordinates(locations, visit_counts):
    # Query All Station Data
    r = requests.get('https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information')
    bikeshare_stations = json.loads(r.content)['data']['stations']
    bikeshare_stations = pd.DataFrame(bikeshare_stations)[['name', 'lat', 'lon']]
    bikeshare_stations.to_csv('Outputs/bikeshare_stations.csv', index=False)

    # In case the station no longer exists, maybe it existed in 2019
    bikeshare_stations_historical = pd.read_csv('Outputs/bikeshare_stations_historical_2019.csv')

    coordinates = []
    for location, visit_count in zip(locations,visit_counts):
        try:
            result = bikeshare_stations.loc[bikeshare_stations['name'] == location, ['lat', 'lon']]
            coordinates.append((result['lat'].iloc[0], result['lon'].iloc[0], visit_count))
        except:
            try:
                result = bikeshare_stations_historical.loc[bikeshare_stations_historical['name'] == location, ['lat', 'lon']]
                coordinates.append((result['lat'].iloc[0], result['lon'].iloc[0], visit_count))
            except:
                print('"' + str(location) + '" : "",')

    print(str(len(coordinates))+" out of "+str(len(locations))+" coordinates found")
    return(coordinates)