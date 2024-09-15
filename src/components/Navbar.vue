<template>
    <div class="bg-gray-900 text-gray-200 py-3.5 px-6 shadow md:flex justify-between items-center">
        <div class="flex items-center">
            <span class="text-blue-600 text-xl mr-1">
                Water for life.
                <!-- logo -->
            </span>
            <h1 class="text-xl">AquaWise</h1>
        </div>

       

        <ul class="md:flex md:items-center ">
            <li class="md:mx-4 " v-for="link in links">
                <a :href="link.link" class="text-xl hover:text-blue-500">{{ link.name }}</a>
            </li>
            <Button>Get Started</Button>
        </ul>
    </div>
</template>

<script>
import Button from './Button.vue'
export default{
    components:{Button},

    setup(){
        let links = [
            {name:"Home", link:"#"},
            {name:"Services", link:"https://jalshakti-ddws.gov.in/en"},
            {name:"Blog's", link:"blogs.html"},
            {name:"Contact", link:"https://www.instagram.com/aquawise87/"},
            {name:"About", link:"about.html"},
        ]

        

        return {links,open,}
    }
}
</script>