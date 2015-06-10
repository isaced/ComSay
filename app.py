from flask import Flask
from views.index import index
from flask.ext.sqlalchemy import SQLAlchemy   
    
app=Flask(__name__)
app.register_blueprint(index)
 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////home/ws/comsay.sqlite'
db=SQLAlchemy(app)
     
if __name__ == '__main__':
    app.debug = True
    app.run("0.0.0.0",port=80)
