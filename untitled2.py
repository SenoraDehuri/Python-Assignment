# -*- coding: utf-8 -*-
def display_menu():
    print("\Menu")
    print("1. Create a list of N integers")
    print("2. Display the list elements")
    print("3. Insert an element at a specific position")
    print("4. Delete an element at a given position")
    print("5. Exit")
    
def create_list():
    n=int(input("Enter the no. of integers you want to input"))
    list=[]
    for i in range(n):
        num=int(input("Enter integer:"))
        list.append(num)
    return list
def display_list(list):
    if list:
        print("List elements:", list)
    else:
        print("The list is empty.")
def insert_element(list):
    element=int(input("Enter the element to insert"))
    position=int(input("Enter the position tyo enter the element"))
    if 0<=position<=len(list):
        list.insert(position,element)
        print("Element ",element,"inserted at position ", position)
    else:
        print("invalid position")
def delete_element(list):
    position=int(input("Enter the position of the element to be deleted"))
    if 0<=position<=len(list):
        removed_element=list.pop(position)
        print("Element ",removed_element,"deleted from position ", position)
    else:
        print("invalid position")  

list=[]
while True:
    display_menu()
    choice =input("Enter your choice(1-5):")
    
    if choice=='1':
        list=create_list()
    elif choice=='2':
        display_list(list)
    elif choice=='3':
        insert_element(list)
    elif choice=='4':
        delete_element(list)
    elif choice=='5':
        print("Exiting the program")
        break;
    else:
        print("Invalid choice.")