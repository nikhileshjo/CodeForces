oddPhrase="I hate"
evenPharse="I love"
joinPhrase="that"
endPhrase="it"
output="I hate"
for i in range(2,int(input())+1):
    if i%2==0:
        output+=" that "+evenPharse
    else:
        output+=" that "+oddPhrase

print(output,end=" it\n")