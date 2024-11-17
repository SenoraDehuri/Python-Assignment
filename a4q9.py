# Write two functions, one of which converts a binary number to decimal and the other one does the
 #reverse.
def binaryToDecimal(n):
     decimal=0
     i=0
     while n!=0:
         b=n%10
         decimal+=b*pow(2,i)
         n=n//10
         i+=1
     return decimal
def decimalToBinary(n):
    binary=0
    i=1
    while n!=0:
        b=n%2
        binary+=b*i
        n=n//2
        i*=10
    return binary

num = int(input("Enter a number: "))
# =============================================================================
# btd=decimalToBinary(num)
# =============================================================================
btd=binaryToDecimal(num)
# =============================================================================
# print("Binary "of",num,"is",btd)
# =============================================================================
print("Decimal of",num,"is",btd)
dtb=decimalToBinary(num)
print("Binary of",num, "is",dtb)
         
 