import osmnx as ox

ox.config(use_cache=True, log_console=True)
gdf = ox.geometries_from_place('Piedmont, CA, USA', tags={'building':True})
fig, ax = ox.plot_footprints(gdf)