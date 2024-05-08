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
belfast_busstops_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastBusstop/Belfast_Busstops.shp'
belfast_roads_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRoads/Belfast_Roads.shp'
belfast_rail_shapefile = 'C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRail/Railplatforms.shp' # Added the railway stops to the script
# Load the Belfast DEA outline, bus stop locations, railway stops and road network into GeoDataFrames which contains all the
# attributes related to the datasets

dea = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastDEA/Belfast_DEA.shp'))
belfast_busstops = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastBusstop/Belfast_Busstops.shp'))
belfast_roads = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRoads/Belfast_Roads.shp'))
belfast_rail = gpd.read_file(os.path.abspath('C:/Users/oisin/Documents/GitHub/EGM722-Assignmenttest/BelfastRail/Railplatforms.shp'))

belfast_utm = ccrs.UTM(30) # Setting the correct the Coordinate Reference System (CRS) for the map

fig = plt.figure(figsize=(15, 15)) # The boundary of the map which will be created and setting the size of 15 by 15 inches
axes = plt.axes(projection=belfast_utm) # Projecting the axes of the boundary into the correct CRS

# ShapelyFeature to use 'dea' geometry attribute, specifying the CRS and colours for the outline and background
belfast_dea_outline = ShapelyFeature(dea['geometry'], belfast_utm, edgecolor='k', facecolor='w')
axes.add_feature(belfast_dea_outline) # Adding the map boundary line

xmin, ymin, xmax, ymax = dea.total_bounds # Displaying the boundaries of the Belfast LGD shapefile
axes.set_extent([xmin-500, xmax+500, ymin-500, ymax+500], crs=belfast_utm) # Scaling the map to be 500m from the map boundary and setting the CRS

dea_colors = ['r', 'b', 'g', 'c', 'm', 'blueviolet', 'chocolate', 'limegreen', 'orange', 'orchid', 'maroon']
dea_names = list(dea.DEA.unique())
dea_names.sort()

for ii, name in enumerate(dea_names): # The code block that allows the program to iterate over until the DEA boundaries are colourised - this is required as there are more than 1 polygon within this shapefile.
    dea_colourise = ShapelyFeature(dea.loc[dea['DEA'] == name, 'geometry'],
                          ccrs.CRS(dea.crs), # Defining the CRS so the script knows where to add the colour to
                          edgecolor='k',# Defining the visual properties of the DEA wards
                          facecolor=dea_colors[ii],
                          linewidth=1.5,
                          alpha=0.6) # Transparency of the colour (In reality this determines how vivid the colour will be)
    axes.add_feature(dea_colourise) # Adding the function to the map

plt.show() # Used this command throughout the editing phase of creating the script to ensure I could see if the data was loading correctly