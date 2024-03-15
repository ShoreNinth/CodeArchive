#Exp6code3

# -*- coding: UTF-8 -*-
#使用了原创命令系统
import random

#设全班共有20人，分别为A,B,C,...,R,S,T将他们顺序打乱，然后分别对应20个成绩
name=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
random.shuffle(name)
#随机数遵循平均值为70，标准差为10的正态分布，保留两位小数
result=['%.2f' % random.gauss(70, 10) for i in range(20)]
student={}
i=0
while i!=19:
    student[name[i]]=result[i]
    i+=1

#由值求键函数，此函数来自https://www.delftstack.com/howto/python/python-dictionary-find-key-by-value/
def get_key(val):
    for key, value in student.items():
         if val == value:
            return key

cmd=['/search','/max','/ave','/exit','/help']
navi=str(input("输入 /search 以查询成绩\n输入 /max 以查看最高分信息\n输入 /ave 以查看本班平均成绩\n输入 /exit 以退出\n输入 /help 以查看指令列表\n"))
while 1:
    if navi =='/search':
        nameinput=str(input('请输入学生姓名：'))
        print(nameinput,'的成绩是',student[nameinput],'分')
    if navi =='/max':
        print(get_key(max(result)),':',max(result))
    if navi =='/ave':
        sum=0
        for i in result:
            sum+=(float(i)/20)
        sum='%.2f' % sum
        print('平均成绩是',sum,'分')
    if navi =='/help':
        print("/search 查询成绩\n/max 查看最高分信息\n/ave 查看本班平均成绩\n/exit 退出\n/help 查看指令列表")
    if navi =='/exit':
        break
    if navi not in cmd:
        print('指令输入错误。请使用 /help 查看命令列表')
    navi=str(input('请输入下一步命令：'))
