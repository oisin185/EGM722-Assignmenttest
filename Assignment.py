import os
import earthaccess
import geopandas as gpd
import rasterio as rio
import rasterio.merge
import shapely

belfast_lgd = gpd.read_file('C:/Users/oisin/Documents/Ulster_Uni/Semsester_2/Programming_for_GIS/LGD_Belfast').to_crs(epsg=4326)

# gets a single polygon (or multipolygon) composed of the individual polygons
outline = belfast_lgd['geometry'].unary_union

outline # note that in a jupyter notebook, this actually displays the polygon.
outline.bounds # get the min x, min y, max x, max y values of the polygon

# gets the minimum rotated rectangle that covers the outline
search_area = outline.minimum_rotated_rectangle

search_area # again, in a jupyter notebook, this displays the polygon