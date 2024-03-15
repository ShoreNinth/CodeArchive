#Exp2code4

#!/usr/bin/python
# -*- coding: UTF-8 -*-
#参考了https://blog.csdn.net/weixin_43980115/article/details/104859967
list=eval(input('输入一个列表:'))
list_R=sorted(list,reverse=True)
print(list_R)

'''最开始没用eval函数，输出结果是：

输入一个列表:1，2，3
['，', '，', '3', '2', '1']

逗号不该出现在这里，故需eval函数将其筛去
'''