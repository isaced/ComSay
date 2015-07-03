'''
Created on 2015-6-12

@author: Shuang.Wu
'''
from flask import Blueprint,session,render_template,request,redirect,url_for,make_response
vip=Blueprint("vip",__name__)

from models.Company import Company
from models.Comments import Comments
import time

@vip.route("/user",methods=["GET"])
def index():
    user=session.get("user")
    if user is None:
        return redirect(url_for("index.login"))
    list=Comments.query.filter_by(user_id=user["id"])
    return render_template("user.html",list=list)

@vip.route("/addCompany",methods=["GET"])
def addCompany():
    return render_template("addCompany.html")

@vip.route("/company/exists",methods=["POST"])
def exists():
    name=request.form["name"]
    
    if name==None:
        return make_response("EXISTS")
    
    company=Company.query.filter_by(name=name).first()
    
    if company==None:
        return make_response("NOT_EXISTS")
    else:
        return make_response("EXISTS")

@vip.route("/company/submit",methods=["POST"])
def comSub():
    name=request.form["name"]
    description=request.form["description"]
    
    if name==None or description==None:
        abort(404)
    
    company=Company(name,description,time.strftime("%Y-%m-%d %T"),None)
    Company.add(company)
    
    return redirect(url_for("vip.index"))