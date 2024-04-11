# problem statement: https://codeforces.com/problemset/problem/32/B

Borze=input()
codeLen=len(Borze)

cnter=0
res=''
while cnter<codeLen:
    if Borze[cnter]=='.':
        res+='0'
        cnter+=1
    else:
        if Borze[cnter:cnter+2]=='-.':
            res+='1'
            cnter+=2
        else:
            res+='2'
            cnter+=2
print(res)