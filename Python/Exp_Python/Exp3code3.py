#Exp3code3

# -*- coding: UTF-8 -*-

Y='是闰年'
N='不是闰年'
x=int(input('请输入一个四位年份：'))
if x%400==0:
    print(x,Y)
elif x%4==0:
    if x%100==0:
        print(x,N)
    else:
        print(x,Y)
else:
    print(x,N)