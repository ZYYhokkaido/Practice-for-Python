file_name=str(input("请输入文件名:"))
word=str(input("请输入需要替换的单词或字符:"))
new_word=str(input("请输入新的单词或字符:"))

f=open(file_name)
count=0

list1=list(f)
f.close()
for each_line in range(0,len(list1)):
    for a in range(0,len(list1[each_line])):
        if list1[each_line][a]==word:
            count+=1

print("文件{0}中共有{1}个[{2}]".format(file_name,count,word))
print("您确定把所有的[{0}]替换成[{1}]吗？".format(word,new_word))
judge=str(input("[YES/NO]"))

write=open(file_name,'w')

if judge=='YES' or 'yes' or 'Yes':
    """
    for each_line in range(0,len(list1)):
        for a in range(0,len(list1[each_line])):
            if list1[each_line][a]==word:
                list1[each_line][a]=new_word
    """
    for each_line in range(len(list1)):
        list1[each_line]=list1[each_line].replace(word,new_word)

write=open(file_name,'w')
write.writelines(list1)

write.close()





