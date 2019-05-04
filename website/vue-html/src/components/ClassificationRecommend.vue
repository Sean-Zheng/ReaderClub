<template>
    <div id="classification-recommend">
        <h2>{{type_name}}</h2>
        <div class="first">
            
        </div>
        <ul v-for="item in recommend_list" :key="item.name">
            <li>
                <p>
                    <router-link to="#">{{item.name}}</router-link>
                    <span>{{item.author}}</span>
                </p>
            </li>
        </ul>
    </div>
</template>

<script>
/**
 * 
    "type_name": "玄幻魔法",
    "recommend_first": {
        "name": "万古神帝",
        "link": "https://www.biduo.cc/biquge/6_6465/",
        "image_url": "https://www.biduo.cc/files/article/image/6/6465/6465s.jpg",
        "description": "    【NEXTIDEA暨2015星创奖征文大赏（玄幻）】\n    八百年前，明帝之子张若尘，被他的未婚妻池瑶公主杀死，一代无上天骄，就此陨落。\n    八百年后，张若尘重新活了过来，却发现曾经杀死他的未婚妻，已经统一昆仑界，开辟出第一中央帝国，号称“池瑶女皇”。\n    池瑶女皇——统御天下，威临八方；青春永驻，不死不灭。\n    张若尘站在诸皇祠堂外，望着池瑶女皇的神像，心中\n"
    },
    "recommend_list": [
        {
            "link": "https://www.biduo.cc/biquge/40_40692/",
            "name": "剑来",
            "author": "烽火戏诸侯"
        }
 */
    export default {
        name:'classification-recommend',
        props: {
            type_name: {
                type: String,
                default: '',
                required:true
            },
            recommend_first:{
                type:Object,
                default:null,
                required:true
            },
            recommend_list:{
                type:Array,
                default:null,
                required:true
            }
        }
    }
</script>

<style scoped>

</style>