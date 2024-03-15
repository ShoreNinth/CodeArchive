#Exp9code1

# -*- coding: UTF-8 -*-
import string
s = input('请输入一个字符串:')
letters = 0
space = 0
digit = 0
others = 0
i = 0
while i < len(s):
    oneword = s[i]  # 获取每个位置的值
    i += 1
    if oneword.isalpha():  # 判断是否是字母
        letters += 1
    elif oneword.isdigit(): # 判断是否为数字
        digit += 1
    elif oneword.isspace(): # 判断是否为空格
        space += 1
    else:
        others += 1
print('字符总数为：',len(s),'个')
print('英文字母个数:',letters,'个')
print('数字个数：',digit,'个')
print('空格个数：',space,'个')
print('其他字符个数：',others,'个')
