#Write a function that takes n as an input and creates a list of n lists such that i th list contains the first five multiples of i.
def multiple_list(n):
    list=[]
    for i in range(1,n+1):
        multiples=[i*j for i in range(1,6)]
        list.append(multiples)
    return list

n=int(input("Enter a positive number")) 
result=multple_list(n) 
for index, multiples in enumerate(result, start=1):
    