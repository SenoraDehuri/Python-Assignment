def coprime(x,y):
    while y!=0:
        x,y=y,x%y
    return x==1
x=int(input("Enter x"))
y=int(input("Enter y"))
if coprime(x,y):
    print("coprime")
else:
    print("Not coprime")