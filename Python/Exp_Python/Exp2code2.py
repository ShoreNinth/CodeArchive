#Exp2code2

#!/usr/bin/python
# -*- coding: UTF-8 -*-

a=int(input('请输入一个四位自然数：'))

#千位
b=a // 1000
#百位
c=(a//100)%10
#十位
d=(a//10)%10
#个位
e=a%10
print(b,c,d,e)