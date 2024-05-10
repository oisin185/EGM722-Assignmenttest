# Importing all modules needed for the script
import os
import geopandas as gpd
import matplotlib.pyplot as plt
from PIL._imaging import outline
from cartopy import crs as ccrs
from cartopy.feature import ShapelyFeature
import cartopy.feature as cfeature
from matplotlib_scalebar.scalebar import ScaleBar

# Load shapefiles needed for the script
belfast_DEA_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastDEA/Belfast_DEA.shp' # Replaced the LGD boundary with the smaller DEA boundary for greater detail
belfast_busstops_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/Belfast_busstops_V2/BelfastBusstops_V2.shp'
belfast_roads_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRoads/Belfast_Roads.shp'
belfast_rail_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRail/Belfast_RailPlatforms.shp' # Added the railway stops to the script
# Load the Belfast DEA outline, bus stop locations, railway stops and road network into GeoDataFrames which contains all the
# attributes related to the datasets

dea = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastDEA/Belfast_DEA.shp'))
belfast_busstops = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/Belfast_busstops_V2/BelfastBusstops_V2.shp'))
belfast_roads = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRoads/Belfast_Roads.shp'))
belfast_rail = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRail/Belfast_RailPlatforms.shp'))

belfast_utm = ccrs.UTM(29) # Setting the correct the Coordinate Reference System (CRS) for the map

fig = plt.figure(figsize=(15, 15)) # The boundary of the map which will be created and setting the size of 15 by 15 inches
ax = plt.axes(projection=belfast_utm) # Projecting the axes of the boundary into the correct CRS

# ShapelyFeature to use 'dea' geometry attribute, specifying the CRS and colours for the outline and background
belfast_dea_outline = ShapelyFeature(dea['geometry'], belfast_utm, edgecolor='k', facecolor='w')
ax.add_feature(belfast_dea_outline, zorder=1) # Adding the map boundary line

xmin, ymin, xmax, ymax = dea.total_bounds # Displaying the boundaries of the Belfast DEA shapefile
ax.set_extent([xmin-500, xmax+500, ymin-500, ymax+500], crs=belfast_utm) # Scaling the map to be 500m from the map boundary and setting the CRS

dea_colors = ['r', 'b', 'g', 'c', 'm', 'blueviolet', 'chocolate', 'limegreen', 'orange', 'orchid', 'maroon']
dea_names = list(dea.DEA.unique())
dea_names.sort()

for loop, name in enumerate(dea_names): # The code block that allows the program to iterate over until the DEA boundaries are colourised - this is required as there are more than 1 polygon within this shapefile.
    dea_feature = ShapelyFeature(dea.loc[dea['DEA'] == name, 'geometry'],
                          ccrs.CRS(dea.crs), # Defining the CRS so the script knows where to add the colour to
                          edgecolor='k',# Defining the visual properties of the DEA wards
                          facecolor=dea_colors[loop],
                          linewidth=1.5,
                          alpha=0.25) # Transparency of the colour (In reality this determines how vivid the colour will be)
    ax.add_feature(dea_feature, zorder=2) # Adding the function to the map

belfast_busstops.plot(ax=ax, color='navy', marker='s', markersize=2, zorder=4) # Used '.plot()' to add the bus stop, roads and rail platforms to the map with various visual appearances for each dataset
belfast_roads.plot(ax=ax, color='dimgrey', linewidth=1, zorder=3)
belfast_rail.plot(ax=ax, color='coral', marker='s', markersize=5, zorder=5) # Added a 'zorder' ranking system to the datasets to ensure they were all visable on the map

plt.show() # Used this command throughout the editing phase of creating the script to ensure I could see if the data was loading correctly