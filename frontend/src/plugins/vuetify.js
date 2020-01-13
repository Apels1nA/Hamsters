import Vue from 'vue'
import Vuetify from 'vuetify/lib'
import 'vuetify/src/stylus/app.styl'

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
    primary: '#7C4DFF',
    secondary: '#F2F2F2',
    accent: '#7C4DFF',
    error: '#F54A4A',
    info: '#7C4DFF',
    success: '#70EA45',
    warning: '#F5DA4A'
  }
})
