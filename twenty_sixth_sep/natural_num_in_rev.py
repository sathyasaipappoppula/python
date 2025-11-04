def natural_num(n):
    if(n==1):
        print(n)
    else:
        print(n)
        return natural_num(n-1)

n=int(input("enter a number: "))
natural_num(n)
