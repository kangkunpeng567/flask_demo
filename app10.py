# #############################################
# html，
# 操作数据库增删改查
# pymysql：数据库连接包
# SQLaChemy:简易化操作mysql不需要写sql语句
# #############################################
# 1、导入render_template该类该类是直接在flask库中写好的，可以使前后分离
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 文本sql的执行，需要使用sqlalchemy中的text()方法处理字符串，再执行语句
# 1、导入 from sqlalchemy import text
# 2、关键部分修改如下：
# result = conn.execute(text("select 1"))
from sqlalchemy import text

# 创建一个路由对象
# __name__参数，代表（app.py）当前文件名这个模块
app = Flask(__name__)

# app.comfig创建好链接信息，然后使用SQLAlchemy来创建对象，它会调用数据库配置文件中的数据库连接对象
HOSTNAME = "127.0.0.1"
PORT = "3306"
USERNAME="root"
PASSWORD="root"
DATABASE = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"

# 测试数据库连接能否成功
db = SQLAlchemy(app)
with app.app_context():
    with db.engine.connect() as conn:
        ############################################################################
        # 文本sql的执行，需要使用sqlalchemy中的text()
        # 方法处理字符串，再执行语句
        # 1、导入
        # from sqlalchemy import text
        # 2、关键部分修改如下：
        result = conn.execute(text("select 1"))
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
