#Exp4code1
# -*- coding: UTF-8 -*-

import random
i=1
a=0
b=0
c=0

for i in range(10001):
    number=random.randint(0, 360)
    if number<30:
        a+=1
    elif number<108:
        b+=1
    else:
        c+=1
print('模拟完成。一等奖抽中',a,'次，','二等奖抽中',b,'次，','三等奖抽中',c,'次。')