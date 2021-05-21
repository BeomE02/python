# -*- coding: utf-8 -*-
"""
Created on Fri May 21 13:47:50 2021

@author: Mac_1
"""

import turtle as t

t.shape('turtle')
t.clear()

s = t.textinput("", "이름을 입력하시오")
t.write("안녕하세요 반갑습니다."+s+"님 반갑습니다.")

for i in range(4):
    t.forward(100)
    t.left(90)