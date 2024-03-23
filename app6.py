# #############################################
# html，
# 过滤器
#
# #############################################
# 1、导入render_template该类该类是直接在flask库中写好的，可以使前后分离
from flask import Flask,render_template
from datetime import  datetime

# 创建一个路由对象
# __name__参数，代表（app.py）当前文件名这个模块
app = Flask(__name__)

# 创建一个user类，构造方法传入参数
class User:
    def __init__(self,username,email):
        self.username = username
        self.email = email

######################################
# 自定义一个过滤器，改变时间函数的显示样式
# 1、value对应的页面中的变量就是mytime。 <h1> {{ mytime|dformat }}</h1>
def date_format(value, str="%Y-%d-%m %H:%m"):

    # 返回value的时间格式，就是我们在后边传参进入的str字符串的格式
    return value.strftime(str)

# 使用路由对象，调用过滤器函数，传入需要调用的过滤器函数名，以及调用过滤器的调用重命名"dformat"
app.add_template_filter(date_format,"dformat")

######################################
# 过滤器,库自带的过滤器
@app.route("/filter")
def filter_demo():
    # 1、创建一个对象并且使用构造方法传入参数
    user = User(username="kangkunpeng",email="111111111")

    mytime=datetime.now()

    # 导入render_template该类该类是直接在flask库中写好的，可以使前后分离
    # 通过render_template获取前端页面，同时传入参数数值对象
    return render_template("index6.html",user=user,mytime=mytime)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
