<template>
  <div>
    <!--事件绑定-->
    <input @keydown.enter="onkeydown">
    <input @keydown.13="onkeydown13">
    <!--自定义事件-->
    <component-a @my-event="onComaMyEvent"></component-a>

    <!--表单数据的双向绑定-->
    <input v-model="myValue" type="text">
    {{ myValue }}

    <input v-model.lazy="myValueLazy" type="text">
    {{myValueLazy}}  {{typeof (myValueLazy)}}

    <input v-model.number="myValueNumber" type="text">
    {{typeof (myValueNumber)}}
    <br>
    <!--多选框动态数据的绑定-->
    <input v-model="myBox" type="checkbox" value="a">
    <input v-model="myBox" type="checkbox" value="b">
    <input v-model="myBox" type="checkbox" value="c">
    {{ myBox }}

    <!--单选框-->
    <input v-model="myBox1" type="radio" value="1">
    <input v-model="myBox1" type="radio" value="2">
    <input v-model="myBox1" type="radio" value="3">
    {{ myBox1 }}
    <!--下拉选择框-->
    <select v-model="selection">
      <option value="1">1</option>
      <option value="2">2</option>
      <option value="3">3</option>
      <option value="4">4</option>
      <option value="5">5</option>
    </select>
    {{selection}}

    <select v-model="selectionfor">
      <option v-for="item in selectOptions" v-bind:value="item.value">{{item.text}}</option>
    </select>
    {{ selectionfor }}

    <!--计算属性-->
    <input type="text" v-model="myvalue1">
    {{ myValueWithoutNum }}

    <!--属性监听  watch-->
    <input type="text" v-model="myVal">

    <!--组件的动态渲染-->
    <!--<div :is="comToRender"></div>-->

    <!--父子组件传递信息-->
    <!--<component-b 数字="51" number-two="123123">-->
    <component-b>

    </component-b>

    <!--插槽功能-->
    <component-b :my-value="myVal">
      <p>123</p>
    </component-b>


    <component-b :my-value="myVal">
      <p>123</p>
      <p slot="header">这是头</p>
      <p slot="footer">这是脚</p>
    </component-b>

    <!--在挂在点上，动态的切换组件-->
    <button v-on:click="toggleComponent">
      切换子组件
    </button>
    <div class="ab">
      <div :is="currentView"></div>
    </div>



  </div>
</template>

<script>
  import componentA from './components/a'
  import componentB from './components/b'
  import componentHello from './components/HelloWorld'

  export default {
    components:{
      componentA,
      componentHello,
      componentB
    },
    data() {
      return{
        myValue:'',
        myValueLazy:'',
        myValueNumber:0,
        myBox:[],
        myBox1:[],
        selection:1,
        selectionfor:0,
        selectOptions:[
          {
            text:'apple',
            value:0
          },
          {
            text:'banana',
            value:1
          }
        ],
        myvalue1:"",
        myVal:'',
        comToRender:'component-hello',
        currentView:'component-a'
      }
    },
    methods:{
      onkeydown(){
        console.log("onkeydown")
      },
      onkeydown13(){
        console.log("onkeydown13")

      },
      onComaMyEvent(paramfromA){
        console.log("onComaMyEvent:" + paramfromA)
      },
      toggleComponent(){
        if(this.currentView === 'component-a'){
          this.currentView = 'component-b'
        }else {
          this.currentView = 'component-a'
        }
      }
    },
    computed:{
      myValueWithoutNum:function () {
        return this.myvalue1.replace(/\d/g,'')
      }
    },
    watch:{
      myVal: function (val, oldVal) {
        console.log(val, oldVal)

      }
    }
  }
</script>

<style>

</style>
