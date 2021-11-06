def myRec(x):
    index=len(x)
    while index>0:
        index-=1
        yield x[index]
        
        

for i in myRec("FishC"):
    print(i,end='')
