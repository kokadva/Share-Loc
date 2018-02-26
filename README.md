# Share-Loc

## Share loccation

An app where you login and see all users locations which are also logged in. You can draw geometric figures on the map which will be seen by everybody. 

### Home project

Technologies used in the project:

```
1. Docker
2. Postgresql + Postgis
3. Geoserver
4. Openlayers
5. Python + Flask-Marshmallow
6. Vue.js
```

Let's start with docker
Install docker CE (Comunity Edition) on your system, I use docker for setting up Geoserver and Postgis

For postgis I've chosen openmaptiles/postgis and for Geoserver kartoza/geoserver docker images.
If you are not familiar with Geoserver I suggest looking briefly into it and getting some knowledge on Geo info services like WMS, WFS and etc. 
(http://geoserver.org/)

To setup Postgis and Geoserver clone the repository into your local machine and in the repository folder run:
```
  - docker image build geoserver-shell/ -t publish
  - docker-compose up 
```

So now to check if everything is working: 
* Go to http://localhost:8080/geoserver <br />
* Go to Layer Preview section, a row country_osm_grid must be present, click Openlayers in Common formats columns <br />
* A world map must appear, that means that postgis and geoserver are connected and working correctly. <br />
