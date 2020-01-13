<template>
  <v-container>
    <a :href="payment_url">Оплатить хочу я очень</a>
  </v-container>
</template>

<script>
  import sha256 from 'js-sha256'

  export default {
    data: () => {
      return {
        login: 'itsensor',
        amount: 2000,
        orderId: '0',
        description:'test',
        isTest: 1,
        apiKey: 'tIc5x0DdJWK4gNeU5Mf9',
        signature: undefined
        // D9uNv4fsoz1Aou2VCp4r aNaRRQPjuD24M74pKI1B
      }
    },
  
    computed: {
      payment_url() {
        return `https://auth.robokassa.ru/Merchant/Index.aspx?MrchLogin=${this.login}&OutSum=${this.amount}&InvId=${this.orderId}&InvDesc=${this.description}&IsTest=${this.isTest}&SignatureValue=${this.signature}`
      }
    },

    async created() {
      this.signature = sha256(`${this.login}:${this.amount}:${this.orderId}:${this.apiKey}`)
      const user = await this.$store.state.user
      if (!user) {
        this.$router.push('/')
      }
      if (user.payment_complete) {
        this.$router.push('/')
      }
    },
  }
</script>