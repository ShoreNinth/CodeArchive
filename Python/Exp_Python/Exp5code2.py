#Exp5code2

# -*- coding: UTF-8 -*-
import random

a=[random.randint(0,10000) for i in range(20)]
b=sorted(a[0:10])
c=sorted(a[-10:],reverse=True)

print(b+c)