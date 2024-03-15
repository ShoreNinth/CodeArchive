#Exp3code7

# -*- coding: UTF-8 -*-

a=list(range(1,101))
sum=0
i=0
while i<100:
    sum+=a[i]
    i+=2
print('100以内所有奇数的和是',sum)
#最开始结果是2550，经过排查发现是全是偶数相加。
# a[i]是第i+1个元素，而不是第i个元素。