i=input("Enter the number of elements followed by the elements")
ele=list(map(int, i.split()[1:]))
print("The list is sorted." if ele ==sorted(ele) else "The list is not sorted")