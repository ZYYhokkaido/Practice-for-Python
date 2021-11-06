file_name=str(input("请输入需要打开的文件(C:\\\\test.txt):"))
f=open(file_name)
list1=list(f)
lines=str(input("请输入需要显示的行数[格式如13:21或:21或21:]:"))
(left,right)=lines.split(':',1)
if left=='':
    left=1
if right=='':
    right=len(list1)

left=int(left)
right=int(right)

if left!=1 and right!=len(list1):
    print("\n从第{0}行到第{1}行的内容如下:\n".format(left,right))

elif left==1 and right!=len(list1):
    print("\n从开始到第{0}行的内容如下:\n".format(right))

elif left!=1 and right==len(list1):
    print("\n从第{0}行到末尾的内容如下:\n".format(left))

elif left==1 and right==len(list1):
    print("\n从开始到末尾的内容如下:\n")


for each_line in range(left-1,right):
    print(list1[each_line])

f.close()
