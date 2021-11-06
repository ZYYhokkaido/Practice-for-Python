name=str(input("请输入文件名："))
f=open(name,"x")

print("请输入内容[单独输入':w'保存退出]")

while True:
    input_user=str(input())
    if input_user==':w':
        break
    else:
        f.write(input_user+'\n')
    
    
f.close()
    
