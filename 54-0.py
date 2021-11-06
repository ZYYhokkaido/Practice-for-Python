import urllib.request
import easygui as g

value = g.multenterbox("请填写喵的尺寸","下载一只喵",["宽","高"],values=[400,600])

choice_width=value[0]
choice_height=value[1]

response=urllib.request.urlopen("http://placekitten.com/g/%s/%s"%(value[0],value[1]))
cat_img=response.read()

path=g.diropenbox("请选择存放喵的文件夹：","浏览文件夹")

with open('%s//cat_%s_%s.jpg'%(path,value[0],value[1]),'wb') as f:
    f.write(cat_img)
