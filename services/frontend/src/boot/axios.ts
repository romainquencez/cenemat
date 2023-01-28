import { boot } from 'quasar/wrappers';
import axios, { AxiosInstance } from 'axios';
import { useUserStore } from 'stores/users'
import { useRouter } from 'vue-router'

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance;
  }
}

// Be careful when using SSR for cross-request state pollution
// due to creating a Singleton instance here;
// If any client changes this (global) instance, it might be a
// good idea to move this instance creation inside of the
// "export default () => {}" function below (which runs individually
// for each client)
const api = axios.create(
  {
    baseURL: process.env.API_URL,
    withCredentials: true,
  }
)

axios.interceptors.response.use(undefined, function (error) {
  if (error) {
    // if user is no longer authenticated, logout him and redirect him to login page
    const originalRequest = error.config
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true
      const userStore = useUserStore()
      const router = useRouter()
      userStore.logOut()
      return router.push({name: 'login'})
    }
  }
})

export default boot(({ app }) => {
  // for use inside Vue files (Options API) through this.$axios and this.$api

  app.config.globalProperties.$axios = axios;
  // ^ ^ ^ this will allow you to use this.$axios (for Vue Options API form)
  //       so you won't necessarily have to import axios in each vue file

  app.config.globalProperties.$api = api;
  // ^ ^ ^ this will allow you to use this.$api (for Vue Options API form)
  //       so you can easily perform requests against your app's API
});

export { api };
