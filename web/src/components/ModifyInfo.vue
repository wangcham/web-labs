<template>
  <div class="all">
    <h1>修改页面</h1>
    <el-input  v-model="username" class="input"/>
    <el-input v-model="password" class="input"/>
    <el-input v-model="nickname" class="input"/>
    <el-button @click="modify">点击修改</el-button>
  </div>
</template>

<script>
import {store} from '../store/store'
import axios from 'axios'
import common from '../assets/common/common'
import {ElMessage} from 'element-plus'
export default {
    name:'ModifyInfo',
    data(){
        return{
            username:'',
            password:'',
            nickname:'',
            store,
            result:[],
        }
    },
    mounted(){
        this.result = this.store.currentinfo
        this.username = this.result[0].username
        this.oldusername = this.result[0].username
        this.password = this.result[0].password
        this.nickname = this.result[0].nickname
    },
    methods:{
        async modify(){
            try{
            await axios.post(common.backend_prefix+'/modifyinfo',{
                username:this.username,
                passowrd:this.password,
                nickname:this.nickname,
                oldusername:this.oldusername
            })
            .then(
                res => {
                    if(res.data.status == 'fail'){
                        //后端返回报错信息
                        ElMessage.error(res.data.message)
                    }else{
                        ElMessage.success("修改成功")
                        this.$router.push({name:'/LogIn'})
                    }
                }
            )
            }catch(error){
                error =>{
                    ElMessage.error(error)
                }
            }
        }
    }
}
</script>

<style>
.all{
    display: flex;
    flex-direction: column;
    width: 300px;
}
.input{
    margin-bottom: 20px;
}
</style>