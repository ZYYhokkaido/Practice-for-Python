class Nstr(str):
    def __init__(self,string):
        if type(string)==str:
            self.total=0
            for a in string:
                self.total+=ord(a)
        else:
            print("参数错误！")

    def __add__(self,other):
        return self.total+other.total

    def __sub__(self,other):
        return self.total-other.total

    def __mul__(self,other):
        return self.total*other.total

    def __truediv__(self,other):
        return self.total/other.total

    def __floordiv__(self,other):
        return self.total//other.total

a=Nstr("FishC")
b=Nstr("love")
print(a+b)
print(a/b)
print(a*b)
print(a-b)
print(a//b)
