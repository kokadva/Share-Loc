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


To set up Postgis DB I've chosen kartoza/postgis docker image
Run commands in the docker cli to start Postgresql + postgis in a container:
  - docker run -e POSTGRES_DB="shareloc" -e POSTGRES_USER="user" -e POSTGRES_PASSWORD="password" -p 5432:5432 --name "postgis" -d openmaptiles/postgis
  
With this command postgis image will run in a container and will be available on port 5432, username: user, password: password, db_name: shareloc

Setting up postgis is done now it's time for Geoserver, if you are not familiar with Geoserver I suggest looking breafly into it and get some knowledge on Geo info services like WMS, WFS and etc. 
(http://geoserver.org/)

For Geoserver to setup I chose kartoza/geoserver image 
Run commands in the docker cli to start Geoserver in a container:
  - sudo docker run --name "geoserver"  --link postgis:postgis -p 8080:8080 -d -t kartoza/geoserver
 
So now to check if everything is working go to localhost:8080/geoserver 
Log in with username: admin password: geoserver
Go to Workspaces, add workspace with name shareloc-postgis, type same in the namespace URI and submit
Go to Stores, add new store, choose PostGIS, name store 
