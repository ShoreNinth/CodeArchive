#Exp9code5

# -*- coding: UTF-8 -*-
import re
string=str(input('请输入英文:'))

Match=re.sub(r'[\s.]I[\s.]','i' ,string)
print(Match)