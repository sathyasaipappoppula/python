num=int(input("enter the range upto you want to print armstrong numbers: "))
for i in range(1,num+1):
    str_i=str(i)
    len_str_i=len(str_i)
    armstrong=0
    for j in str_i:
        armstrong+=(int(j)**len_str_i)
    if(i==armstrong):
        print(i,end=" ")
