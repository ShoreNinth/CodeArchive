#Exp3code5

# -*- coding: UTF-8 -*-
import random

x=[random.randint(1, 101) for  i in range(20)]

y=x[::2]
y.sort()
y.reverse()
print(y)