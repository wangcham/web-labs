<template>
  <div class="login">
    <h1>用户登陆页面(首页)</h1>
    <el-input placeholder="请输入用户名" style="margin-bottom: 20px;" v-model="username" class="input"></el-input>
    <el-input placeholder="请输入密码" type="password" v-model="password" class="input"></el-input>
    <div>
        <el-button @click="login" type="primary">登录</el-button>
        <el-button @click="register" type="primary">注册</el-button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import common from '../assets/common/common'
import {ElMessage} from 'element-plus'
import {store} from '../store/store'
export default {
    name:'logIn',
    data(){
        return{
            username:'',
            password:'',
            results:[],
            store,
        }
    },
    methods:{
        async login(){  
            if(this.username == '' || this.password == ''){
                ElMessage.error("用户名或密码不可为空");
                return
            }
            try{
                await axios.post(common.backend_prefix+'/login',{
                    'username':this.username,
                    'password':this.password,
                })
                .then(
                    res =>{
                        if(res.data.status == 'fail'){
                            ElMessage.error(res.data.message)
                            this.username = ''
                            this.password = ''
                        }else{
                            this.results = res.data.infos
                            ElMessage.success("登陆成功")
                            this.store.currentinfo = this.results;
                            console.log(this.store.currentinfo)
                            if(res.data.type == 1){
                                this.store.ifadmin = 1;
                                this.$router.push({name:'/AdminView'});
                            }else{
                                this.$router.push({name:'/ModifyInfo'});
                            }
                        }
                    }
                )
            }catch{
                error =>{
                    console.log(error)
                }
            }
        },
        register(){
            this.$router.push({name:'/RegisterNew'})
        }
    }
}
</script>

<style>
.login{
    display: flex;
    flex-direction: column;
    width: 300px;
}
.input{
    margin-bottom: 20px;
}
</style>