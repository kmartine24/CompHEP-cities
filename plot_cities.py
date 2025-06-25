import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

cities = [["Chicago",41.881832, -87.623177],
          ["Boston", 42.355083, -71.065880],
          ["Madison", 43.073051, -89.401230],
          ["Austin", 30.266666, -97.733330],
          ["Knoxville", 35.964668, -83.926453],
	  ["Urbana-Champaign", 40.1106, 88.2073]]
scale = 5

map = Basemap(llcrnrlon=-125,llcrnrlat=25,urcrnrlon=-65,urcrnrlat=50,
	width=5000000,height=12000000,
	projection = 'lcc', resolution = 'l', lat_0=5, lon_0=-98)

map.drawstates()
map.drawcoastlines()
map.drawcountries()

#sets ocean color
map.drawlsmask(land_color=(0, 0, 0, 0), ocean_color='xkcd:lightblue', lakes=True)

# Get the location of each city and plot it
for (city, latitude, longitude) in cities:
    x, y = map(longitude, latitude)
    map.plot(x, y, marker='o',color='plum')
plt.show()
