#Exp3code6

# -*- coding: UTF-8 -*-
#思路参考了https://blog.csdn.net/intials_gys/article/details/84144000，但写完代码后我觉得我比ta强(滑稽)

#输入值限制
while True:
    a=int(input('请输入一个小于1000的整数:'))
    if a<2 or a>999:
        print("错误：输入值超出范围")
    else:
        break
print(a,'=')

i=2
while True:
    Remainder=a%i
#第一个if语句必须比第二个优先，不然输入2就会输出：
#2 =
#2 *
#然后卡住。因为a变成了1，这时候程序就一脸懵了。想避免这个错误，最简单的方法应该就是把这个if语句提前。
    if a==i:
        print(i)
        break
    if Remainder == 0:
        print(i,'*')
        a=a//i
    if Remainder != 0:
        i=i+1