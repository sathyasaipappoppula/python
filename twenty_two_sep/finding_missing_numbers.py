num=int(input("enter a number: "))
l1=list(map(int,str(num)))
mini=min(l1)
maxi=max(l1)
res=0
for i in range(mini,maxi+1):
    if i not in l1:
        res=(res*10)+i 
print(res)
