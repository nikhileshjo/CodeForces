#problem statment: https://codeforces.com/problemset/problem/732/A

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

shovelRate,change=map(int,input().split())
minShovel=compute_lcm(10,shovelRate)//shovelRate

for i in range(1,minShovel):
    shovelCst=shovelRate*i
    if (shovelCst)%10==change:
        minShovel=shovelCst//shovelRate

print(minShovel)