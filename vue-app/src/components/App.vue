<template>
  <router-view></router-view>
</template>

<script>

  import MapComponent from './map-component.vue'
  import LoginFormComponent from './login-form-component.vue'

  export default {
    name: 'app',
    components: { MapComponent, LoginFormComponent },
    data () {
      return {
      }
    }
  }
</script>

<style lang="scss">
</style>
