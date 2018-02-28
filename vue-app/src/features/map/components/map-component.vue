<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <div>
    <div id="map" class="map"></div>

  </div>
</template>

<script>
  import Map from 'ol/map';
  import View from 'ol/view';
  import TileLayer from 'ol/layer/tile';
  import XYZ from 'ol/source/xyz';
  import OSM from 'ol/source/osm';

  export default {
    data () {
      return {
        username: '',
        password: ''
      }
    },
    mounted: function () {
      var map = new Map({
        target: 'map',
        layers: [
          new TileLayer({
            source: new OSM()
          })
        ],
        view: new View({
          center: [0, 0],
          zoom: 2
        })
      });
    }
  }
</script>


<style>
  .map {
    height: 100%;
    width: 100%;
  }
</style>
