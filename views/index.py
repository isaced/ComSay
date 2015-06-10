from flask import Blueprint, render_template,request,session

index = Blueprint('index', __name__)

@index.route('/')
def index_list():
    return render_template('index.html')

@index.route('/login')
def login():
    if session.get('user') is None:
        return render_template("login.html")
    else:
        return redirect(url_for("user"))


    

        