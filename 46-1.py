import time as t

class Record:
    def __init__(self,value=None,name=None):
        self.value=value
        self.name=name

    def __get__(self,instace,owner):
        f=open("record.txt","a")
        print("{0}变量于北京时间 {1} 被读取, {2} = {3}".format(self.name,t.ctime(),self.name,self.value))
        f.write("{0}变量于北京时间 {1} 被读取, {2} = {3}\n".format(self.name,t.ctime(),self.name,self.value))
        f.close()
        return self.value

    def __set__(self,instance,value=None):
        f=open("record.txt","a")
        self.value=value
        print("{0}变量于北京时间 {1} 被修改, {2} = {3}".format(self.name,t.ctime(),self.name,self.value))
        f.write("{0}变量于北京时间 {1} 被修改, {2} = {3}\n".format(self.name,t.ctime(),self.name,self.value))
        f.close()

class Test:
    x=Record(10,'x')
    y=Record(8.8,'y')


