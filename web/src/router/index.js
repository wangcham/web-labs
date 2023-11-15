import LogIn from '../components/LogIn.vue'
import ModifyInfo from '../components/ModifyInfo.vue'
import RegisterNew from '../components/RegisterNew.vue'
import {createRouter,createWebHistory} from 'vue-router'
import AdminView from '../components/AdminView.vue'
const routes = [
    {path:'/',redirect:'/LogIn'},
    {path:'/LogIn',name:'/LogIn',components:{LogIn:LogIn}},
    {path:'/ModifyInfo',name:'/ModifyInfo',components:{ModifyInfo:ModifyInfo}},
    {path:'/RegisterNew',name:'/RegisterNew',components:{RegisterNew:RegisterNew}},
    {path:'/AdminView',name:'/AdminView',components:{AdminView:AdminView}}
]

const router = createRouter(
    {
        history:createWebHistory(),
        routes
    }
);

//导出前端路由
export default router