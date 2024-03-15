#Exp2code3

#!/usr/bin/python
# -*- coding: UTF-8 -*-
#参考了https://blog.csdn.net/qq_43505736/article/details/108607542

lstA=input('输入第一个列表的元素(用空格隔开):')
lstA=list(lstA)
lstB=input('输入第二个列表的元素(依旧用空格隔开):')
lstB=list(lstB)
#字典名为d1ct
d1ct=dict()
d1ct=dict(zip(lstA,lstB))

#去除空格
"""
这里多了一行代码，用于去除空格。

去除前：
输入第一个列表的元素(用空格隔开):1 2 3 4
输入第二个列表的元素(依旧用空格隔开):A B C D E
{'1': 'A', ' ': ' ', '2': 'B', '3': 'C', '4': 'D'}

去除后：
输入第一个列表的元素(用空格隔开):1 2 3 4
输入第二个列表的元素(依旧用空格隔开):A B C D E
{'1': 'A', '2': 'B', '3': 'C', '4': 'D'}

"""
del d1ct[" "]

print(d1ct)