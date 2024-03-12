orgWord=input()
transWord=input()

orgWordRev = orgWord[::-1]

if orgWordRev==transWord:
    print("YES")
else:
    print("NO")