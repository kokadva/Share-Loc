import Login from './features/authentication/components/login-form-component.vue';
import Map from './features/map/components/map-component.vue';

export const routes = [
  {path: '', component: Login},
  {path: '/map', component: Map},
];
