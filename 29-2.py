file_name=str(input("请输入需要打开的文件(C:\\\\test.txt):"))
f=open(file_name)
lines=int(input("请输入需要显示该文件前几行:"))
list1=list(f)

print("\n文件{0}的前{1}行的内容如下\n".format(file_name,lines))

for each_line in range(0,lines):
    print(list1[each_line])

f.close()
