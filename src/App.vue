<template>

  <div class="h-screen">
    <Navbar />
    <div class="overflow-hidden min-h-screen"><HeroSection /></div>
  </div>
  


</template>

<script>

import Navbar from './components/Navbar.vue';
import HeroSection from './components/HeroSection.vue';



export default{
  name:"App",
  components:{Navbar,HeroSection},
}

</script>