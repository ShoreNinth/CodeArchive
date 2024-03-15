#Exp10code2

# -*- coding: UTF-8 -*-
from random import randint

def guessNumber(maxValue,maxTimes):
    value=randint(1,maxValue)
    for i in range(maxTimes):
        prompt='请输入您猜的数字:'if i==0 else '请再猜一次:'
        try:
            x=int(input(prompt))
        except:
            print('必须输入整形数，且在数字1和',maxValue,'之间')
        else:
            if x==value:
                print('恭喜您，猜对了!')
                break
            elif x>value:
                print('太大了！')
            else:
                print('太小了！')
    else:
        print('游戏结束，您失败了！')
        print('正确答案是：',value)

a=int(input('请输入最大值：'))
b=int(input('请输入最多猜数次数：'))
guessNumber(a,b)
