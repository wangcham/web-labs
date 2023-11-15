import asyncio
from quart import Quart, render_template
import db
from api.login import login_app
from api.register import register_app
from api.modifyinfo import modifyinfo_app
from api.admin import admin_app

app = Quart(__name__, template_folder="/web/dist", static_folder="/web/dist", static_url_path="")
app.register_blueprint(login_app)
app.register_blueprint(register_app)
app.register_blueprint(modifyinfo_app)
app.register_blueprint(admin_app)

@app.route('/')
async def index():
    return await render_template("index.html")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        database = db.Database()
        #创建数据库
        database.create()
        database.addAdmin()

        loop.run_until_complete(app.run_task(host='0.0.0.0', port=5000))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
