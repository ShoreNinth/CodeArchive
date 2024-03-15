#Exp10code1

# -*- coding: UTF-8 -*-
f=input("邮件内容所在文件：")
with open(f,'r') as fp:
    l=fp.readlines()
c=0
for text in l:
    for i in text:
         if ord(i)>32 and ord(i)<48:
              c+=1
         if ord(i)>90 and ord(i)<97:
              c+=1
if c>15:
    print("这封邮件是垃圾邮件。")
else:
    print("这封邮件是正常邮件。")
