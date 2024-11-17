# Write a Python program that removes all occurrences of a specific element from a list.

def remove_occ(list,ele):
    return [i for i in list if i!=ele]

list=input("Enter the elements").split()
list=[int(element) for element in list]
ele=int(input("Enter the element to remove" ))
mlist=remove_occ(list,ele)
print(mlist)