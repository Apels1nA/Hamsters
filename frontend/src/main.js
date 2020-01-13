import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import store from './store'
import VeeValidate from 'vee-validate'

Vue.config.productionTip = false
Vue.use(
  VeeValidate,
  {
    aria: true,
    dictionary: {
      en: {
        messages: {
          required: 'Это поле не должно быть пустым',
          confirmed: 'Пароли не совпадают',
          email: 'Некорректный email',
          min: 'Минимальная длина пароля 6 символов',
          max: 'Максимальная длина пароля 20 символов',
          number: 'Это поле может содержать только цифры'
        }
      }
    }
  }
)

new Vue({
  router,
  store,
  render: h => h(App),
  async created () {
    await this.$store.dispatch('getCurrentUser')
  }
}).$mount('#app')
