import pickle as p
import os

class MyDes:
    def __init__(self,name=None):
        self.name=name

    def __set__(self,instance,value):
        output=open("{0}.pkl".format(self.name),"wb")
        self.value=value
        p.dump(self.value,output)
        output.close()

    def __get__(self,instance,owner):
        return self.value

    def __delete__(self,instance):
        os.remove("{0}.pkl".format(self.name))
    

class Test:
    x=MyDes('x')
    y=MyDes('y')
