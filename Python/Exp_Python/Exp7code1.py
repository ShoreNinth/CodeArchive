#Exp7code1

# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

city=['Beijing','Shanghai','London','Boston','New York','Paris','Tokyo','Seoul','Los Angeles','Moscow','San Francisco','Toronto','Chicago','Berlin','Singapore','Hong Kong','Shenzhen','Stockholm','Osaka','Amsterdam']
cor=[476644,232201,187324,185779,161885,129790,128862,127102,110414,109533,93371,83356,78414,75502,74841,61547,55508,51760,50866,50490]

Cor=sorted(cor)
city.reverse()

plt.barh(city, Cor)
plt.title('全球永久定居科研人员数量前20的城市')

plt.show()
