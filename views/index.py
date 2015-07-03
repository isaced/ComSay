from flask import Blueprint, render_template,request,Response,make_response,session,flash,redirect,url_for

index = Blueprint('index', __name__)

from models.User import User
from models.Company import Company
from models.Comments import Comments
import time,serials

@index.route('/')
def index_list():
    list=Company.query.order_by(Company.createTime.desc()).all()
    return render_template('index.html',list=list)

@index.route("/company/<string:id>")
def company(id):
    company=Company.query.filter_by(id=id).first()
    list=Comments.query.filter_by(company_id=id).all()
    return render_template("company.html",list=list,company=company)

@index.route("/company/comments/submit",methods=["POST"])
def commentsSub():
    user_id=request.form["user_id"]
    company_id=request.form["company_id"]
    contents=request.form["contents"]
    if user_id==None or company_id==None or contents==None:
        abort(404)
    user=User.query.filter_by(id=user_id).first()
    company=Company.query.filter_by(id=company_id).first()
    comments=Comments(contents,time.strftime("%Y-%m-%d %T"),user,company)
    Comments.add(comments)
    return redirect(url_for("index.company",id=company_id))

@index.route("/logout")
def logout():
    session["user"]=None
    return render_template("index.html")    

@index.route('/login',methods=["GET","POST"])
def login():
    if request.method=="GET":
        if session.get('user') is None:
            return render_template("login.html")
        else:
            return redirect(url_for("vip.index"))
    elif request.method=="POST":
        user_name=request.form["username"]
        password=request.form["password"]
        error=None
        if user_name == None or user_name=="":
            error="NOT_EXISTS"
            return render_template("login.html",error=error)
        else:
            user=User.query.filter_by(user_name=user_name).first()
            if user is None:
                error="NOT_EXISTS"
                return render_template("login.html",error=error)
            elif password==user.password:
                _dict=serials.getDict(user)
                session["user"]=_dict
                return redirect(url_for("vip.index"))
            else:
                error="WRONG_PASSWORD"
                return render_template("login.html",error=error)
    else:
        abort(404)
        

@index.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    elif request.method=="POST":
        user_name=request.form["username"]
        password=request.form["password"]
        user=User(user_name,password,time.strftime("%Y-%m-%d %T"),None)
        User.add(user)
        session["user"]=serials.getDict(user)
        return redirect(url_for("vip.index"))

@index.route("/exists",methods=["POST"])
def ifExists():
    name=request.form["username"]
    resp=None
    if name==None or name=="":
        resp=make_response("USERNAME_EXISTS")
    else:
        user=User.query.filter_by(user_name=name).first()
        if user is None:
            resp=make_response("NOT_EXISTS")
        else:
            resp=make_response("USERNAME_EXISTS")   
    return resp     