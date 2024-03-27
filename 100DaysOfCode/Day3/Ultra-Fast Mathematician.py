#link to problem: https://codeforces.com/problemset/problem/61/A
str1=input()
str2=input()
output=''
for i,j in zip(str1,str2):
    if i!=j:
        output+='1'
    else:
        output+='0'
print(output)