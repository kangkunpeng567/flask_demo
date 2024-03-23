# #############################################
# html，
# 表关联查询user、artic
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
    # artics888 = db.relationship("Artic",back_populates="author999")

# 创建书外键关联
class Artic(db.Model):
    __tablename__ = "artic"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title= db.Column(db.String(200),nullable=False)
    content= db.Column(db.Text,nullable=False)
    # 设置w外键，晚间关联的是user表中的id
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    # 添加关系，随后在访问 artic.author时，会自动在自己表中寻找有没有和user产省
    # 外键的关系的字段，然后查询user结果返回;
    # 通过关联关系，查询该作者所有的文章，这时需要在use、artic两张表中都添加边关系
    author = db.relationship("User",backref="artics") # 会自动在user中天添加斌关系


artic =Artic(title="FLASK!!",content="gasdjgfjhsdghjg456")
# artic.author_id=user.id;
# user=User.query.get(artic.author_id)
print(artic.author)



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



@app.route("/articadd")
def articadd():
    artic =Artic(title="FLASK!!",content="知了")
    artic.author=User.query.get(2)

    artic2 = Artic(title="红楼梦!!", content="曹雪芹")
    artic2.author = User.query.get(2)

    artic3 = Artic(title="西游记!!", content="罗贯中")
    artic3.author = User.query.get(2)

    db.session.add_all([artic,artic2,artic3])
    # 提交
    db.session.commit()
    return "添加一篇文章"


@app.route("/articqury")
def articqury():
    user =User.query.get(2)
    for artic in user.artics:
        print(artic.title)
    return "文章查宅哦成功"
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
