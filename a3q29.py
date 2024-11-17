def is_perfect(n):
    if n<=0:
        return False
    sum=0;
    for i in range(1,n//2+1):
        if n%i==0:
            sum+=i
    return sum==n
n=int(input("Enter a number"))
if is_perfect(n):
    print("Perfect")
else:print("Not perfect")