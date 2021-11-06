name1=str(input("请输入需要比较的头一个文件名："))
name2=str(input("请输入需要比较的另一个文件名："))

f1=open(name1,"r")
f2=open(name2,"r")

list1=list(f1)
list2=list(f2)
number=[]
count=0

if len(list1) <= len(list2):
    for line in range(0,len(list1)):
        if list1[line]!=list2[line]:
            count+=1
            number.append(line+1)

else:
    for line in range(0,len(list2)):
        if list1[line]!=list2[line]:
            count+=1
            number.append(line+1)

print("两个文件共有[%d]处不同"%count)
for a in range(0,count):
    print("第%d行不一样"%number[a])


