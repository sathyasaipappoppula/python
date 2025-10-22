s1=input("enter input: ")

#1st method 

# print(s1[::-1])


#2nd method 

# s2=""
# for i in s1:
#     s2=i+s2
# print(s2)


#3rd method 

# s2=""
# for i in range(0,len(s1)):
#     s2=s1[i]+s2 
# print(s2)


#4th method 

s2=""
for i in range(len(s1)-1,-1,-1):
    s2+=s1[i]
print(s2)