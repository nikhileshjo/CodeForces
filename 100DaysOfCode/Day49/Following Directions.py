# problem statement: https://codeforces.com/problemset/problem/1791/B

def reach_obj(charArr):
    pos=[0,0]
    for i in charArr:
        if i=='U':
            pos[1]+=1
        elif i=='D':
            pos[1]-=1
        elif i=='L':
            pos[0]-=1
        else:
            pos[0]+=1
        if pos==[1,1]:
            return "YES"
    return "NO"

for _ in range(int(input())):
    arrLen=input()
    arr=input()
    print(reach_obj(arr))
