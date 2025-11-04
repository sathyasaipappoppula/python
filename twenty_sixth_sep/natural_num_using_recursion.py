def natural_num(n,x):
    if(x==n):
        print(n)
    else:
        print(x)
        return natural_num(n,x+1)

n=int(input("enter a number: "))
x=1
natural_num(n,x)
