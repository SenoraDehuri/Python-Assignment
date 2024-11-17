def product(n):
     nstr=str(abs(n))
     prod=1
     for digit in nstr:
        prod*=int(digit)
     return prod
 
n=int(input("Enter a number"))
number=int(n)
result=product(number)
print(result)