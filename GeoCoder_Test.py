from geopy import Nominatim

geolocator = Nominatim(user_agent='heatmap_example')
address = 'Kew Beach Ave / Kenilworth Ave'
# parts = address.split('/')
# address = (parts[1] + " / " + parts[0]).strip()
# print(address)
location = geolocator.geocode(address)
print('the coordinates for '+str(address)+' are '+str(location))

# the coordinate for Spadina Ave / Sussex Ave are Spadina Ave & Sussex, Spadina Avenue, University—Rosedale, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5S 2T9, Canada
# the coordinate for Spadina Ave / Harbord St are Harbord Street, Spadina Avenue, University—Rosedale, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5S 1G2, Canada
# the coordinate for Soho St / Queen St W are Soho St / Queen St W, Soho Street, Spadina—Fort York, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5V 2A1, Canada
# the coordinate for St. Patrick St / Dundas St W are St. Patrick, Dundas Street West, Spadina—Fort York, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5G 1Y8, Canada
# the coordinate for Fort York Blvd / Garrison Rd are None
# the coordinate for Garrison Rd / Fort York Blvd are None
# the coordinate for Bathurst St / Fort York Blvd are Bathurst St & Fort York Blvd, Fort York Boulevard, Spadina—Fort York, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5V 0E7, Canada
# the coordinate for St. George St / Bloor St W are St George St & Bloor St W, St George Street, University—Rosedale, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5S 2E9, Canada
# the coordinate for Cherry Beach are Cherry Beach, Toronto—Danforth, Old Toronto, Toronto, Golden Horseshoe, Ontario, Canada
# the coordinate for Tommy Thompson Park (Leslie Street Spit) are Tommy Thompson Park, Leslie Street Spit Trail, Toronto—Danforth, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5A 1A1, Canada
# the coordinate for Kew Beach Ave / Kenilworth Ave are None
# the coordinate for Kenilworth Ave / Kew Beach Ave are None
# the coordinate for Danforth Ave / Ellerbeck St are None
# the coordinate for Ellerbeck St / Danforth Ave are None
# the coordinate for Wellington St W / York St are York Street, Wellington Street West, Financial District, Spadina—Fort York, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5K 1H6, Canada
# the coordinate for Spadina Ave / Sullivan St are Sullivan Street, Spadina Avenue, Spadina—Fort York, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5T 2C2, Canada
# the coordinate for King St W / Portland St are Portland Street, King Street West, Spadina—Fort York, Old Toronto, Toronto, Golden Horseshoe, Ontario, M5V 1M3, Canada
# the coordinate for Coronation Park (Martin Goodman Trail) are None
# the coordinate for Housey St / Dan Leckie Way are None
# the coordinate for Dan Leckie Way / Housey St are None