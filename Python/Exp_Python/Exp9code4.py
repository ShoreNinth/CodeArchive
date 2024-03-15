#Exp9code4

# -*- coding: UTF-8 -*-
#参考了https://ask.csdn.net/questions/7562348
texts = input("请输入英文:").split(" ")
try:
    while(True):
        i = texts.index("i")
        texts[i]="I"
except:
    text = " ".join(texts)
    print(text)