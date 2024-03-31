#Problem statement: https://codeforces.com/problemset/problem/785/A

polCnt=int(input())
faceCnt=0

for _ in range(polCnt):
    shape=input()
    if shape=="Tetrahedron":
        faceCnt+=4
    elif shape=="Cube":
        faceCnt+=6
    elif shape=="Octahedron":
        faceCnt+=8
    elif shape=="Dodecahedron":
        faceCnt+=12
    else:
        faceCnt+=20

print(faceCnt)