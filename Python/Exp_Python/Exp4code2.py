#Exp4code2

# -*- coding: UTF-8 -*-
#部分参考了https://blog.csdn.net/weixin_43518405/article/details/109148075
from  itertools import cycle

while 1:
    n=int(input('请输入初始人数：'))
    if n==1:
        print('对影成三人？重来！')
    else:
        break

k=int(input('请输入报数临界值：'))
r=[]

print('-----游戏开始-----')
for i in range(1,n+1):
    r.append(i)

counter=1
x=cycle(r)
while len(r)!=1:
    print(next(x),'号报了',counter)
    # r.append(r.pop(0))
    #这是原作者的代码：通过将报数者移至列表末尾形成环
    counter += 1
    if counter == k:
        print(r[0],'报了',k,'，退出圈子')
        del r[0]
        counter = 1
print(r,'号最后留了下来')