list1=['1.Just do it','2.一切皆有可能','3.让编程改变世界','4.Impossible is nothing']
list2=['4.阿迪达斯','2.李宁','3.鱼c工作室','1.耐克']

list3=[(list2[y]+':'+list1[x][2:]) for x in range(len(list1)) for y in range(len(list2)) if list1[x][0]==list2[y][0]]

print(list3)
