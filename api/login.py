import traceback
from quart import Quart,request,jsonify,Blueprint
from quart_cors import cors
import db

login_app = Blueprint('login_app',__name__)
cors(login_app)

@login_app.route('/login',methods=['post'])
async def login():
    try:
        data = await request.get_json()
        username = data['username']
        password = data['password']

        database = db.Database()

        sql = "select * from info where username = ? "
        res = database.execute(sql,(username,))
        if not res:
            return jsonify({'status':'fail','message':'用户不存在'})
        
        query = "select * from info where username=? and password=?"

        results = database.execute(query,(username,password))
        if not results:
            return jsonify({'status':'fail','message':'密码错误'})
        else:
            data = []
            ifadmin = 0
            for result in results:
                username = result[0]
                password = result[1]
                nickname = result[2]
                admin = result[3]
                ifadmin = admin
                item = {'username':username,'password':password,'nickname':nickname}
                
                data.append(item)
            
            return jsonify({'infos':data,'type':ifadmin})

    
    except Exception as e:
        print(str(e))