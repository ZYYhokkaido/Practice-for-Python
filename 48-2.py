class MyRec:
    def __init__(self,arg):
        self.arg=arg
        self.index=len(arg)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index<0:
            raise StopIteration
        else:
            return self.arg[self.index]
        
myRec=MyRec("FishC")
for i in myRec:
    print(i,end='')
