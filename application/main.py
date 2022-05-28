from logging import warning
from flask import Flask, redirect
from flask import render_template
from flask import send_from_directory
from flask import request
from flask import session
import function
import datetime

import os
import datetime
import calculate
import get_information
from decimal import Decimal

# import calculate
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=5)


@ app.route("/", methods=["POST","GET"])
def main():
    user_agent = request.headers.get("User-Agent")
    is_mobile = function.judge_pc_or_mobile(user_agent)

    session["mobile"] = is_mobile
    if request.method == "POST":
        info = calculate.main()
        
        round = float(get_information.get_round(info["altitude_angle"]))/0.34
        round = Decimal(round).quantize(Decimal("0.00001"), rounding = "ROUND_HALF_UP")
    else:
        info = {"altitude_angle":"", "azimuth_angle":""}
        round = ""

    weather = get_information.get_weather()
    with open("weather.csv", "a", encoding="utf-8") as f:
        print("ok")
        f.write("{},{},{},{},{}".format(str(weather["weather"]),str(weather["temperature"]),str(weather["humidity"]),str(weather["pressure"]), str(weather["wind"]), str(weather["warning"])))
    if weather["warning"] == {}:
        weather["warning"] = "您当前地区很安全，无灾害预警"

    location = str(get_information.get_position()["latitude"])+","+str(get_information.get_position()["longitude"])
    ip = get_information.get_position()["ip"]
    if session["mobile"]:
        return render_template("indexm.html", altitude_angle=info["altitude_angle"], azimuth_angle=info["azimuth_angle"], weather=weather, round=round, location=location, ip=ip)
    else:
        return render_template("indexm.html", altitude_angle=info["altitude_angle"], azimuth_angle=info["azimuth_angle"], weather=weather, round=round, location=location, ip=ip)

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
        session["name"] = username
        session["password"] = password
        print(username, password)
        with open("userconf", "r") as f:
            userconf = eval(str(f.read()))
        
        if userconf["username"] == username and userconf["password"] == password:
            return render_template("login.html", reminder="用户名或密码错误！")
        else:
            return redirect("/")
    else:
        return render_template("login.html",  reminder="欢迎登录")

# @app.route("/settings", met)

@app.route("/download")
def index():
    return send_from_directory(directory="./",path="./weather.csv",filename="weather.csv",as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")