# =============================================================================
#  Input 10 integers from the keyboard into a list. The number to be searched is entered through the
#  keyboard by the user. Write a Python program to find if the number to be searched is present in the
#  list and if it is present, display the number of times it appears in the list.
# =============================================================================

l1=[]
print("Enter 10 integers")
for i in range(10):
    num=int(input("Enter integer"))
    l1.append(num)
search=int(input("Enter the number to be searched"))
count=l1.count(search)
if count>0:
    print(f"The number {search} is present in the list and appears {count} times.")
else:
    print(f"The number {search} is not present in the list")