import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",48, -100],
          ["Boston", 49, -90]]
scale = 5

map = Basemap(llcrnrlon=-125,llcrnrlat=25,urcrnrlon=-65,urcrnrlat=50,
#        projection='lcc',lat_1=32,lat_2=45,lon_0=-95)
	projection = 'lcc', resolution = 'l', lat_0=38, lon_0=-98)

map.drawstates()
map.drawcoastlines()
map.drawcountries()

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='Red')
plt.show()
