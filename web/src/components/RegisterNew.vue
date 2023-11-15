<template>
  <div>
    <h1>注册页面</h1>
    <div style="width: 300px;">
        <el-input v-model="username" placeholder="请输入用户名" class="input"/>
        <el-input v-model="password" placeholder="请输入密码" class="input"/>
        <el-input v-model="confirm" placeholder="请再次输入密码" class="input"/>
        <el-input v-model="nickname" placeholder="请输入昵称" class="input"/>
        <el-button @click="register" type="primary">注册</el-button>
    </div>
  </div>
</template>

<script>
import {ElMessage} from 'element-plus'
import common from '@/assets/common/common'
import axios from 'axios'
export default {
    name:'RegisterNow',
    data(){
        return{
            username:'',
            password:'',
            confirm:'',
            nickname:'',
        }
    },
    methods:{
        async register(){
            if(this.password != this.confirm){
                ElMessage.error("两次输入的密码不一致，请重新输入！")
                this.password = '';
                this.confirm = '';
                return;
            }
            try{
                await axios.post(common.backend_prefix+'/register',{
                    username:this.username,
                    password:this.password,
                    nickname:this.nickname,
                })
                .then(
                    res =>{
                        if(res.data.status == 'fail'){
                            ElMessage.error(res.data.message)
                            this.username = '';
                            this.password = '';
                            this.nickname = '';
                            this.$router.push({name:'/LogIn'})
                        }else{
                            ElMessage.success("注册成功")
                            this.$router.push({name:'/LogIn'})
                        }
                    }
                )          
            }catch(error){
                error =>{
                    console.log(error)
                }
            }
        }
    }
}
</script>

<style>
.input{
    margin-bottom: 20px;
}
</style>