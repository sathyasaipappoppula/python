def even_num(n,x):
    if(x==n):
        print(x)
    else:
        print(x)
        return even_num(n,x+2)
n=int(input("enter a number: "))
if(n%2!=0):
    n-=1

x=0
even_num(n,x)