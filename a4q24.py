#Given a list of tuples, remove all the tuples with length K, where K is user-defined.
def remove(list,k):
    return [t for t in list if len(t)!=k]
list=[(1, 2, 3), (4, 5), (6, 7, 8), (9, 10), (11, 12, 13)]
k=int(input("Enter the length of tupes to remove"))
result=remove(list,k)
print(result)