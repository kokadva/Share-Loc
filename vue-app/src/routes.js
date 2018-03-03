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
      }
    }
  ]
});

// function guardRoute (to, from, next) {
//   // work-around to get to the Vuex store (as of Vue 2.0)
//   const auth = router.app.$options.store.state.auth
//
//   if (!auth.isLoggedIn) {
//     next({
//       path: '/login',
//       query: { redirect: to.fullPath }
//     })
//   } else {
//     next()
//   }
// }
//
export default router

