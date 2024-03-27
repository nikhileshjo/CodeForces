str1=input()
str2=input()
output=''
for i,j in zip(str1,str2):
    if i!=j:
        output+='1'
    else:
        output+='0'
print(output)