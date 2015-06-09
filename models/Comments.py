'''
Created on 2015-6-9

@author: Shuang.Wu

'''
from app import db

class Comments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contents=db.Column(db.String(255),nullable=False)
    create_time=db.Column(db.String(20),nullable=False)
    user=db.Column(db.Integer,db.ForeignKey('User.id'))
    company_id=db.Column(db.Integer,db.ForeignKey('Company.id'))
    company=db.relationship('Company',backref=db.backref('Comments',lazy='dynamic'))
    
    def __init__(self,contents,create_time,user,company):
        self.contents=contents
        self.create_time=create_time
        self.user=user
        self.company=company
        
    def __repr__(self):
        return '<Comments %r>' %self.id

def init_db():
    """
        此方法用来创建comments表,请在未创建comments表时使用
    """
    db.create_all()