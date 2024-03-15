#Exp9code6

# -*- coding: UTF-8 -*-
#参考了https://blog.csdn.net/m0_37639542/article/details/70169816
import re
words=input("请输入英文:")
l=re.split('[\. ]+',words)
print(l)
i=0
for i in l:
    if len(i)==3:
        print(i)
    else:
        print('')