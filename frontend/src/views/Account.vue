<template>
    <v-container class="account">
        <p v-if="showSuccessLabel">Пароль обновлен успешно</p>
        <h2>Страница пользователя</h2>
        <div class="account__info">
            <h3>Информация о пользователе</h3>
            <p><strong>Почта:&nbsp;</strong>{{$store.state.user.email}}</p>
            <router-link to="#"><span @click="toggleForm">Редактировать пароль</span></router-link>
            <p :class="$store.state.user.payment_complete ? 'approve' : 'no-approve'">
                Статус: 
                <span v-if="!$store.state.user.payment_complete">Не оплачено</span>
                <span v-else>Оплачено</span>
            </p>
            <v-form v-if="showPasswordForm" class="account__info-form">
                <p class="account__info__password">Сменить пароль</p>
                <v-text-field prepend-icon="lock" @change="confirmPass" name="password" label="Пароль" id="password"  v-validate="'required|min:6|max:20'" type="password" v-model.lazy="password"></v-text-field>
                <ul>
                    <li v-for="error in errors.collect('password')" :key="error">{{ error }}</li> 
                </ul>
                <v-text-field prepend-icon="lock" @change="confirmPass" name="repPassword" label="Повторите пароль" id="repPassword"  v-validate="'required|min:6|max:20'" type="password" v-model="repPassword"></v-text-field>
                <ul>
                    <div v-if="showPasswordError">
                        <li>Пароли не сопадают</li>
                        <li v-for="error in errors.collect('repPassword')" :key="error">{{ error }}</li> 
                    </div>
                </ul>
                <v-btn @click="changePassword" :disabled="password && showPasswordError">Сохранить пароль</v-btn>
            </v-form>
        </div>
        <div class="account__download">
            <h3>Скачать мобильное приложение</h3>
            <v-btn disabled>iOS</v-btn>
            <router-link to="#"><v-btn color="success">Android</v-btn></router-link>
        </div>
    </v-container>
</template>

<script>
  import authAPI from '@/api/user'  

  export default {
    name: 'account',
    data: () => {
        return {
            showPasswordForm: false,
            showPasswordError: false,
            showSuccessLabel: false,
            password: '',
            repPassword: ''
        }
    },
    methods: { 
        async toggleForm() {
            this.showPasswordForm = !this.showPasswordForm
        },
        async confirmPass() {
            if(
                this.password != this.repPassword && 
                this.repPassword != this.password
            ) {
                this.showPasswordError = true
            }
            else {
                this.showPasswordError = false
            }
        },
        async changePassword() {
            const valid = await this.$validator.validate()
            if(valid){
                await authAPI.changePassword(this.password)
                this.showSuccessLabel = true
                await authAPI.logout()
                location.reload()
            }
        }
    }

  }
</script>

<style lang="scss">
    @media screen and (max-width: 768px) {
        .account__info-form{
            width: 90% !important;
        }
    }
    .account{
        text-align: center;
        .approve{
            span{
                color: green;
            }
        }
        .no-approve{
            span{
                color: red;
            }
        }
        h3{
            margin-bottom: 10px;
        }
        &__info{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 50px;
            line-height: 30px;
            &-form{
                width: 30%;
                ul{
                    margin-bottom: 10px;
                }
                li{
                    font-size: 12px;
                    list-style-type: none;
                    color: #F54A4A;
                }
            }
            &__password{
                font-size: 20px;
            }
            p{
                margin: 0;
            }
        }
    }
</style>
