import osmnx as ox
#WEEK 2 of GITHUB
ox.config(use_cache=True, log_console=True)
gdf = ox.geometries_from_place('Piedmont, CA, USA', tags={'building':True})
fig, ax = ox.plot_footprints(gdf)
