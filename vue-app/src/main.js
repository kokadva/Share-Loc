import Vue from 'vue'
import App from './App.vue'
import loginform from './components/authentication-form.vue'


Vue.component('login-form', loginform);

new Vue({
  el: '#app',
  render: h => h(App)
});
