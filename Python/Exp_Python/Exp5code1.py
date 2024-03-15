#Exp5code1

# -*- coding: UTF-8 -*-
import time,random
T1=time.perf_counter()
List=[]
Tuple=()
Dict={}
Set=set()

#添加耗时统计
List=[random.randint(1, 10001) for i in range(1000)]
T2=time.perf_counter()

Tuple=tuple(random.randint(1, 10001) for i in range(1000))
T3=time.perf_counter()

#字典生成思路：把列表中的第i(1<=i<=500)项和第i+500项分别组合成键值对
for i in range(500):
    Dict[List[i]]=List[500+i]
T4=time.perf_counter()

Set={random.randint(1, 10001) for i in range(1000)}
T5=time.perf_counter()
print('-------增加元素-------')
print('列表耗时:',T2-T1,'微秒')
print('元组耗时:',T3-T2,'微秒')
print('字典耗时:',T4-T3,'微秒')
print('集合耗时:',T5-T4,'微秒')

#删除耗时统计
#将它们的前100项删除（字典和元组例外。字典为前50组键值对，元组因不能修改元素而不参与本次统计）
i=99
T6=time.perf_counter()
while i!=-1:
    del Dict[List[i]]
    i-=1
T7=time.perf_counter()

i=99
T8=time.perf_counter()
while i!=-1:
    Set.discard(list[i])
    i-=1
T9=time.perf_counter()

i=99
T10=time.perf_counter()
while i!=-1:
    del List[i]
    i-=1
T11=time.perf_counter()

print('-------删除元素-------')
print('列表耗时:',T11-T10,'微秒')
print('字典耗时:',T7-T6,'微秒')
print('集合耗时:',T9-T8,'微秒')

#查找耗时统计
#分别随机抽取100个元素（字典例外。字典为50组键值对）
a=random.sample(List, 100)
T12=time.perf_counter()       
for i in range(100):
    List.index(a[i])
T13=time.perf_counter()

a=random.sample(Tuple, 100)
T14=time.perf_counter()
for i in range(100):
    Tuple.index(a[i])
T15=time.perf_counter()

a=sorted(Dict)

T16=time.perf_counter()
for i in range(50):
    Dict.get(a[i])
T17=time.perf_counter()

Set_2=[]
for i in range(100):
    element=random.choice(list(Set))
    Set_2.append(element)

T18=time.perf_counter()
for i in range(100):
    if Set_2[i] in Set:
        pass
T19=time.perf_counter()
print('-------查找元素-------')
print('列表耗时:',T13-T12,'微秒')
print('元组耗时:',T15-T14,'微秒')
print('字典耗时:',T17-T16,'微秒')
print('集合耗时:',T19-T18,'微秒')

#排序耗时统计
#将它们分别按正序排序
T20=time.perf_counter()
List=sorted(List)
T21=time.perf_counter()

T22=time.perf_counter()
Tuple=tuple(sorted(list(Tuple)))
T23=time.perf_counter()

T24=time.perf_counter()
Dict=sorted(Dict)
T25=time.perf_counter()

T26=time.perf_counter()
Set=sorted(Set)
T27=time.perf_counter()

print('-------排序元素-------')
print('列表耗时:',T21-T20,'微秒')
print('元组耗时:',T23-T22,'微秒')
print('字典耗时:',T25-T24,'微秒')
print('集合耗时:',T27-T26,'微秒')

# -------增加元素-------
# 列表耗时: 0.0027072000000000207 微秒
# 元组耗时: 0.0025915999999999717 微秒
# 字典耗时: 0.00019540000000001223 微秒
# 集合耗时: 0.0023152000000000172 微秒
# -------删除元素-------
# 列表耗时: 3.289999999994686e-05 微秒
# 字典耗时: 4.399999999998849e-05 微秒
# 集合耗时: 5.189999999999362e-05 微秒
# -------查找元素-------
# 列表耗时: 0.00032240000000000046 微秒
# 元组耗时: 0.00029970000000001384 微秒
# 字典耗时: 1.3900000000011126e-05 微秒
# 集合耗时: 2.9500000000015625e-05 微秒
# -------排序元素-------
# 列表耗时: 7.819999999997274e-05 微秒
# 元组耗时: 7.930000000000437e-05 微秒
# 字典耗时: 2.7200000000004998e-05 微秒
# 集合耗时: 6.430000000001712e-05 微秒