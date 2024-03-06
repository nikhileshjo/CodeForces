input_len = int(input())
stones = list(input())
for i in range(input_len):
    flag = 1
    try:
        while flag:
            if stones[i]==stones[i+1]:
                stones.pop(i+1)
            else:
                flag=0
    except:
        break
print(input_len-len(stones))