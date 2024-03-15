# -*- coding: utf-8 -*-
# 作者：郭昭阳
# 学号：202178030309

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import json
import pandas as pd
import numpy as np
import csv

import logger
import csvmanager

window_login = tk.Tk()
window_login.geometry('300x250')
window_login.title('学生信息管理系统')
window_login.iconphoto(False, tk.PhotoImage(file='.\icons\login.png'))

def _main_():
    window_main=tk.Tk()
    window_main.title('学生信息管理系统')
    window_main.iconphoto(False, tk.PhotoImage(file='.\icons\home.png'))

    def add():
        window_add=tk.Toplevel(window_main)
        window_add.geometry('350x250')
        window_add.title('添加')
        window_add.iconphoto(False, tk.PhotoImage(file='.\icons\_add.png'))

        def csv_add():
            ng = new_gender.get()
            nn_=new_name_.get()
            nsn = new_school_number.get()
            #姓名、性别可以重复，但学号不会。
            if nsn in csvmanager.school_number_array:
                tk.messagebox.showerror('错误', '用户名已存在')
            elif ng == '' or nn_ == '' or nsn == '':
                tk.messagebox.showerror('错误', '缺少信息')
            # 注册信息没有问题则将信息写入数据库
            else:
                #这里这个转化步骤是无奈之举
                #TypeError: can only concatenate str (not "int") to str
                if ng == 0:
                    ng='女'
                else:
                    ng='男'
                with open(file='students_info.CSV',mode='a', encoding='utf-8') as f:
                    f.write(str(csvmanager.number_array[-1]+1)+','+nn_+','+ng+','+nsn+'\n')

                    #python警告FutureWarning: elementwise comparison failed; returning scalar instead, but in the future will perform elementwise comparison

                tk.messagebox.showinfo('提示','添加成功')
                logger.login_activity()
                with open(file='log.txt',mode='a', encoding='utf-8') as f:
                    f.write('已添加学号为'+nsn+'的学生\n')
                window_main.update()
                window_add.destroy()

        # 姓名变量及标签、输入框
        new_name_ = tk.StringVar()
        tk.Label(window_add, text='姓名：').place(x=10, y=10)
        tk.Entry(window_add, textvariable=new_name_).place(x=150, y=10)
        # 性别变量
        new_gender = tk.IntVar()
        tk.Label(window_add, text='性别：').place(x=10, y=50)
        tk.Radiobutton(window_add,text='男',value='1').place(x=150, y=50)
        tk.Radiobutton(window_add,text='女',value='0').place(x=200, y=50)

        # 学号密码变量及标签、输入框
        new_school_number = tk.StringVar()
        tk.Label(window_add, text='学号：').place(x=10, y=90)
        tk.Entry(window_add, textvariable=new_school_number).place(x=150, y=90)
        # 确认注册按钮及位置
        bt_confirm_sign_up = tk.Button(window_add, text='确认添加',command=lambda:csv_add())
        bt_confirm_sign_up.place(x=150, y=130)

    def search():
        def search_progress():
            key = key_school_number.get()
            if key in str(csvmanager.school_number_array):
                i=0
                #将学号对应的id找出来，就可以查出其他信息了
                while str(csvmanager.school_number_array[i])!=key:
                    i+=1
                RESULT='姓名：'+csvmanager.name_array[i]+' 性别：'+csvmanager.gender_array[i]+' 学号：'+str(csvmanager.school_number_array[i])
                tk.messagebox.showinfo('查找完成',RESULT)
            elif key == '':
                tk.messagebox.showerror('错误', '未输入关键词')
            else:
                tk.messagebox.showinfo('查找完成', '无结果')
            window_search.destroy()

        window_search = tk.Toplevel(window_main)
        window_search.geometry('350x200')
        window_search.title('查找')
        window_search.iconphoto(False, tk.PhotoImage(file='.\icons\search.png'))
        # 用户名变量及标签、输入框
        key_school_number = tk.StringVar()
        tk.Label(window_search, text='学号：').place(x=10, y=10)
        tk.Entry(window_search, textvariable=key_school_number).place(x=150, y=10)
        # 确认注册按钮及位置
        bt_confirm_search = tk.Button(window_search, text='开始查找',command=lambda:search_progress())
        bt_confirm_search.place(x=150, y=100)


    def delete():
        def delete_progress():
            key_ = key_school_number.get()
            if key_ in str(csvmanager.school_number_array):
                i=0
                while str(csvmanager.school_number_array[i])!=key_:
                    i+=1
                #数据在第i+1行
                csvmanager.editor(i)
                tk.messagebox.showinfo('结果','删除成功')
                logger.login_activity()
                with open(file='final_project\log.txt',mode='a', encoding='utf-8') as f:
                    f.write('已删除学号为'+key_+'的学生\n')
            elif key_ == '':
                tk.messagebox.showerror('错误', '未输入关键词')
            else:
                tk.messagebox.showwarning('删除时遇到问题', '此学号不存在')
            window_delete.destroy()
            window_main.update()
        window_delete = tk.Toplevel(window_main)
        window_delete.geometry('350x200')
        window_delete.title('删除')
        window_delete.iconphoto(False, tk.PhotoImage(file='.\icons\delete.png'))

        key_school_number = tk.StringVar()
        tk.Label(window_delete, text='学号：').place(x=10, y=50)
        tk.Entry(window_delete, textvariable=key_school_number).place(x=150, y=50)

        bt_confirm_search = tk.Button(window_delete, text='确认删除',command=lambda:delete_progress())
        bt_confirm_search.place(x=150, y=100)

        tip = tk.Label(window_delete, text="请输入学号",font=('微软雅黑',16))
        tip.pack()

    def edit():
        #修改功能是个遗憾，一直没找到解决方案
        tkinter.messagebox.showinfo('提示','请先删除再添加已完成修改')

    #菜单
    _menu2=tk.Menu(window_main)

    submenu_open = tk.Menu(_menu2, tearoff=0) 
    submenu_open.add_command(label='添加',command=lambda:add())
    submenu_open.add_command(label='查找',command=lambda:search())
    submenu_open.add_command(label='修改',command=lambda:edit())
    submenu_open.add_command(label='删除',command=lambda:delete())
    _menu2.add_cascade(label='操作', menu=submenu_open)

    submenu_about_2 = tk.Menu(_menu2, tearoff=0)
    submenu_about_2.add_command(label='关于',command=lambda:tkinter.messagebox.showinfo("关于","作者：郭昭阳\n学号：202178030309\nMade with Tkinter"))
    _menu2.add_cascade(label='帮助', menu=submenu_about_2)

    window_main.config(menu=_menu2)
    #Treeview
    content_list=ttk.Treeview(window_main)
    content_list['columns']=('id','name','gender','school_number')

    content_list.column('#0', width=0,stretch=tk.NO)
    content_list.column("id",anchor='center', width=80)
    content_list.column("name",anchor='center', width=80)
    content_list.column("gender",anchor='center', width=80)
    content_list.column("school_number",anchor='center', width=80)

    content_list.heading('id', text='序号', anchor='center')
    content_list.heading('name', text='姓名', anchor='center')
    content_list.heading('gender', text='性别', anchor='center')
    content_list.heading('school_number', text='学号', anchor='center')

    for i in range(len(csvmanager.name_array)):
        ID=i+1
        NAME=csvmanager.name_array[i]
        GENDER=csvmanager.gender_array[i]
        SCHOOL_NUMBER=csvmanager.school_number_array[i]
        content_list.insert(parent='', index=i,values=(ID,NAME,GENDER,SCHOOL_NUMBER))

    #总算让滚动条有用了
    content_list.VScroll1 = tk.Scrollbar(window_main, orient='vertical')
    content_list.VScroll1.place(relx=0.950, rely=0.028, relwidth=0.024, relheight=0.958)
    content_list.config(yscrollcommand=content_list.VScroll1.set)
    content_list.VScroll1.config(command=content_list.yview)

    content_list.pack()

menu_title = tk.Label(window_login, text="欢迎回来！",font=('微软雅黑',16), width=60, height=4)
menu_title.pack()

# 标签 用户名密码
tk.Label(window_login, text='用户名:').place(x=60, y=100)
tk.Label(window_login, text='密码:').place(x=60, y=125)
# 用户名输入框
var_usr_name = tk.StringVar()
entry_usr_name = tk.Entry(window_login, textvariable=var_usr_name)
entry_usr_name.place(x=100, y=100)

# 密码输入框
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window_login, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=100, y=125)

# 登录函数
def usr_log_in():
    # 输入框获取用户名密码
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 从本地字典获取用户信息
    with open(file='Authenticator.json', encoding='utf-8', mode='r') as ff:
        for line in ff:
            usrs_info = json.loads(line)
    # 判断用户名和密码是否匹配
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='welcome',message='欢迎您：' + usr_name)
            logger.login_activity()
            with open(file='log.txt',mode='a', encoding='utf-8') as f:
                f.write('用户'+usr_name+'登录成功\n')
            window_login.destroy()
            _main_()       #打开主界面
        else:
            tk.messagebox.showerror(message='密码错误')
            logger.login_activity()
            with open(file='log.txt',mode='a', encoding='utf-8') as f:
                f.write('用户'+usr_name+'登录失败\n')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名或密码为空')
    # 不在数据库中弹出是否注册的框
    else:
        is_signup = tk.messagebox.askyesno('欢迎', '您还没有注册，是否现在注册')
        if is_signup:
            usr_sign_up()
# 注册函数
def usr_sign_up():
    # 确认注册时的相应函数
    def signtowcg():
        # 获取输入框内的内容
        nn = new_name.get()
        np = new_pwd.get()
        npf = new_pwd_confirm.get()

        # 本地加载已有用户信息,如果没有则已有用户信息为空
        try:
            with open(file='Authenticator.json', encoding='utf-8', mode='r') as ff:
                for line in ff:
                    exist_usr_info = json.loads(line)
        except FileNotFoundError:
            exist_usr_info = {}
            # 检查用户名存在、密码为空、密码前后不一致
        if nn in exist_usr_info:
            tk.messagebox.showerror('错误', '用户名已存在')
        elif np == '' or nn == '':
            tk.messagebox.showerror('错误', '用户名或密码为空')
        elif np != npf:
            tk.messagebox.showerror('错误', '密码前后不一致')
        # 注册信息没有问题则将用户名密码写入数据库
        else:
            exist_usr_info[nn] = np
            with open(file='Authenticator.json', encoding='utf-8', mode='w') as f:
                f.write(json.dumps(exist_usr_info)+'\n')
                tk.messagebox.showinfo('欢迎', '注册成功')
                logger.register_activity()
            with open(file='log.txt',mode='a', encoding='utf-8') as f:
                f.write('用户'+nn+'注册成功\n')
            # 注册成功关闭注册框
            window_sign_up.destroy()
    # 新建注册界面
    window_sign_up = tk.Toplevel(window_login)
    window_sign_up.geometry('350x200')
    window_sign_up.title('注册')
    window_sign_up.iconphoto(False, tk.PhotoImage(file='.\icons\_register.png'))
    # 用户名变量及标签、输入框
    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='用户名：').place(x=10, y=10)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=150, y=10)
    # 密码变量及标签、输入框
    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='请输入密码：').place(x=10, y=50)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=150, y=50)
    # 重复密码变量及标签、输入框
    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='请再次输入密码：').place(x=10, y=90)
    tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*').place(x=150, y=90)
    # 确认注册按钮及位置
    bt_confirm_sign_up = tk.Button(window_sign_up, text='确认注册',command=signtowcg)
    bt_confirm_sign_up.place(x=150, y=130)

# 登录 注册按钮
bt_login = tk.Button(window_login, text='登录', width=10,command=usr_log_in)
bt_login.place(x=90, y=160)
bt_logup = tk.Button(window_login, text='注册', width=10,command=usr_sign_up)
bt_logup.place(x=170, y=160)

#菜单
_menu = tk.Menu(window_login)

#最开始子窗口自动执行的解决方案
#tkinter要求由按钮（或者其它的插件）触发的控制器函数不能含有参数。若要给函数传递参数，需要在函数前添加lambda。

submenu_about = tk.Menu(_menu, tearoff=0)
submenu_about.add_command(label='关于',command=lambda:tkinter.messagebox.showinfo("关于","作者：郭昭阳\n学号：202178030309\nMade with Tkinter"))
_menu.add_cascade(label='帮助', menu=submenu_about)

window_login.config(menu=_menu)

window_login.mainloop()
