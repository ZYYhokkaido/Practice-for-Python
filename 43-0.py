class A:
    count=0
    def __init__(self,*x):
        self.count=len(x)
        print("传入了{0}个参数, 他们分别是：".format(self.count),end='')
        for a in x:
            print("{0}".format(a),end=' ')

a=A(1,2,3)
    
