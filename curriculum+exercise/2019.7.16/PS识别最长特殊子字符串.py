def judge(x):
    if x==x[::-1]:
        return 1
    else:
        return 0
x=''
n=input()
for i in range(1,len(n)+1):
    for j in range(0,len(n)-i+1):
        if judge(n[j:j+i]):
            x=n[j:j+i]
           
print(x)
