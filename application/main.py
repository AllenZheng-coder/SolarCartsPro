from errno import ESTALE
from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import session
import function
import datetime
import database
import os
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=5)


@ app.route("/")
def main():
    user_agent = request.headers.get("User-Agent")
    is_mobile = function.judge_pc_or_mobile(user_agent)
    session["mobile"] = is_mobile

    if session["mobile"]:
        return render_template("indexm.html", date=datetime.datetime.now().strftime(r"%Y年%m月%d日  %H:%M:%S"))
    else:
        return render_template("indexm.html")

@app.route("/charts/<content>")
def shows(content):
    try:
        return render_template("{}.html".format(content))
    except:
        return "404"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.values.get("username")
        password = request.values.get("password")
        print(username, password)
        if database.login(username) == -1:
            return render_template("login.html", reminder="用户名或密码错误！")
        else:
            return redirect("/")
    else:
        return render_template("login.html",  reminder="欢迎登录")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")