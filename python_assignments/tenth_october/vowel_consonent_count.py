s1=input("enter a string: ")
vowels="aeiouAEIOU"
consonents="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTUWXYZ"
vowel_count=0 
consonent_count=0 
spaces_count=0 
for i in s1:
    if i in vowels:
        vowel_count+=1 
    elif i in consonents:
        consonent_count+=1 
    elif i==" ":
        spaces_count+=1 

print("vowels count: ",vowel_count)
print("consonents count: ",consonent_count)
print("spaces count: ",spaces_count)
