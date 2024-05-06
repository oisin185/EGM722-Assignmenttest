# import all modules needed for the script
import os
import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy import crs as ccrs
import cartopy.feature as cfeature
from matplotlib_scalebar.scalebar import ScaleBar

# Load shapefiles needed for the scirpt
belfast_lgd_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastLGD/Belfast_LGD.shp'
belfast_busstops_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastBusstop/Belfast_Busstops.shp'
belfast_roads_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRoads/Belfast_Roads.shp'

# Load the Belfast LGD outline, busstop locations and road network into GeoDataFrames which contains all the attributes related to the datasets
lgd = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastLGD/Belfast_LGD.shp'))
belfast_busstops = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastBusstop/Belfast_Busstops.shp'))
belfast_roads = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRoads/Belfast_Roads.shp'))

belfast_utm = ccrs.UTM(30) # setting the correct the Coordinate Reference System (CRS) for the map

fig = plt.figure(figsize=(10, 10)) # The boundary of the map which will be created and setting the size of 10 inches by 10 inches
axes = plt.axes(projection=belfast_utm) # Projecting the axes of the boundary into the correct CRS