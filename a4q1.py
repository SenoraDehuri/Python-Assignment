# -*- coding: utf-8 -*-
import random

def sum_avg(list):
    total=sum(list)
    avg=total/len(list)
    return total,avg
n=int(input("Enter:"))
list=[random.randint(1,100) for i in range (n)]
total,avg= sum_avg(list)
print(list)
print("Sum",total)
print("Average",avg)