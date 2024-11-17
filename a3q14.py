def is_armstrong(n):
    num_str=str(n)
    num_digits=len(num_str)
    sumpow=sum(int(digit)**num_digits for digit in num_str)
     
    return sumpow==n
n=int(input("Enter a number:"))
if is_armstrong(n):
   print("armstrong")
else:
   print("not armstrong")    

