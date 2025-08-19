
def prime_or_not(num):
    if(num<=1):
        return "not a prime"
    else:
        for i in range(2,num):
            if(num%i==0):
                return  "not a prime"
                break 
        else:
            return "prime"
num=int(input("enter a number: "))
res=prime_or_not(num) 
print(res)
        