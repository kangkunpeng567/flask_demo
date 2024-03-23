# #############################################
# url和视图的映射
# #############################################
from flask import Flask,request
app = Flask(__name__)

# url: http[80]  /  https[443],不需要自己写，确认好通讯协议后就不需要确认端口
# @route映射函数，自己配置映射列表
@app.route('/hello')
def hello():
    return "hello word!9999991"


# 一、路由传参，通过<>进行参数传递
@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
    return "id: %s" % blog_id

# 二、通过列表访问的访问例表的时候，更加的灵活的设置页面数
# 页面请求格式：http://127.0.0.1:5000/blog/list?page=2
@app.route('/blog/list')
def blog_list():
    # 定义一个page变量用来接受页面请求（字典的形式存储），page是key，默认值是1，类型是int
    page = request.args.get("page",default=1,type=int)
    # 得到用户请求的key值反馈给页面打印输出
    return f"id:{page}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
