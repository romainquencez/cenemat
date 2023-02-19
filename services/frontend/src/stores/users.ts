import { defineStore } from 'pinia'
import { api } from 'boot/axios'

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
      const response = await api.post('users/login', credentials)
      if (response.status !== 200 ) throw Error
      const user = await api.get('users/whoami')
      const data = user.data
      this.user = {
        createdAt: new Date(data.created_at),
        email: data.email,
        farm: data.farm,
        firstName: data.first_name,
        lastName: data.last_name,
        id: data.id,
        identifier: Number(data.identifier),
        legalStatusId: data.legal_status_id,
        isAdmin: data.is_admin,
      }
      return response
    },
    async logOut() {
      return await api.post('users/logout').then(() => {
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
