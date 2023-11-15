import traceback
from quart import Quart,request,jsonify,Blueprint
from quart_cors import cors
import db

register_app = Blueprint('register_app',__name__)
cors(register_app)

@register_app.route('/register',methods=['post'])
async def register():
    data = await request.get_json()
    username = data['username']
    password = data['password']
    nickname = data['nickname']

    sql = "SELECT * from info where username = ?"

    database = db.Database()
    try:
        result = database.execute(sql,(username,))
        if result:
            return jsonify({'status':'fail','message':'用户已存在'})
        else:
            query = "insert into info (username,password,nickname,admin) VALUES (?,?,?,?)"
            try:
                database.execute(query,(username,password,nickname,0))
                return jsonify({'status':'success','message':'great'})
            except Exception as e:
                print(str(e))
    except Exception as e:
        print(str(e))