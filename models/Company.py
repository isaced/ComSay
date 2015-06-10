'''
Created on 2015-6-9

@author: Shuang.Wu
'''

from app import db

class Company(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True)
    description=db.Column(db.String(255),nullable=False)
    createTime=db.Column(db.String(20),nullable=False)
    modifyTime=db.Column(db.String(20))
    
    def __init__(self,name,description,createTime,modifyTime):
        self.name=name
        self.description=description
        self.createTime=createTime
        self.modifyTime=modifyTime
        
    def __repr__(self):
        return '<Company %>' % self.name