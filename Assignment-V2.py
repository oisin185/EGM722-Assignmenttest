# Importing all modules needed for the script
import os
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from cartopy import crs as ccrs
from cartopy.feature import ShapelyFeature


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
ax.set_extent([xmin-1500, xmax+500, ymin-500, ymax+500], crs=belfast_utm) # Scaling the map to be 500m from the map boundary on 3 sides and 1500m on one side and setting the CRS

dea_colors = ['gold', 'royalblue', 'g', 'c', 'm', 'blueviolet', 'chocolate', 'limegreen', 'orange', 'orchid', 'maroon'] # Defining what colours the DEA wards will have
dea_names = list(dea.DEA.unique())
dea_names.sort() # Sorting by alphabetical order - This will be the order in which the wards are colourised by.

# The code block that retrieves the rows in the dea dataset
# and uses those to iterate over until the DEA boundaries are colourised -
# this is required as there are more than 1 polygon within this shapefile.
for loop, name in enumerate(dea_names):
    dea_feature = ShapelyFeature(dea.loc[dea['DEA'] == name, 'geometry'],
                          ccrs.CRS(dea.crs), # Defining the CRS so the script knows where to add the colour to
                          edgecolor='k',# Defining the visual properties of the DEA wards
                          facecolor=dea_colors[loop],
                          linewidth=1.5,
                          alpha=0.5) # Transparency of the colour
    ax.add_feature(dea_feature, zorder=2) # Adding the function to the map


# Adding the other datasets to the map and defining their appearance
# Used '.plot()' to add the bus stop, roads and rail platforms to the map with various visual appearances for each dataset
belfast_busstops.plot(ax=ax, color='navy', marker='s', markersize=2, zorder=4)
belfast_roads.plot(ax=ax, color='dimgrey', linewidth=1.5, zorder=3)
belfast_rail.plot(ax=ax, color='r', marker='s', markersize=5, zorder=5) # Added a 'zorder' ranking system to the datasets to ensure they were all visable on the map

# Generating handles for the legend
def generate_handles(labels, colors, edge='k', alpha=1): # Function 'generate_handles' used to create the handles for the legend
    lc = len(colors)
    handles = []
    for loop in range(len(labels)): # Creating loop which will iterate over the DEA wards and assign them a place on the legend
            handles.append(mpatches.Rectangle((0, 0), 1, 1, facecolor=colors[loop % lc], edgecolor=edge, alpha=alpha))
    return handles

# Defining the handles which the 'ax.legend()' function will use to add the handles to the legend
dea_handles = generate_handles(dea.DEA.unique(), dea_colors, alpha=1)
busstops_handle = generate_handles(['Bus Stops'], ['navy'])
roads_handles = [mlines.Line2D([], [], color='dimgrey')] # Different code here from the above and below lines as it is a Line geometry instead of Point
rail_handles = generate_handles(['Rail Platforms'], ['r'])

names = [] # Empty string for the Handles to occupy
for name in dea_names:
    names.append(name.title())

# Creating the legend and defining the appearance of it.
handles = dea_handles + roads_handles  + busstops_handle + rail_handles
labels = names + ['Bus Stops', 'Roads', 'Rail Platforms'] # Importing the dataset names into the legend
leg = ax.legend(handles, labels, title='Legend', title_fontsize=12, fontsize=10, loc='upper left', frameon = True, framealpha = 1) # Defining the appearance of the legend

fig.suptitle("Belfast's DEA Boundaries, Roads, Bus Stops and Rail Platforms", fontsize = 16, fontweight = 'bold') # This adds a title to the map and defines how the lettering will appear

# Inserting a scale bar into the map which measures 1000m
def scale_bar(ax, location=(0.92, 0.1), length=1000, units='m', text_offset=400):
# Defining the location of the scalebar, the length of the scalebar, the '1000m' text description so that it appears below the scalebar

    x0, x1 = ax.get_xlim()  # Get the x-axis limits
    y0, y1 = ax.get_ylim()  # Get the y-axis limits

    # Calculate the position of the scale bar
    sbx = x0 + (x1 - x0) * location[0]
    sby = y0 + (y1 - y0) * location[1]

    # Plot the scale bar
    ax.plot([sbx, sbx - length], [sby, sby], color='k', linewidth=9, transform=ax.transData)

    # Add text for the length of the scale bar
    ax.text(sbx - length / 2, sby - text_offset, f'{length} {units}', fontsize=8, ha='center')

    return ax

ax = scale_bar(ax) # Call the scale bar string

ax.gridlines(draw_labels=True, linewidth=0.5) # Add gridlines to the map and defining the appearance

plt.show() # Used this command throughout the editing phase of creating the script to ensure I could see if the data was loading correctly


# This should display a map of the Belfast DEA boundaires colourised with the above colours, the road network, the bus stops and the rail platforms within these boundaires.
# Should also display a legend with the colour to the DEA boundaires, a title with the text 'Belfast's DEA Boundaries, Roads, Bus Stops and Rail Platforms',
# a scale bar measuring 1000m, and graticules.