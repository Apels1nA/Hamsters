<template>
  <v-footer color="primary">
    <v-layout justify-center row wrap>
      <v-btn 
        v-for="link in links" 
        :key="link" 
        color="white" 
        flat round> 
        {{ link }} 
      </v-btn>
      <v-flex lighten-2 text-xs-center white--text> &copy;{{ new Date().getFullYear() }} — <strong>itSensor</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      links: [
      ]
    })
  }
</script>

<style>

</style>
