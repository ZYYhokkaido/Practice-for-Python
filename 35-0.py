import random
import easygui as e

time=3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
temp = e.enterbox("不妨猜一下胖子现在心里想的是哪个数字(1~10)：","数字小游戏")
guess = int(temp)
if guess!=secret:
    e.msgbox("不对哦～再试一次叭(还剩下{0}次机会)".format(time),'数字小游戏',"加油！")
while guess != secret and time>=1:
    temp = temp = e.enterbox("不妨猜一下胖子现在心里想的是哪个数字(1~10)(还剩下{0}次机会)：".format(time),"数字小游戏")
    guess = int(temp)
    if guess == secret:
        break
    else:
        if guess > secret:
            e.msgbox("大了！",'数字小游戏',"加油!")
            time-=1
        else:
            e.msgbox("小了！",'数字小游戏',"加油!")
            time-=1

if guess==secret:
    e.msgbox("猜中啦！奖励亲亲一枚",'数字小游戏',"点击领取奖励")
else:
    e.msgbox("真可惜呀～",'数字小游戏')
