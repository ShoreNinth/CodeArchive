#Exp5code4

# -*- coding: UTF-8 -*-
import random
a=[random.randint(1,10000) for i in range(1000)]
print(len(a))
b=[i for i in a if i%2!=0 ]
