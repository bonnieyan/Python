<template>
  <div>
    {{msg}}
    <button @click="emitMyEvent">A组件中的按钮</button>
  </div>
</template>

<script>
  export default {
    data(){
      return{
        msg:"我是组件A"

      }
    },
    methods:{
      emitMyEvent(){
        this.$emit('my-event', this.msg)
      }
    }
  }
</script>

<style scoped>

</style>
