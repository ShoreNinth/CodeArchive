#Exp7code2

# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

country=['美国','中国','日本','德国','韩国','法国','英国','澳大利亚','加拿大','意大利','瑞士','以色列','荷兰','巴西','瑞典','其他国家']
expenditure=[6075,4680,1264,1189,697,638,544,309,285,280,266,237,208,197,177,2506]

MD3={'#83F8CD','#E6DEFF','#CEE5FF','#BBF294','#FFE084','#FFDCBB','#FFDADA','#D1E4FF','#B1EBFF','#FFDEAA','#CCEE99','#FFDBCA','#FFEEB2','#FFD6FE','#E7DEFF','#5C76AA'}
explode=[0.05,0.05,0.05,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.05,]

plt.pie(expenditure,labels=country,textprops={'color':'#4286F3'},colors=MD3,autopct='%1.1f%%',explode=explode,radius=0.8)
plt.title('2021年全球国家科研经费排名')

plt.show()
