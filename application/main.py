from flask import Flask
from flask import render_template
from flask import request
from flask import session
import function
import datetime
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=5)


@ app.route("/")
def agent_show():
    user_agent = request.headers.get("User-Agent")
    is_mobile = function.judge_pc_or_mobile(user_agent)
    session["mobile"] = is_mobile

    if session["mobile"]:
        return render_template("indexm.html")
    else:
        return render_template("indexm.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")