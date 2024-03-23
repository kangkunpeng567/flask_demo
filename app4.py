# #############################################
# html，模板渲染
# #############################################
# 1、导入render_template该类该类是直接在flask库中写好的，可以使前后分离
from flask import Flask,render_template
app = Flask(__name__)

# url: http[80]  /  https[443],不需要自己写，确认好通讯协议后就不需要确认端口
# @route映射函数，自己配置映射列表
@app.route('/')
def hello():
    # 返回render_template对象调用的页面
    return render_template("index3.html")


# html传入参数
# 接口访问格式：http://127.0.0.1:5000/blog/1234
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    # 返回render_template对象调用的页面
    return render_template("index4.html",blog_id=blog_id)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
