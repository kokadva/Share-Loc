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
        userLocationsLayer: null
      }
    },

    mounted: function () {

      this.view = new ol.View({
        center: [0, 0],
        zoom: 2,
        projection: "EPSG:4326"
      });


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


      var vectorLayerSource = new ol.source.Vector({
        url: 'http://0.0.0.0:8000/rest/location/get/all',
        format: new ol.format.GeoJSON()
      });
      this.userLocationsLayer = new ol.layer.Vector({
        source: vectorLayerSource,
        projection: 'EPSG:3857'
      });

      var source = new ol.source.Vector({
        features: [this.positionFeature]
      });

      var vector = new ol.layer.Vector({
        source: source,
        projection: 'EPSG:3857'
      });

      this.map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          vector,
          this.userLocationsLayer
        ],
        view: this.view
      });

      this.geolocation = new ol.Geolocation({
        projection: this.view.getProjection(),
        tracking: true
      });

      this.geolocation.on('change:position', this.updatePostionFeature);

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
        console.log("Refreshing user locations layer");
        this.userLocationsLayer.setSource(this.getUserLocationsSource());
      },

      getUserLocationsSource: function () {
        return new ol.source.Vector({
          url: 'http://0.0.0.0:8000/rest/location/get/all',
          format: new ol.format.GeoJSON()
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
