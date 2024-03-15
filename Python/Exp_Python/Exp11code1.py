#Exp11code1

# -*- coding: UTF-8 -*-
import turtle
import time
def drawGap():
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(30)
    drawGap()
    turtle.right(90)
def drawDigit(digit):
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(30)
def nowDate():
    t = time.gmtime()
    date = time.strftime("%Y-%m=%d+",t)
    return date
def main():
    turtle.pensize(10)
    turtle.pencolor("red")
    turtle.penup()
    turtle.fd(-250)
    turtle.pendown()
    str1 = nowDate()
    print(str1)
    for c in str1:
        if c=='-':
            turtle.write("年",font=("微软雅黑",20,"normal"))
            turtle.fd(40)
            turtle.pencolor("green")
        elif c=='=':
            turtle.write("月",font=("微软雅黑",20,"normal"))
            turtle.fd(40)
            turtle.pencolor("yellow")
        elif c=='+':
            turtle.write("日",font=("微软雅黑",20,"normal"))
            turtle.fd(40)
        else:
            num = eval(c)
            drawDigit(num)
    turtle.hideturtle()
    turtle.done()
main()
