import easygui as g
import os

file_path=g.fileopenbox(default='*.txt')

file_name=os.path.basename(file_path)

with open(file_name) as f:
    old_file=f.read()
    new_file=g.textbox('文件[{0}]的内容如下:'.format(file_name),"显示文件内容",old_file)
    

if old_file!=new_file[:-1]:
    choice=g.buttonbox(msg="检测到文件内容发生改变，请选择以下操作：",choices=("覆盖保存","放弃保存","另存为"))
    if choice=="覆盖保存":
        f_write=open(file_name,"w")
        f_write.writelines(new_file)
        f_write.close()
    elif choice=="放弃保存":
        pass
    elif choice=="另存为":
        save_name=g.filesavebox(default='*.txt')
        f_write=open(save_name,"w")
        f_write.writelines(new_file)
        f_write.close()

                       
                



