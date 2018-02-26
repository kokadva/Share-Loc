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
  - cd geoserver-shell && docker image build . -t publish
  - docker-compose up 
```

So now to check if everything is working: 
* Go to http://localhost:8080/geoserver <br />
* Go to Layer Preview section, a row country_osm_grid must be present, click Openlayers in Common formats columns <br />
* A map and a world map must appear, that means that you've set up postgis and geoserver correctly. <br />
