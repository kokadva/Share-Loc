import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '',
      name: 'login',
      component: function (resolve) {
        require(['./components/login-form-component.vue'], resolve)
      }
    },
    {
      path: '/map',
      name: 'map',
      component: function (resolve) {
        require(['./components/map-component.vue'], resolve)
      },
      beforeEnter: guardRoute
    }
  ]
});

function guardRoute (to, from, next) {

  var token = localStorage.getItem('token');
  // TODO check if valid
  if (token == null) {
    next({
      path: '',
      query: { redirect: to.fullPath }
    })
  } else {
    next()
  }
}

export default router

