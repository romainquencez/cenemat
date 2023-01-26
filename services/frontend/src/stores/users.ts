import axios from 'axios'
import { defineStore } from 'pinia'

export const usersStore = defineStore('users', {
  state: () => ({
    user: null,
  }),
  getters: {
    isAuthenticated: state => !!state.user,
    stateUser: state => state.user,
  },
  actions: {
    async register({dispatch}, form) {
      await axios.post('register', form)
      const UserForm = new FormData()
      UserForm.append('username', form.username)
      UserForm.append('password', form.password)
      await dispatch('logIn', UserForm)
    },
    async logIn({dispatch}, user) {
      await axios.post('login', user)
      await dispatch('viewMe')
    },
    async viewMe({commit}) {
      const {data} = await axios.get('users/whoami')
      await commit('setUser', data)
    },
    // eslint-disable-next-line no-empty-pattern
    async deleteUser({}, id) {
      await axios.delete(`user/${id}`)
    },
    async logOut({commit}) {
      const user = null
      commit('logout', user)
    }
  },
  mutations: {
    setUser(state, username) {
      state.user = username;
    },
    logout(state, user) {
      state.user = user;
    },
  }
})
