# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:32:49 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")

while True:
    s = t.textinput("","도형을 입력하시오: ")
    t.reset()
    if s == "사각형" :
        sw = t.textinput("", "가로: ")
        w=int(sw)
        sh = t.textinput("", "세로: ")
        h=int(sh)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
    elif s == "삼각형":
        sl = t.textinput("", "길이를 입력하시오: ")
        l=int(sl)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
    elif s == "원":
        sr = t.textinput("", "반지름을 입력하시오: ")
        r=int(sr)
        t.circle(r)
    else:
        t.write("삼각형, 사각형, 원 중 도형을 고르세요.")

t.exitonclick()
    
    