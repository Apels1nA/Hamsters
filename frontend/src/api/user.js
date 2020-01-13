import axios from './index'
import router from '../router'

export default {
  async signup (credentials) {
    try {
      await axios.post('/users', {
        email: credentials.email,
        password: credentials.password
      })
    } catch (error) {
      return undefined
    }
  },

  async login (credentials) {
    try {
      await axios.post('/login', {
        email: credentials.email,
        password: credentials.password
      })
      router.push('/')
    } catch (error) {
      return error.response.status
    }
  },

  async changePassword (password) {
    try {
      await axios.patch('/users', {
        password: password
      })
    } catch (error) {
      return error.response.status
    }
  },

  async logout () {
    try {
      await axios.get('/logout')
      router.push('/')
    } catch (error) {
      return error.response.status
    }
  },

  async getCurrentUser () {
    try {
      const user = await axios.get('/users/current')
      return user.data
    } catch (error) {
      return undefined
    }
  }
}
