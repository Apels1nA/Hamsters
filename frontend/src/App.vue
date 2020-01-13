<template>
  <v-app>
    <Header/>
    <router-view/>
    <Footer/>
  </v-app>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Footer, Header
  }
}
</script>

<style lang="scss">
  *{
    margin: 0;
    padding: 0;
    text-decoration: none;
  }

  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
  }

  input[type='number'] {
    -moz-appearance: textfield;
  }
  
  .v-stepper__header, .v-stepper__items{
    box-shadow: none;
  }
  .v-btn {
    border-radius: 20px; 
  }
  .button{
    color: #fff;
    font-weight: 300;
    text-decoration: none;
    background: #7C4DFF;
    border-radius: 20px;
    padding: 10px 50px;
    transition: all .2s;
    cursor: pointer;
    &:hover{
      background: rgb(111, 60, 250);
      transition: all .2s;
    }
  }
  .dialog_window{
    background: #fff;
    border-radius: 20px;
  }
</style>
