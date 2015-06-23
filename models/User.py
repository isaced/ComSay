'''
Created on 2015-6-9

@author: Shuang.Wu
'''

from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(80),unique=True)
    password=db.Column(db.String(255),nullable=False)
    create_time=db.Column(db.String(20),nullable=False)
    modify_time=db.Column(db.String(20))
    
    def __init__(self,user_name,password,create_time,modify_time):
        self.user_name=user_name
        self.password=password
        self.create_time=create_time
        self.modify_time=modify_time
    
    def __repr__(self):
        return '<User %r>' %self.user_name

    def add(user):
        db.session.add(user)
        db.session.commit()
        