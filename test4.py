def convert(x):
    list1=[]
    result=[]
    a=0
    while x/2!=0:
        temp=x%2
        list1.append(temp)
        x=int(x/2)
        print(x)

    result=list(reversed(list1))
    return result

x=int(input('x='))
print(convert(x))
