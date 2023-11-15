<template>
  <div>
    <h1>管理员界面</h1>
    <div style="width: 700px;">
        <el-table :data="results" style="width: 100%;">
            <el-table-column prop="username" label="Username" width="180"></el-table-column>
            <el-table-column prop="password" label="Password" width="180"></el-table-column>
            <el-table-column prop="nickname" label="Nickname" width="180"></el-table-column>
            <el-table-column>
                <template #default="scope">
                <el-button size="small" @click="handleEdit(scope.$index, scope.row)"
                >修改</el-button
                >
                <el-button
                size="small"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)"
                >删除</el-button
                >
            </template>
            </el-table-column>
        </el-table>
    </div>
  </div>
</template>

<script>
import {store} from '../store/store'
import {ElMessage} from 'element-plus'
import axios from 'axios'
import common from '../assets/common/common'

export default {
    name:'AdminView',
    data(){
        return{
            results:[],
            store,
            username:'',
            password:'',
            nickname:'',
        }
    },
    mounted(){
        try{
            axios.post(common.backend_prefix+'/getdata'
            ).then(
                res =>{
                    if(res.data.status == 'fail'){
                        ElMessage.error("获取用户信息失败")
                    }else{
                        this.results = res.data
                        ElMessage.success("获取用户信息成功")
                    }
                }
            )

        }catch(error){
            error =>{
                console.log(error)
            }
        }
    },
    methods:{
        handleEdit(index,row){
        this.username = row.username;
        this.password = row.password;
        this.nickname = row.nickname;
        const data = [
            {
                'username':this.username,
                'password':this.password,
                'nickname':this.nickname,
            }
        ]
        this.store.currentinfo = data;
        this.$router.push({name:'/ModifyInfo'})
    },
    async handleDelete(index,row){
        this.username = row.username;
        try{
        await axios.post(common.backend_prefix+'/deleteuser',{
            'username':this.username,
        })
        .then(
            res =>{
                if(res.data.status == 'fail'){
                    ElMessage.error(res.data.message)
                }else{
                    ElMessage.success("删除成功");
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
    },
}
</script>

<style>

</style>