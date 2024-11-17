# -*- coding: utf-8 -*-
def rotate(x,y,z):
    return (y,z,x)
a='Doug'
b=22
c=1984
for i in range(3):
    a,b,c=rotate(a,b,c)
    print("a:", a ,"b:",b, "c:",c)
