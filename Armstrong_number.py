num=int(input("enter a number: "))
str_num=str(num)
len_str_num=len(str_num)
armstrong=0
for i in str_num:
    int_i=int(i)
    armstrong+=(int_i**len_str_num)
if(num==armstrong):
    print("Armstrong")
else:
    print("Not a Armstrong")
