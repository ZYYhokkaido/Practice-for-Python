def compare(first,second,test):
    count=0
    for a in range(0,len(test)):
        if test[a]==first and test[a+1]==second:
            count+=1

    return count

test=input('请输入目标字符串:')
semi=input('请输入子字符串(两个字符):')
first=semi[0]
second=semi[1]

print("子字符串在目标字符串中共出现{0}次".format(compare(first,second,test)))





        
