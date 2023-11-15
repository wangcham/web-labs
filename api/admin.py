import traceback
from quart import Quart,request,jsonify,Blueprint
from quart_cors import cors
import db

admin_app = Blueprint('admin_app',__name__)
cors(admin_app)
#获取后端用户数据
@admin_app.route('/getdata',methods=['post'])
def getdata():
    database = db.Database()
    sql = "select username,password,nickname from info"
    results = database.execute(sql)

    if not results:
        return jsonify({'status':'fail','message':'没有用户数据'})
    
    data = []

    for result in results:
        username = result[0]
        password = result[1]
        nickname = result[2]

        item = {'username':username,'password':password,'nickname':nickname}
        data.append(item)

    return jsonify(data)

@admin_app.route('/deleteuser',methods=['post'])
async def deleteuser():
    data = await request.get_json()
    username = data['username']

    sql = "select admin from info where username = ?"

    database = db.Database()
    result = database.execute(sql,(username,))
    if result:
        if result[0][0] == 1:
            return jsonify({'status':'fail','message':'管理员账户无法删除！'})
        else:
            try:
                query = "delete from info where username = ?"
                database.execute(query,(username,))
                return jsonify({'status':'success','message':'操作成功'})
            except Exception as e:
                print(str(e))
    else:
        return jsonify({'status':'fail','message':'找不到此用户'})

