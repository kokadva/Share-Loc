# Share-Loc

Share loccation

Home project


First of all i'll tell which technologies I use:

1. Docker 
2. Postgresql-Postgis
3. Geoserver
4. Openlayers
5. Python-Flask

Let's start with docker
Install docker CE (Comunity Edition) on your system, I use docker for setting up Geoserver and Postgis


To set up Postgis DB I've chosen openmaptiles/postgis docker image, for Geoserver kartoza/geoserver image.
If you are not familiar with Geoserver I suggest looking briefly into it and get some knowledge on Geo info services like WMS, WFS and etc. 
(http://geoserver.org/)

To set up Postgis-Geoserver clone this repository into your local machine and run docker-compose up in the repository folder

So now to check if everything is working go to localhost:8080/geoserver 
Log in with username: admin password: geoserver
Go to Workspaces, add workspace with name shareloc-postgis, type same in the namespace URI and submit
Go to Stores, add new store, choose PostGIS, 
  Data Source Name: test
  host: postgis
  port: 5432
  database: shareloc
  schema: <empty>
  user: shareloc
  password: shareloc
click save
There will com up a page New Layer with a table consisting of two rows, click publish of "country_osm_grid"
Scroll down to Bounding Boxes section, click Compute from data, and Compute from native bounds
Switch to Publishing section at the top and in the WMS settings, Layer settings, Default style choose polygon
Scroll down and click save
Go to Layer Preview section, a row country_osm_grid must be present, click Openlayers in Common formats columns
A map and a world map must appear, that means that you've set up postgis and geoserver correctly.
