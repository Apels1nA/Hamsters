import Vue from 'vue'
import Vuex from 'vuex'

import authAPI from '@/api/user'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: undefined,
    signUp: false
  },
  mutations: {
    setAuth (state, user) {
      state.user = user
    },
    setSignUp (state) {
      state.signUp = !state.signUp
    }
  },
  actions: {
    setSignUp ({ commit }) {
      commit('setSignUp')
    },

    async getCurrentUser ({ commit }) {
      const user = await authAPI.getCurrentUser()
      commit('setAuth', user)
    },

    async changePassword ({ commit }, password) {
      await authAPI.changePassword(password)
    },

    async logout ({ commit }) {
      await authAPI.logout()
      commit('setAuth', undefined)
    },

    async login ({ commit }, credentials) {
      const user = await authAPI.login(credentials)
      if (user === 401) {
        return user
      } else {
        commit('setAuth', user)
        await this.dispatch('getCurrentUser')
      }
    }
  }
})
