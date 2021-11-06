def qiuhe(*canshu):
    base=3
    result=0
    for a in range(0,len(canshu)):
        result+=canshu[a]
        print(result)
        
    if canshu[len(canshu)-1]==5:
        base=5
        return result
    else:
        result*=base
        return result

print(qiuhe(1,2,3,4))
