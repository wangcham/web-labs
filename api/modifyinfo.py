import traceback
from quart import Quart,request,jsonify,Blueprint
from quart_cors import cors
import db

modifyinfo_app = Blueprint('modifyinfo_app',__name__)
cors(modifyinfo_app)

@modifyinfo_app.route('/modifyinfo',methods=['post'])
async def modifyinfo():
    data = await request.get_json()
    username = data['username']
    password = data['passowrd']
    nickname = data['nickname']
    oldusername = data['oldusername']

    sql = "SELECT * from info where username = ?"
    database = db.Database()
    try:
        result = database.execute(sql,(username,))
        if result and username != oldusername:
            return jsonify({'status':'fail','message':'用户名已经存在！'})
        else:
            query = "update info set username =?,password=?,nickname=? where username =?" 
            try:
                database.execute(query,(username,password,nickname,oldusername))
                return jsonify({'status':'success','message':'操作成功'})
            except Exception as e:
                return jsonify({'status':'fail','message':'数据库操作异常'})    
    except Exception as e:
        print(str(e))