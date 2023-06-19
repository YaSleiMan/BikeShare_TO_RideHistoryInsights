from geopy import Nominatim

def location_to_coordinates(locations, visit_counts):
    # Hardcoded Values
    coordinate_dict = {
        "Fort York Blvd / Garrison Rd":"43.63739613451603, -79.40612171600311",
        "Kew Beach Ave / Kenilworth Ave":"43.66633047663169, -79.30140222538206",
        "Danforth Ave / Ellerbeck St": "43.67671389584629, -79.35643003310071",
        "Coronation Park (Martin Goodman Trail)": "43.63558375535192, -79.4035811953714",
        "Housey St / Dan Leckie Way": "43.638155708522774, -79.3975186737966",
        "D'Arcy St / McCaul St": "43.65532958729307, -79.39185752239844",
        "University Ave / Richmond St W": "43.65013976200553, -79.38611012416523",
        "Berkeley St / Adelaide St E": "43.653339189811796, -79.36496897399171",
        "111 Bond St (North of Dundas St E) ": "43.65690292756406, -79.37854144306614",
        "Dalton Rd / Bloor St W": "43.66611012212478, -79.40667964746912",
        "King St W / Jordan St": "43.648991509352406, -79.37863025118989",
        "Princess St / Adelaide St E": "43.65240097833613, -79.36738658196664",
        "Queens Quay E / Lower Sherbourne St": "43.64516208005284, -79.36546389057112",
        "Hubbard Blvd. / Glen Manor Dr.": "43.66874924814692, -79.29138409914165",
        "Strachan Ave / Princes' Blvd": "43.6348661579098, -79.40907311509858",
        "Dundas St E / Pembroke St": "43.65819629206575, -79.37237783154258",
        "Bathurst St / Adelaide St W": "43.644871753471605, -79.40304417522952"
    }

    # Obtain coordinates for each address using geocoding
    geolocator = Nominatim(user_agent='heatmap_example')
    coordinates = []
    check = 0
    for location, visit_count in zip(locations,visit_counts):
        # Cleanup
        if location.endswith(' - SMART'):
            location = location[:-len(' - SMART')]
        elif location.endswith(' -SMART'):
            location = location[:-len(' -SMART')]
        elif location.endswith(' SMART'):
            location = location[:-len(' SMART')]

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

        print(location)

    print(str(len(coordinates))+" out of "+str(len(locations))+" coordinates found")
    return(coordinates)