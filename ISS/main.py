import ephem

# Create an observer object for the location you want to track the ISS from
observer = ephem.Observer()
observer.lat = '51.5074' # replace with your latitude
observer.lon = '-0.1278' # replace with your longitude
observer.elevation = 10 # replace with your elevation in meters

# Create a ISS object
iss = ephem.readtle('ISS (ZARYA)',
                    '1 25544U 98067A   22045.71223958  .00002902  00000-0  68910-4 0  9991',
                    '2 25544  51.6442  86.4123 0005461  15.6017 354.5269 15.49042424297474')

# Update the ISS object with the current time and location
observer.date = ephem.now()
iss.compute(observer)

# Print the current position of the ISS
print("ISS current position:")
print("Latitude: ", iss.sublat)
print("Longitude: ", iss.sublong)
