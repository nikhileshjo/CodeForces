#problem statement: https://codeforces.com/problemset/problem/1520/B

def ordCnt(n):
    num=int(n)
    result=0
    for j in range(1,len(n)+1):
        for i in range(1,10):
            if int(str(i)*j)<=num:
                result+=1
            else:
                return result
    return result


for i in range(int(input())):
    n=input()
    res=ordCnt(n)
    print(res)