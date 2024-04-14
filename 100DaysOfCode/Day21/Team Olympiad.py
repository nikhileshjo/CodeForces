#problem statement: https://codeforces.com/problemset/problem/490/A

def nth_occurrence(lst, value, n):
    count = 0
    for i, v in enumerate(lst):
        if v == value:
            count += 1
            if count == n:
                return i
    return None


studCnt=input()
skills=list(input().split())
resCnt=skills.count(str('1'))
for i in range(1,4):
    tmp=skills.count(str(i))
    if resCnt>tmp:
        resCnt=tmp
print(resCnt)
for j in range(resCnt):
    st1=nth_occurrence(skills,'1',j+1)+1
    st2=nth_occurrence(skills,'2',j+1)+1
    st3=nth_occurrence(skills,'3',j+1)+1
    print(st1,st2,st3)
