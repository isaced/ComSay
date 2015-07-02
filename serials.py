'''
Created on 2015-7-2

@author: Shuang.Wu
'''

import inspect


def getDict(entity):
    members=inspect.getmembers(entity)
    obj=None
    for sers in members:
        if sers[0]=="__dict__":
            obj=sers[1]
    del obj["_sa_instance_state"]
    return obj
