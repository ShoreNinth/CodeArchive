#Exp9code3

# -*- coding: UTF-8 -*-
import string

pw=str(input('请输入密码字符串:'))
digit=0
lowercase=0
uppercase=0
mark=0
for i in pw:
    if i.isdigit():
        digit=1
    elif i.islower():
        lowercase=1
    elif i.isupper():
        uppercase=1
    else:
        mark=1
level=digit+lowercase+uppercase+mark
if level==1:
    print('该字符串作为密码是弱密码')
elif level==2:
    print('该字符串作为密码是中低密码')
elif level==3:
    print('该字符串作为密码是中高密码')
else:
    print('该字符串作为密码是强密码')