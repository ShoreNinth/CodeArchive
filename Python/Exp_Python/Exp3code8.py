#Exp3code8

# -*- coding: UTF-8 -*-

#自定义筛选函数，灵感来自上个实验的因式分解
#最开始用自定义函数报错了，发现原因是定义的函数必须要在调用之前出现，也就是说，Python源代码是由上往下解析的
def screen(x):
    j=2
    while True:
        Remainder=x%j
        if x == j:
            print(x,'是质数')
            break
        if Remainder == 0:
            break #合数无需输出
        if Remainder != 0:
            j+=1 

import itertools
a=['1','2','3','4']
#空列表c用于存放未经过筛选的数
c=[]
for a in itertools.permutations(a,4):
    b=a[0]+a[1]+a[2]+a[3]
    c.append(int(b))

#筛选
i=0
while i<24:
    screen(c[i])
    i+=1