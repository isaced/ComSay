'''
Created on 2015-6-12

@author: Shuang.Wu
'''
from flask import Blueprint,session
vip=Blueprint("vip",__name__)


@vip.route("/user",methods=["GET"])
def index():
    if session.get("user") is None:
        return redirect(url_for("index.login"))
    return render_template("user.html")
