#Write a python program that prompts the user to enter ten numbers and displays the mean and standard deviation
import math
numbers=[]
for i in range(10):
    num=float(input("Enter numbers"))
    numbers.append(num)
mean=sum(numbers)/len(numbers)
variance=sum((x-mean)**2 for x in numbers)/len(numbers)
std_deviation=math.sqrt(variance)
print("Mean:",mean)
print("Standard deviation:",std_deviation)