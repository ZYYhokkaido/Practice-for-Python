def count(*text):
    for b in range(0,len(text)):
        number=0
        alphabet=0
        else1=0
        skip=0
        for a in range(0,len(text[b])):
            if ord(text[b][a])<=57 and ord(text[b][a])>=49:
                number+=1

            elif (ord(text[b][a])<=90 and ord(text[b][a])>=65)or(ord(text[b][a])<=122 and ord(text[b][a])>=97):
                alphabet+=1

            elif ord(text[b][a])==32:
                skip+=1

            else:
                else1+=1
            
        print("第{0}个字符串共有：英文字母{1}个，数字{2}个，空格{3}个，其他字符{4}个。".format(b+1,alphabet,number,skip,else1))

count("I love money!","I don't like money!!!")
