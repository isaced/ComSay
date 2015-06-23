from flask import Blueprint, render_template,request,Response,make_response,session,flash,redirect,url_for

index = Blueprint('index', __name__)

from models.User import User
import time

@index.route('/')
def index_list():
    user=User.query.filter_by(user_name="isaced").first()
    print(user.user_name)
    return render_template('index.html',mem=user)

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
                print(user.__dict__)
                session["user"]=user
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
        print(user.id+","+user.user_name+","+user.password+","+user.create_time+","+user.modify_time)
        #user=User.query.filter_by(user_name=user.user_name).first()
        session[user]=user.__dict__
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