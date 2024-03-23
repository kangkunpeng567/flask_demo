# 1、flask路由，用来匹配url
# 2、requrst 请求 abord函数
# 3、模板
# 4、flask数据库
# 5、表单
# 6、ajax

############################################################
# 安装： pip install flask
####
# 导入flask类
from flask import Flask

# 创建一个路由对象
# __name__参数，代表（app.py）当前文件名这个模块
app = Flask(__name__)

# 1、路由匹配的逻辑。
# # 路由，页面上输入一个网址url，页面就会就会找到这个路由进行匹配."/"根路由
# 2、如果页面上的url在路由中匹配到当前地址就会返回路由函数中的信息打印到前端页面
@app.route('/hello')
def hello():
    return "hello word!9999991"

@app.route('/hi')
def hi():
    return "<h1> hihi8888888 !<h1>"

# 1、debug 模式：（调试过程将非常有用不需要频繁重启）
#    社区版本需要添加参数配置，app.run(debug=True)

# 2、host：监听主机名是多少
# 如果希望汪局域网内，其他人访问我们的电脑，我们只需要让本机在局域网内的IP给到其他人
# app.run(host="0.0.0.0")

# 3、修改端口号port
# 如果重复端口号，可以修改
# app.run(port="5001")

# 如果当前文件是作为主入口文件
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="5001")