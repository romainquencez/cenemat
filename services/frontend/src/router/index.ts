import { route } from 'quasar/wrappers';
import {
  createMemoryHistory,
  createRouter,
  createWebHashHistory,
  createWebHistory,
} from 'vue-router';
import { useUserStore } from 'stores/users'

import routes from './routes';

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default route(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory);

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(process.env.VUE_ROUTER_BASE),
  });

  const userStore = useUserStore()

  Router.beforeEach((to, from, next) => {
    // if route require being authenticated, but user is not authenticated
    if (
      to.matched.some((record) => record.meta.requiresAuth) &&
      !userStore.isAuthenticated
    ) {
      // redirect to login page
      Router.push({name: 'login'})

      // if route require being unauthenticated, but user is authenticated
    } else if (
      to.matched.some((record) => record.meta.requiresAuth === false) &&
      userStore.isAuthenticated
    ) {
      // redirect to user page
      Router.push({name: 'user'})

    // if route does not require any special authentication
    } else {
      // continue to route
      next()
    }
  })

  return Router;
});
