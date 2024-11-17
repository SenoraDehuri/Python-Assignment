#Write a function that takes a positive integer and returns the number of digits.
def count(n):
    count=0;
    while n!=0:
        count+=1
        n=n//10
    return count
n=int(input("Enter a number"))
print(count(n))
        

