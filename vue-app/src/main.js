import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import loginformcomponent from './features/authentication/components/login-form-component.vue'
import mapcomponent from './features/map/components/map-component.vue'
import VueResource from 'vue-resource'

import { routes } from './routes';

Vue.component('login-from-component', loginformcomponent);
Vue.component('map-component', mapcomponent);
Vue.use(VueRouter);
Vue.use(VueResource);

const router = new VueRouter({
  routes
});


new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
