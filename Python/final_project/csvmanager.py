import pandas as pd
#pandas需要下载
import numpy as np
#numpy需要下载
#最开始装的panda报错No module named 'request'
#已通过https://blog.csdn.net/aliexken/article/details/122612099 解决

students_info=pd.read_csv("students_info.csv")
_number=students_info["序号"]
_name=students_info["姓名"]
_gender=students_info["性别"]
_school_number=students_info["学号"]

number_array=np.array(_number)
name_array=np.array(_name)
gender_array=np.array(_gender)
school_number_array=np.array(_school_number)

#转列表不然无法删除元素
number_list=list(number_array)
name_list=list(name_array)
gender_list=list(gender_array)
school_number_list=list(school_number_array)

def editor(i):
    del number_list[-1]
    del gender_list[i]
    del name_list[i]
    del school_number_list[i]

    #转回数组，方便写入csv
    number_array_edited=np.array(number_list)
    name_array_edited=np.array(name_list)
    gender_array_edited=np.array(gender_list)
    school_number_array_edited=np.array(school_number_list)

    list=[number_array_edited,name_array_edited,gender_array_edited,school_number_array_edited]
    name=['序号','姓名','性别','学号']
    print(len(number_array_edited),len(name_array_edited),len(gender_array_edited),len(school_number_array_edited))
    writer=pd.DataFrame({name[0]:number_array_edited,name[1]:name_array_edited,name[2]:gender_array_edited,name[3]:school_number_array_edited})
    writer.to_csv('final_project\students_info.CSV',index=False)
