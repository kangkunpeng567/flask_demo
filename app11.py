# #############################################
# html，
# ORM,只需要修改少量代码。就可以做到对底层数据库的替换
# pymysql：数据库连接包
# SQLaChemy:简易化操作mysql不需要写sql语句
# #############################################
# 1、导入render_template该类该类是直接在flask库中写好的，可以使前后分离
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
# 文本sql的执行，需要使用sqlalchemy中的text()方法处理字符串，再执行语句
# 1、导入 from sqlalchemy import text
# 2、关键部分修改如下：
# result = conn.execute(text("select 1"))


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

# 创建用户对象类
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username= db.Column(db.String(100),nullable=False)
    password= db.Column(db.String(100),nullable=False)

# #############################################
# 创建数据库
# 请求上下文配置
with app.app_context():
    # 映射到数据库，之这里只能出纳关键数据库
    db.create_all()


# #############################################
# 数据库中插入行数据
# 创建添加用户并且写如数据库
@app.route("/adduser")
def user_add():
    # 创建用户对象
    user = User(username="zhangsan",password="123456")
    # 写入数据
    db.session.add(user)
    # 提交
    db.session.commit()
    return "数据库添加量一条对象"

# #############################################
# 数据库查询，单条数据查询
@app.route("/quryuser")
def user_qury():
    # 创建用户对象,根据主键查找朱建id是1
    user = User.query.get(1)
    print(f"密码：{user.username},用户名：{user.password}\n")
    return f"数据库查询成功  密码：{user.username}, 用户名：{user.password} \n"


# 数据库查询，多条数据查询
@app.route("/quryusermany")
def user_qury_many():
    # 创建用户对象,根据主键查找朱建id是1
    users= User.query.filter_by(username="zhangsan")
    for user in users:
        print(f"密码：{user.username},用户名：{user.password}\n")
    return f"数据库查询成功 \n"


# #############################################
# 数据库update，数据库的行数据修改更新
@app.route("/userupdate")
def user_update():
    # 创建用户对象,根据主键查找朱建id是1
    user= User.query.filter_by(username="zhangsan").first()
    user.password="78946"
    # 提交
    db.session.commit()
    return "数据库xiugai一条对象"


# #############################################
# 数据库删除
@app.route("/userdelete")
def user_delete():
    # 查询需要删除的对象
    user= User.query.get(1)
    # 删除该对象
    db.session.delete(user)
    # 提交
    db.session.commit()
    return "数据库删除一条对象"



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
