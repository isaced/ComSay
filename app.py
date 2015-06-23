from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy   

from views.index import index
from views.vip import vip
 
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/ws/comsay.sqlite'
db=SQLAlchemy(app)

app.register_blueprint(index)
app.register_blueprint(vip)
app.config["SECRET_KEY"]='COMPANY_SAY'
     
if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0",port=80)

