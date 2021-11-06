def gcd1(a,b):
    if(a>b):
        while a%b!=0:
            r=a%b
            a=b
            b=r

        return b
    

    elif(a==b):
        return a

    else:
        while b%a!=0:
            r=b%a
            b=a
            a=r

        return a

a=int(input('a='))
b=int(input('b='))
print(gcd1(a,b))
