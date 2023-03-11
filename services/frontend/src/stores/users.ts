import { defineStore } from 'pinia'
import { get, post, postFormData } from 'src/mixins/fetch'

export const useUserStore = defineStore('users', {
  state: () => ({
    user: null,
  }),
  getters: {
    isAuthenticated: state => !!state.user,
    isAdmin: state => state.user ? state.user.isAdmin : false,
    stateUser: state => state.user,
  },
  actions: {
    async logIn(credentials) {
      const response = await postFormData('users/login', credentials)
      const data = await get('users/whoami')
      this.user = {
        createdAt: new Date(data.created_at),
        email: data.email,
        firstName: data.first_name,
        lastName: data.last_name,
        id: data.id,
        identifier: Number(data.identifier),
        isAdmin: data.is_admin,
      }
      return response
    },
    async logOut() {
      return await post('users/logout').then(() => {
        this.user = null
      })
    }
  },
  mutations: {
    setUser(state, username) {
      state.user = username;
    },
  }
})
