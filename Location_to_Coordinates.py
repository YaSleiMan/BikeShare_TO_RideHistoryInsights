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
        "Bathurst St / Adelaide St W": "43.644871753471605, -79.40304417522952",
        "Bremner Blvd / Rees St": "43.64099114188913, -79.38776886173602",
        "King St W / Bay St (West Side)": "43.64854585487397, -79.38090593290008",
        "Front St W / University Ave (2)": "43.645224830874064, -79.38319791722124",
        "King St W / Bay St (East Side)": "43.64873517436065, -79.37961624630012",
        "Bay St / Queens Quay W (Ferry Terminal)": "43.64118243343749, -79.3768608743376",
        "Bay St / Bloor St W (East Side)": "43.64161246574678, -79.3754182841772",
        "Front St W / Bay St (North Side)": "43.64172871936933, -79.37709286336468",
        "Bay St / College St (East Side)": "43.66045454260344, -79.38550593841289",
        "Baldwin St / Spadina Ave": "43.65493557358157, -79.39869213994943",
        "Toronto Eaton Centre (Yonge St)": "43.65611690458023, -79.38161080753405",
        "Ursula Franklin St / St. George St": "43.660438420267894, -79.39693272085542",
        "Ursula Franklin St / Huron St": "43.66009523286462, -79.39868570406395",
        "Kewbeach Ave / Kenilworth Ave": "43.666616252698816, -79.30059532683305",
        "Fort York  Blvd / Capreol Ct": "43.639874571108564, -79.39563486173606",
        "Alton Ave / Dundas St E (Greenwood Park)": "43.66745738887322, -79.32940389141045",
        "Spadina Ave / Blue Jays Way": "43.64140372780608, -79.39319906173591",
        "East Liberty St / Western Battery Rd": "43.63916584218743, -79.41141587522984",
        "Gould St / Yonge St (TMU)": "43.65748307629533, -79.3810135942689",
        "Elm St/ University Ave (East Side)": "43.65646866092935, -79.38791808040006",
        "D'Arcy St / Spadina Ave": "43.65393453375615, -79.3983147057624",
        "Richmond St E / Jarvis St Green P": "43.65267522851995, -79.37409513697031",
        "York St / Lake Shore Blvd W": "43.64163506354045, -79.3809951194067",
        "Richmond St W / York St": "43.650449871107995, -79.38457274639377",
        "Ontario St / Adelaide St E": "43.65341869886721, -79.36650162714241"
    }

    # Obtain coordinates for each address using geocoding
    geolocator = Nominatim(user_agent='heatmap_example')
    coordinates = []
    for location, visit_count in zip(locations,visit_counts):
        # Cleanup
        if location.endswith(' - SMART'):
            location = location[:-len(' - SMART')]
        elif location.endswith(' -SMART'):
            location = location[:-len(' -SMART')]
        elif location.endswith(' SMART'):
            location = location[:-len(' SMART')]

        # Overwrite Geolocator / In Case Geolocator Fails
        if location in coordinate_dict:
            coordinate = coordinate_dict[location]
            # print('the coordinate for ' + str(location) + ' are ' + str(coordinate))

            coordinate_latitude = float(coordinate.split(',')[0])
            coordinate_longitude = float(coordinate.split(',')[1])
            coordinates.append((coordinate_latitude, coordinate_longitude, visit_count))

        else:
            # Find coordinates
            try:
                coordinate = geolocator.geocode(location)
            except:
                coordinate = None
            # print('the coordinate for '+str(location)+' are '+str(coordinate))

            # Try Again (Flipping streets)
            if coordinate is None:
                try:
                    parts = location.split('/')
                    coordinate = geolocator.geocode((parts[1] + " / " + parts[0]).strip())
                    # print('the coordinate for ' + str(location) + ' are ' + str(coordinate))
                except:
                    pass

            # Exit
            if coordinate is not None:
                # print(str(coordinate.latitude)+" / "+str(coordinate.longitude))
                coordinates.append((coordinate.latitude, coordinate.longitude,visit_count))

            if coordinate is None:
                print('"' + str(location) + '" : "",')

    print(str(len(coordinates))+" out of "+str(len(locations))+" coordinates found")
    return(coordinates)