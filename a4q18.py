#Write a python program to create a new list that contains the square of every element ina given list using list comprehension
user=input("Enter numbers: ")
numbers=list(map(int, user.split()))
sq=[x**2 for x in numbers]
print("og:", numbers)
print("squared:",sq)
