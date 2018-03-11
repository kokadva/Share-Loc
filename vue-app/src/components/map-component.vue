<template>
  <div id="map" class="map"></div>
</template>

<script>

  export default {
    data () {
      return {
        username: '',
        password: '',
        geolocation: null,
        positionFeature: null,
        map: null,
        view: null,
        timer: null,
        userLocationsLayer: null,
        geometryDrawinsLayer: null,
        gpsLayer: null,
        drawingLayer: null,
        drawInteraction: null,
      }
    },

    mounted: function () {

      // View
      this.view = new ol.View({
        center: [0, 0],
        zoom: 2,
        projection: "EPSG:4326"
      });

      // Drawing layer
      this.drawingLayer = new ol.layer.Vector({
        source: new ol.source.Vector({wrapX: false})
      });


      // Position point (GPS)
      this.positionFeature = new ol.Feature();
      this.positionFeature.setStyle(new ol.style.Style({
        image: new ol.style.Circle({
          radius: 6,
          fill: new ol.style.Fill({
            color: '#3399CC'
          }),
          stroke: new ol.style.Stroke({
            color: '#fff',
            width: 2
          })
        })
      }));

      // GPS layer (for position point)
      this.gpsLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
          features: [this.positionFeature]
        }),
        projection: 'EPSG:3857'
      });


      // Drawings layer (WMS)
      this.geometryDrawinsLayer = new ol.layer.Tile({
        source: new ol.source.TileWMS({
          url: 'http://localhost:8080/geoserver/shareloc/wms',
          params: {
            'LAYERS': '	shareloc:geometry_drawings'
          }
        })
      });


      // Vector layer for gps
      this.userLocationsLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
          url: 'http://0.0.0.0:8000/rest/location/get/all',
          format: new ol.format.GeoJSON()
        }),
        projection: 'EPSG:3857'
      });

      // Map
      this.map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          this.geometryDrawinsLayer,
          this.drawingLayer,
          this.gpsLayer,
          this.userLocationsLayer,
        ],
        view: this.view
      });


      // Init drawing interaction
      this.drawInteraction = new ol.interaction.Draw({
        source: this.drawingLayer.getSource(),
        type: "Polygon"
      });
      this.map.addInteraction(this.drawInteraction);
      this.drawInteraction.on('drawend', this.uploadDrawendPolygon);

      // Geolocation init
      this.geolocation = new ol.Geolocation({
        projection: this.view.getProjection(),
        tracking: true
      });
      this.geolocation.on('change:position', this.updatePostionFeature);

      // Timer init
      this.timer = setInterval(this.refreshUserLocations, 1000)

    },


    methods: {
      updatePostionFeature: function () {
        var coordinates = this.geolocation.getPosition();
        console.log("Location changed");
        this.positionFeature.setGeometry(coordinates ? new ol.geom.Point(coordinates) : null);
        this.$http.post('http://0.0.0.0:8000/rest/location/update', {
          'token': localStorage.getItem('token'),
          'coordinates': coordinates
        }).then(response => {
          console.log(response.body.token);
        }, response => {
          console.log("Error");
        });
      },

      refreshUserLocations: function () {
        this.userLocationsLayer.setSource(this.getUserLocationsSource());
      },

      getUserLocationsSource: function () {
        return new ol.source.Vector({
          url: 'http://0.0.0.0:8000/rest/location/get/all',
          format: new ol.format.GeoJSON()
        });
      },

      uploadDrawendPolygon: function (e) {
        var coordinates = e.feature.getGeometry().getCoordinates()[0];
        console.log(coordinates);
        this.$http.post('http://0.0.0.0:8000/rest/drawing/upload', {
          'token': localStorage.getItem('token'),
          'coordinates': coordinates
        }).then(response => {
//           TODO clean up drawing layer
          console.log(response.body.token);
        }, response => {
          console.log("Error");
        });

      }
    }
  }
</script>


<style>
  .map {
    height: 100%;
    width: 100%;
  }
</style>
