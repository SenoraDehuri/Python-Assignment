def cumulative_sum(list):
    clist=[]
    total=0
    for i in list:
        total+=i
        clist.append(total)
    return clist

n=input("Enter numbers")
nlist=[int(num) for num in n.split()]
result=cumulative_sum(nlist)
print(result)