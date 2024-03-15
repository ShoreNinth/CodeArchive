#Exp5code4

# -*- coding: UTF-8 -*-
#输入值限制
while True:
    a=int(input('请输入一个大于2的自然数:'))
    if a==2 or a<2:
        print("错误：您输入的值无效，请重新输入一个大于2的自然数：")
    else:
        break

PrimeNumList=[i for i in range(2,a)]
DelNumList=[]
for j in PrimeNumList:
    i=2
    while 1:
        Remainder=j%i
        if j == i:
            break
        if Remainder == 0:
            DelNumList.append(j)
            break
        if Remainder != 0:
            i=i+1

for i in DelNumList:
    if i in PrimeNumList:
        PrimeNumList.remove(i)
print(PrimeNumList)
