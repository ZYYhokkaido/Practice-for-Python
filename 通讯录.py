tongxunlu={}
print("|---欢迎进入通讯录程序---|")
print("|---1.查询联系人资料---|")
print("|---2.插入新的联系人---|")
print("|---3.删除已有联系人---|")
print("|---4.退出通讯录程序---|")

shuru=0
while shuru!=4:
    shuru=int(input("\n请输入相关的指令代码:"))
    
    if shuru==2:
        name=str(input("请输入联系人姓名:"))
        
        if name not in tongxunlu:
            number=input("请输入用户联系电话:")
            tongxunlu[name]=number
            print("已成功输入联系人，您可进行其他操作")
            
        else:
            print("您输入的姓名在通讯录中已存在 -->> {0}:{1}".format(name,tongxunlu[name]))
            change=str(input("是否修改用户资料(YES/NO):"))
            if change=="YES":
                number=input("请输入用户联系电话:")
                tongxunlu[name]=number
                print("已成功输入联系人，您可进行其他操作")
                
            elif change=="NO":
                print("联系人信息保持不变，您可进行其他操作")
                continue
    

    elif shuru==1:
        name=str(input("请输入联系人姓名:"))
        if name in tongxunlu:
            print("{0}:{1}".format(name,tongxunlu[name]))

        if name not in tongxunlu:
            print("您输入的联系人不存在，您可进行其他操作")

    elif shuru==3:
        name=str(input("请输入您想删除的联系人的姓名:"))
        tongxunlu.pop(name)
        print("已成功删除联系人，您可进行其他操作")

print("|---感谢使用通讯录程序---|") 
