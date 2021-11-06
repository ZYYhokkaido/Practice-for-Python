import os
import easygui as g

path=g.diropenbox("请选择您的代码库","浏览文件夹")

a=os.listdir(path)
print(a)
count_py=0
count_py_num=0
count_c=0 #行数
count_c_num=0 #文件数


for file in a:
    if file[-3:]==".py":
        count_py_num+=1
        f=open(file)
        count_py+=len(list(f))
    
    if file[-2:]==".c":
        count_c_num+=1
        f=open(file)
        count_c+=len(list(f))

sum_count=count_py+count_c
persent=sum_count/100000*100

g.textbox(msg="您总共积累编写了{0}行代码，完成进度：{1}%\n离10万行代码还差{2}行，请继续努力！".format(sum_count,persent,100000-sum_count),title="代码行数统计结果",
text="[.py]源文件%d个,源代码%d行\n[.c]源文件%d个,源代码%d行\n"%(count_py_num,count_py,count_c_num,count_c))
        


        

        
