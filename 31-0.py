import pickle

f_read=open('record.txt')
boy=[]
girl=[]
count=0

for each_line in f_read:
    if each_line[:6]!='======':
        (role,words)=each_line.split(':',1)
        if role=='小甲鱼':
            boy.append(words)
        elif role=='小客服':
            girl.append(words)
    
    else:
        count+=1
        file_name='小甲鱼_'+str(count)+'.txt'
        f_write=open(file_name,"wb")
        pickle.dump(boy,f_write)
        f_write.close()

        file_name='小客服_'+str(count)+'.txt'
        f_write=open(file_name,"wb")
        pickle.dump(girl,f_write)
        f_write.close()

        boy=[]
        girl=[]

count+=1
file_name='小甲鱼'+str(count)+'.txt'
f_write=open(file_name,"wb")
pickle.dump(boy,f_write)
f_write.close()

file_name='小客服'+str(count)+'.txt'
f_write=open(file_name,"wb")
pickle.dump(girl,f_write)
f_write.close()

f.close()


