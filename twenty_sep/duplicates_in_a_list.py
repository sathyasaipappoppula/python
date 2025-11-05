def is_duplicate(num):
    str_num=str(num)
    for i in str_num:
        if(str_num.count(i)>1):
            return False 
    return True
l1=list(map(int,input("enter input: ").split()))
l2=[]
for i in l1:
    l2.append(is_duplicate(i))
print(l2)