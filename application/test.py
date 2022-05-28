from flask import Flask,session
import os
 
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24) # 必须要设置否则报错，RuntimeError：会话不可用，因为没有设置密钥。将应用程序上的secret_key设置为唯一且保密的内容。
# 添加数据到session中
# 操作session的时候 跟操作字典是一样的。
# SECRET_KEY
 
@app.route('/')
def hello_world():
    session['username'] = 'zhangsan' # 或者flask.session['username'] = 'zhangsan'这样写也可以，就是需要倒入一下flask
    return 'Hello World!'
 
if __name__ == '__main__':
    app.run(debug=True)