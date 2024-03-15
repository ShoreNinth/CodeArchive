#Exp9code2
#凯撒加密
# -*- coding: UTF-8 -*-

s = input('请输入一个字符串:')
k = int(input('请输入密钥：'))

lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
encrypt=[]
for word in s:
    if word in lower_case:
        index1=lower_case.index(word)
        if index1>26-k:
            index1-=26
        encrypt.append(lower_case[index1+k])
    elif word in upper_case:
        index2=upper_case.index(word)
        if index2>26-k:
            index2-=26
        encrypt.append(upper_case[index2+k])
    else:
        encrypt.append(word)
result=''
for i in encrypt:
    result=result+i
print('凯撒加密结果为:',result)