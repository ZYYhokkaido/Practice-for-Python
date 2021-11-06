def find(x):
    count=0
    hundred=int(x/100)
    ten=int((x-hundred*100)/10)
    one=x-hundred*100-ten*10

    if x==hundred**3+ten**3+one**3:
        print(x)

for x in range(100,999):
    find(x)
