#write a python fucntion that sorts a list of tuples based on the second element of each tuple
def sort(tlist):
    slist=sorted(tlist, key=lambda x:x[1])
    return slist

tlist=[(1, 3), (4, 1), (2, 2), (5, 0)]
sortedList=sort(tlist)
print(tlist)
print(sortedList)