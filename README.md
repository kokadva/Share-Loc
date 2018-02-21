# Share-Loc

## Share loccation

### Home project


Technologies used in the project:

```
1. Docker
2. Postgresql + Postgis
3. Geoserver
4. Openlayers
5. Python + Flask-Marshmallow
```

Let's start with docker
Install docker CE (Comunity Edition) on your system, I use docker for setting up Geoserver and Postgis

For postgis I've chosen openmaptiles/postgis and for Geoserver kartoza/geoserver docker images.
If you are not familiar with Geoserver I suggest looking briefly into it and getting some knowledge on Geo info services like WMS, WFS and etc. 
(http://geoserver.org/)

To setup Postgis and Geoserver clone the repository into your local machine and in the repository folder run:
```
  - docker-compose up 
```

So now to check if everything is working go to http://localhost:8080/geoserver <br />
* Log in into geoserver: <br />
  ```
    username: admin 
    password: geoserver
  ```
* Go to Workspaces, add workspace with name shareloc-postgis, type same text in the namespace URI and click submit <br />
* Go to Stores, add new store, choose PostGIS and enter values: <br /> 
  ```
    Data Source Name: test
    host: postgis
    port: 5432
    database: shareloc
    schema: <empty>
    user: shareloc
    password: shareloc
  ```
* Click save button in the end <br />
* There will com up a page New Layer with a table consisting of two rows, click publish of "country_osm_grid" <br />
* Scroll down to Bounding Boxes section, click Compute from data, and Compute from native bounds <br />
* Switch to Publishing section at the top and in the WMS settings, Layer settings, Default style choose polygon, scroll down and click save <br />
* Go to Layer Preview section, a row country_osm_grid must be present, click Openlayers in Common formats columns <br />
* A map and a world map must appear, that means that you've set up postgis and geoserver correctly. <br />
