def largest(n):
    l1=l2=l3=0
    while n!=0:
        b=n%10;
        if b>l1:
            l3=l2
            l2=l1
            l1=b
        elif b>l2:
            l3=l2
            l2=b
        elif b>l3:
            l3=b
        n=n//10
    print("largest:",l1)
    print("second largest:",l2)
    print("third largest:",l3)
    
n=int(input("Enter a number"))
largest(n)
