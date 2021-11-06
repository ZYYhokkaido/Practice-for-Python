import math as m

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


class line:
    def __init__(self,point1,point2):
        self.point1=point1
        self.point2=point2

    def getLen(self):
        line_len=m.sqrt(m.pow((self.point1.x-self.point2.x),2)+m.pow((self.point1.y-self.point2.y),2))
        print(line_len)

point1=point(1,1)
point2=point(1,1)

line=line(point1,point2)
line.getLen()
