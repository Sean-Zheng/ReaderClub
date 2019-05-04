<template>
    <div id="page-link">
        
    </div>
</template>

<script>
    export default {
        name:'page-link',
        props: {
            previous: {
                type: String,
                default: '',
                required:true
            },
            next:{
                type:String,
                default:'',
                required:true
            },
            catalog:{
                type:String,
                default:'',
                required:true
            }
        }
    }
</script>

<style scoped>

</style>