# #############################################
# html，
# 流程控制、if、for
# #############################################
# 1、导入render_template该类该类是直接在flask库中写好的，可以使前后分离
from flask import Flask,render_template
from datetime import datetime

# 创建一个路由对象
# __name__参数，代表（app.py）当前文件名这个模块
app = Flask(__name__)

######################################
# 流程控制 if
@app.route("/control")
def control_statement():
    age = 18

    books = [{"name":"三国演义","autho":"罗贯中"},{"name":"水浒","autho":"施耐庵"}]
    return render_template("index7.html", age=age, books=books)




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
