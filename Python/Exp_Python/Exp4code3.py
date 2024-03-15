#Exp4code3

# -*- coding: UTF-8 -*-
#写了几个小时终于写出来了

import random,itertools
#最开始用的combinations函数，但是发现不够理想：这个函数更适合排列，而不是组合
#调试时发现打印的列表不全

#创建一个包含0~9数字的列表a
a=[]
for i in range(10):
    a.append(str(i))

#创建用于存放所有可能四位数组合的列表b
b=list(itertools.permutations(a,4))

#c用于存放有意义的四位数，即千位数字不为0的数
c=[]
for i in range(len(b)):
    x=''.join(b[i])
    c.append(x)

#三位数最大的为0987，而这些数都是排好顺序的，故可以用循环删去
x=c.index('0987')
i=x
while i!=-1:
    del c[i]
    i-=1
#随机从列表c中抽取一个数
y=str(random.sample(c, 1))

#如果循环进行了第8次，那么卡普耶卡的发现就是错误的（当然，第8次循环不应该会发生）
counter=0
#列表d用于存放第一次拆分后的四个数字
d=[y[5],y[2],y[3],y[4]]

while 1:
    #列表e用于存放组合
    e=list(itertools.permutations(d, 4))
    #列表f用于存放所选出的数字的重新组合
    f=[]
    for i in range(len(e)):
        x=''.join(e[i])
        f.append(x)
    i=0
    while i in range(len(f)):
        f[i]=int(f[i])
        i+=1
    #剔除f里的“非四位数”
    Max=max(f)
    Min=min(f)
    temp=Max-Min
    counter+=1
    if counter==8:
        print('错误：循环进行了8次。程序已停止')
        break
    if temp==6174:
        print('此猜想正确，循环共执行了',counter,'次')
        break
    else:
        print('第',counter,'次循环结束，但差不为6174.')
        d=str(temp)