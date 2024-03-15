#Exp3code4

# -*- coding: UTF-8 -*-

import random
a=[random.randint(0, 100) for i in range(50)]

i=49
while i!=0:
    if a[i]%2==1:
        del a[i]
    i=i-1
print(a)