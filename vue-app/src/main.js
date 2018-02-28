import Vue from 'vue'
import App from './App.vue'
import loginformcomponent from './features/authentication/components/login-form-component.vue'

Vue.component('login-from-component', loginformcomponent);

new Vue({
  el: '#app',
  render: h => h(App)
})
