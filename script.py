'''
Created on 2015-6-10
    此此脚本用来创建models中的表,请在未创建表时使用
    如果要建立的表中有外键，则该表的python见表语句
    不能单独调用，必须和其他表的见表语句一起调用，否
    则会抛出NoReferencedTableError错误
@author: Shuang.Wu
'''
from app import db


from models import Company,User,Comments
db.create_all()







