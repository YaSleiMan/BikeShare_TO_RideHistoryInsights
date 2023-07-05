import json
import pandas as pd
import requests

r = requests.get('https://tor.publicbikesystem.net/ube/gbfs/v1/en/station_information')
bikeshare_stations = json.loads(r.content)['data']['stations']
bikeshare_stations = pd.DataFrame(bikeshare_stations)[['name', 'lat', 'lon']]

result = bikeshare_stations.loc[bikeshare_stations['name'] == 'Berkeley St / Adelaide St E - SMART', ['lat', 'lon']]
print(result['lat'].iloc[0])