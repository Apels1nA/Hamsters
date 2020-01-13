<template>
  <v-layout class="header">
    <router-link class="logo" to="/"></router-link>
    <div class="header__account">
      <div class="header__sign" v-if="$store.state.user">
        <router-link to="account">{{$store.state.user.email}}</router-link>
        <p @click="logout">Выйти</p>
      </div>
      <div class="header__sign" v-else>
        <p @click="signIn = true">Войти</p>
        <p class="button" @click="showSignUp">Регистрация</p>
      </div>
    </div>
    <v-layout class="sign" align-center justify-center v-if="signIn">
      <div @click="signIn = false" class="sign__mask"></div>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12 sign__content">
          <h2>Вход</h2>
          <v-icon class="sign__close" @click="signIn = false">close</v-icon>
          <v-card-text>
            <v-form>
              <v-text-field 
                prepend-icon="mail" 
                name="email" 
                label="Электронная почта" 
                type="mail" 
                v-validate="'required|email'"  
                v-model="user.email">
              </v-text-field>
              <ul>
                  <li v-if="showSignInError">Логин или пароль не существует</li>
                  <li v-for="error in errors.collect('email')" :key="error">{{ error }}</li> 
              </ul>
              <v-text-field 
                prepend-icon="lock" 
                name="password" 
                label="Пароль" 
                id="password" 
                type="password" 
                v-validate="'required|min:6|max:20'" 
                v-model="user.password">
              </v-text-field>
              <ul>
                  <li v-for="error in errors.collect('password')" :key="error">{{ error }}</li> 
              </ul>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn 
              color="primary" 
              @click="login">
              Войти
          </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
    <v-layout 
      class="sign" 
      align-center 
      justify-center 
      v-if="formSignUp || $store.state.signUp" >
      <div @click="closeSignUp" class="sign__mask"></div>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12 sign__content">
          <h2>Регистрация</h2>
          <v-icon class="sign__close" @click="closeSignUp">close</v-icon>
          <v-card-text>
            <v-form>
              <v-text-field 
                prepend-icon="mail" 
                name="email" 
                label="Электронная почта" 
                id="email" 
                v-validate="'required|email'" 
                type="mail"  
                v-model.lazy="registration.email">
              </v-text-field>
              <ul>
                  <li v-for="error in errors.collect('email')" :key="error">{{ error }}</li> 
              </ul>
              <v-text-field 
                prepend-icon="lock" 
                @change="confirmPass" 
                name="password" 
                label="Пароль" 
                id="password"  
                v-validate="'required|min:6|max:20'" 
                type="password" 
                v-model.lazy="registration.password">
              </v-text-field>
              <ul>
                  <li v-for="error in errors.collect('password')" :key="error">{{ error }}</li> 
              </ul>
              <v-text-field 
                prepend-icon="lock" 
                @change="confirmPass" 
                name="repPassword" 
                label="Повторите пароль" 
                id="repPassword"  
                v-validate="'required|min:6|max:20'" 
                type="password" 
                v-model.lazy="registration.repPassword">
              </v-text-field>
               <ul>
                  <li v-if="showPassError">Пароли не сопадают</li>
                  <li v-for="error in errors.collect('repPassword')" :key="error">{{ error }}</li> 
              </ul>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-btn 
              @click="cofirmRegister" 
              color="primary">
              Зарегистрироваться
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-layout>
</template>

<script>
import authAPI from '@/api/user'

  export default {
    data: () => {
      return {
        formSignUp: false,
        codeConfirm: false, 
        showPassError: false,
        signIn: false,
        showSignInError: false,
        user: {
          email: '',
          password: ''
        },
        registration:{
          email: '',
          password: '',
          repPassword: '',
          code: ''
        },
      }
    },
    methods: {
      async cofirmRegister() {
         const valid = await this.$validator.validate()
         if(valid && !this.showPassError){
           this.codeConfirm = true
           await authAPI.signup({ 
             email: this.registration.email,
             password: this.registration.password
            })
            this.formSignUp = false
            this.codeConfirm = true
        }
      },
      confirmPass() {
        if(
          this.registration.password != this.registration.repPassword && 
          this.registration.repPassword != this.registration.password
        ) {
          this.showPassError = true
        }
        else {
          this.showPassError = false
        }
      },
      showSignUp () {
        this.formSignUp = true
        this.showPassError = false
        this.codeConfirm = false
      },
      closeSignUp() {
        this.formSignUp = false
        this.$store.dispatch('setSignUp')
      },
      async login() {
        const valid = await this.$validator.validate()
        if(valid){
          const status = await this.$store.dispatch('login', this.user)
          if(status === 401){
            this.showSignInError = true
            error.response.status
          }
          this.signIn = false
          this.$router.push('/')
        }
      },
      async logout() {
        await this.$store.dispatch('logout')
        this.signIn = false
        this.$router.push('/')
      }
    }
  }
</script>

<style lang="scss">
@media screen and (max-width: 768px) {
  .header{
    flex-direction: column;
    &__account{
      margin: 0 !important;
    }
    &__sign{
      flex-direction: column;
      margin-top: 5px !important;
      p, a{
        margin: 10px 0 !important; 
        transform: scale(1.2);
      }
    }
    .sign{
      .flex{
        height: 100%;
      }
      &__content{
        border-radius: 0 !important;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
      }
    }
  }
}
  .header{
    display: flex;
    align-items: center;
    padding: 10px 100px;
    &__sign{
      display: flex;
      align-items: center;
      p{
        cursor: pointer;
        font-size: 18px;
        margin: 0;
        transition: color .2s;
        &:first-child{
          margin-right: 15px;
          &:hover{
            color: #7C4DFF;
            transition: color .2s;
          }
        }
        &:last-child{
          padding: 7px 25px;
        }
      }
    }
    &__account{
      display: flex;
      align-items: center;
      margin-left: auto;
      a{
        margin-right: 10px;
      }
    }
    .logo{
      display: block;
      background: url(../assets/logo.svg) center no-repeat;
      height: 100px;
      width: 100px;
    }
    .button{
      margin-left: auto;
      height: 40px;
    }
    .sign{
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: 4;
      ul{
        margin-bottom: 10px;
      }
      li{
        font-size: 12px;
        list-style-type: none;
        color: #F54A4A;
      }
      h2{
        text-align: center;
        padding: 0 20px 20px 20px;
      }
      &__content{
        padding: 20px;
        border-radius: 20px;
        position: relative;
        .v-btn{
          margin: auto;
        }
      }
      &__mask{
        position: fixed;
        width: 100vw;
        height: 100vh;
        background: #00000060;
      }
      &__close{
        position: absolute;
        top: 27px;
        right: 30px;
      }
    }
  }
  
</style>

