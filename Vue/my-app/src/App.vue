<template>
  <div id="app">
  <!--
    <img src="./assets/logo.png">
    <router-view/>
    <Banner />
  -->
  <!-- 分为上下两部分，上面渲染路由选择的页面内容，下面渲染固定的菜单栏组件 -->
  <!-- 上部分 -->

  <!-- 下部分 -->

  </div>
</template>

<script>
// import Banner from './components/Banner'

import Home from './components/modules/Home'

export default {
  name: 'App',
  components: {
    Banner
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
