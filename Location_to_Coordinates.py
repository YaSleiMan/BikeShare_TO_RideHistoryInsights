from geopy import Nominatim

def location_to_coordinates(locations, visit_counts):
    coordinate_dict = {
        "Fort York Blvd / Garrison Rd":"43.63739613451603, -79.40612171600311",
        "Kew Beach Ave / Kenilworth Ave":"43.66633047663169, -79.30140222538206",
        "Danforth Ave / Ellerbeck St": "43.67671389584629, -79.35643003310071",
        "Coronation Park (Martin Goodman Trail)": "43.63558375535192, -79.4035811953714",
        "Housey St / Dan Leckie Way": "43.638155708522774, -79.3975186737966",
        "D'Arcy St / McCaul St": "43.65532958729307, -79.39185752239844",
        "University Ave / Richmond St W": "43.65013976200553, -79.38611012416523"
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
        # print('the coordinate for '+str(location)+' are '+str(coordinate))

        # Try Again (Flipping streets)
        if coordinate is None:
            try:
                parts = location.split('/')
                coordinate = geolocator.geocode((parts[1] + " / " + parts[0]).strip())
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
                print('"' + str(location) + '" : "",')
                pass

        # Exit
        if coordinate is not None:
            if check == 0:
                # print(str(coordinate.latitude)+" / "+str(coordinate.longitude))
                coordinates.append((coordinate.latitude, coordinate.longitude,visit_count))
            elif check == 1:
                check = 0
                coordinate_latitude = float(coordinate.split(',')[0])
                coordinate_longitude = float(coordinate.split(',')[1])
                coordinates.append((coordinate_latitude, coordinate_longitude,visit_count))

    print(str(len(coordinates))+" out of "+str(len(locations))+" coordinates found")
    return(coordinates)