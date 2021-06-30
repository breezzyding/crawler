# -*- coding: utf-8 -*-

from flask import Flask, render_template, request   
import datetime

app = Flask(__name__)  # 获取Flask对象，以当前模块名为参数

# 路由默认为（127.0.0.1:5000）
# @app.route('/')  # 装饰器对该方法进行路由设置，请求的地址
# def hello_world():  # 方法名称

#     return '你好，欢迎光临!'  # 返回响应的内容

# debug模式开启



@app.route("/index")
def hello():
    return "nihao!"


# 通过访问路径，获取用户的字符串参数
@app.route("/user/<name>")
def welcome(name):

    return "你好,%s"%name

# 通过访问路径，获取用户的整形参数      此外，还有float类型
@app.route("/user/<int:id>")
def welcome2(id):

    return "你好,%d号的会员"%id

# 路由路径不能重复，用户通过唯一路径访问特定的函数


# 返回给用户渲染后的网页文件
# @app.route("/")
# def index2():
#     return render_template("testindex.html")



# 向页面传递一个变量
@app.route("/")
def index2():
    time = datetime.date.today()                   # 普通变量
    name = ["小张", "小王", "小赵"]                 # 列表类型
    task = {"任务":"打扫卫生", "时间":"3小时"}       # 字典类型
    return render_template("testindex.html", var = time, list = name, task = task)

# 表单提交
@app.route('/test/register')
def register():
    return render_template("test/register.html")

# 接收表单提交的路由，需要制定method为post
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("test/result.html", result = result)


if __name__ == '__main__':
    app.run(debug=True)
