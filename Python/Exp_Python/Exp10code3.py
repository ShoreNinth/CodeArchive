#Exp10code3

# -*- coding: UTF-8 -*-
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

goal=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
a=[]
nterms = len(goal)+1
if nterms <= 0:
   print("输入正数")
else:
   for i in range(nterms):
        a.append(recur_fibo(i))
print("斐波那契数列:",a)
