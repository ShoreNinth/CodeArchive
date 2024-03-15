#Exp6code4

# -*- coding: UTF-8 -*-
import random

totime=int(input('请输入投掷飞镖次数：'))

intime=0
i=0
while i!=totime:
    #random.random()生成浮点数的范围是[0,1)，可设置为x,y各有50%的概率变为负数
    x=random.random()
    a=random.randint(0,1)
    if a==0:
        x=-x
    y=random.random()
    b=random.randint(0,1)
    if b==0:
        y=-y
    if x*x + y*y <= 1:
        intime+=1
    i+=1
pie=float((intime/totime)* 4)
print('本次所求圆周率是：',pie)
