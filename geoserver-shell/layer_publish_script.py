from geoserver import GeoserverShell

workspace = 'shareloc'
store = 'shareloc-postgis'
rest_url = "http://localhost:8080/geoserver/rest/"

postgis_host = 'postgis'
port = '5432'
database = 'shareloc'
user = 'shareloc'
password = 'shareloc'
db_type = 'postgis'
layer_name = 'country_osm_grid'

g = GeoserverShell(rest_url)
g.create_workspace(workspace)
g.create_store(workspace, store, postgis_host, port, database, user, password, db_type)
g.publish_layer(workspace, store, layer_name)
