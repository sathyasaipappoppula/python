l1=input("enter input: ").split()
l2=[]
s=0
for i in l1:
    if i not in l2:
        l2.append(i)
        c=l1.count(i)
        s+=c//2 
print(s)
