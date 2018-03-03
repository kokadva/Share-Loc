import Vue from 'vue'
import router from './routes'
import VueResource from 'vue-resource'

Vue.use(VueResource);

/* App component */
import App from './components/App.vue'


new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
