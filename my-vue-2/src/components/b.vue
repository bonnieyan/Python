<template>

  <div>
    {{msg}}
    {{ 数字 }}
    {{ numberTwo }}
    {{myValue}}
    <slot>插槽没有插上</slot>

    <slot name="header"> 没有头 </slot>
    <p>中间的内容</p>
    <slot name="footer"> 没有脚 </slot>

  </div>

</template>

<script>
  export default {
    props:['数字','number-two','my-value'],
    data(){
      return{
        msg:"我是B组件"
      }

    }
  }
</script>

<style scoped>

</style>

