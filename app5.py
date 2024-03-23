# #############################################
# html，
# 1、创建类对象进行传参；
# 2、通过json进行传参
#
# #############################################
# 1、导入render_template该类该类是直接在flask库中写好的，可以使前后分离
from flask import Flask,render_template
app = Flask(__name__)

# 创建一个user类，构造方法传入参数
class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

# html传入参数，可以是一个类
@app.route('/')
def blog_detail():
    # 1、创建一个对象并且使用构造方法传入参数
    user = User(username="kangkunpeng",email="3128676939")

    # 2、通过创建json对象传参
    persson = {
        "username":"zhangsan",
        "email":"31286769399"
    }
    # 返回render_template对象调用的页面
    return render_template("index5.html",user=user,persson=persson)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
