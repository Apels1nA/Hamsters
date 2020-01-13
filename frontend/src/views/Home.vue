<template>
    <v-container class="container__top">
      <div class="container__top_text">
        <h1 class="font-weight-light">it-Sensor</h1>
        <p>сервис для управления умными устройствами</p>
      </div>
      <v-btn 
        @click="checkOrder" 
        color="primary" 
        class="text-none button">
        Получить доступ
      </v-btn>
    </v-container>
</template>

<script>
  export default {
    methods: {
      checkOrder() {
        if (!this.$store.state.user) {
          this.$store.dispatch('setSignUp')
        }
        else {
          this.$router.push('/order')
        }
      }
    }
  }
</script>

<style lang="scss">
  @media only screen{
    .container{
      max-width: 100%;
    }
  }
  .container__top{
    margin: 0;
    padding: 20vh 45% 30vh 15%;
    background: url(../assets/display.png) no-repeat right bottom;
    background-size: 45%;
    .button{
      padding: 0 30px;
      font-size: 1.2em;
    }
    .dialog_window{
      width: 50%;
    }
    &_text{
      margin: 20px 0;
      h1{
        line-height: 1em;
        font-size: 7em;
      }
      p{
        margin-bottom: 0;
        font-size: 2em;
      } 
    }
  }
  @media screen and (orientation: portrait){
    .container__top{
      padding: 20px 10% 350px 10%;
      background-size: 90%;
      background-position: center bottom;
      &_text{
        h1{
        font-size: 50px;
        }
        p{
          margin-bottom: 0;
          font-size: 25px;
        } 
      }
    }
  }
  @media screen and (orientation: landscape) and (max-width: 959px){
    .container__top{
      padding: 80px 45% 150px 10%;
      background-size: 50%;
      background-position: right bottom;
      &_text{
        h1{
        font-size: 50px;
        }
        p{
          margin-bottom: 0;
          font-size: 25px;
        } 
      }
    }
  }
</style>

