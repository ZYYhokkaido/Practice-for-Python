"""
def f(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return f(n-1)+f(n-2)

"""
def f(n):
    list1=[]
    for a in range(0,n):
        if a==0:
            list1.append(1)
        elif a==1:
            list1.append(1)
        else:
            list1.append(list1[a-1]+list1[a-2])

    return list1[a]


n=int(input('请输入一个正整数:'))
print(f(n))  
