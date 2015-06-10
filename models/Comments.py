'''
Created on 2015-6-9

@author: Shuang.Wu

'''
from app import db

class Comments(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contents=db.Column(db.String(255),nullable=False)
    create_time=db.Column(db.String(20),nullable=False)
    user=db.Column(db.Integer,db.ForeignKey('user.id'))#"the user.id" is table "user" not the class User
    user=db.relationship('User',backref=db.backref("Comments",lazy='dynamic'))#here is class User
    company_id=db.Column(db.Integer,db.ForeignKey('company.id'))#"the company.id" is table "company" not the class Company
    company=db.relationship('Company',backref=db.backref('Comments',lazy='dynamic'))#here is class Company
    
    def __init__(self,contents,create_time,user,company):
        self.contents=contents
        self.create_time=create_time
        self.user=user
        self.company=company
        
    def __repr__(self):
        return '<Comments %r>' %self.id