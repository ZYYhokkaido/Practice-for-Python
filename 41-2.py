class Cal(int):
    def __new__(cls,string):
        num=0
        if type(string)==str:
            for a in range(0,len(string)):
                num += ord(string[a])
            return int.__new__(cls,num)

        else:
            return int.__new__(cls,string)

c=Cal('A')
print(c)
