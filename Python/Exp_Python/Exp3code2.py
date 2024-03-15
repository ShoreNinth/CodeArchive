#Exp3code2

# -*- coding: UTF-8 -*-

x=int(input('请输入x的值：'))
if x<0:
    y=0
elif 0<=x<5:
    y=x
elif 5<=x<10:
    y=3*x-5
elif 10<=x<20:
    y=0.5*x-2
elif 20<=x:
    y=0
print(y)