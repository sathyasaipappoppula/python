# num=int(input("enter a number: "))
# str_num=str(num)
# len_str_num=len(str_num)
# armstrong=0
# for i in str_num:
#     int_i=int(i)
#     armstrong+=(int_i**len_str_num)
# if(num==armstrong):
#     print("Armstrong")
# else:
#     print("Not a Armstrong")



# 2nd method

num=int(input("enter a number: "))
str_num=str(num)
len_str_num=len(str_num)
num2=num 
sum=0
while(num2>0):
    digit=num2%10 
    sum+=digit**len_str_num 
    num2//=10 
if(sum==num):
    print("Armstrong")
else:
    print("Not a Armstrong")