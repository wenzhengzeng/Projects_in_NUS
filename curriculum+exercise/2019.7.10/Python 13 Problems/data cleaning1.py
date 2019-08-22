n=int(input())
a=[]
i=n
while i:
    a.append(input())
    i-=1
def judge(x):
    x1=x.split()
    if len(x1)==2:
        print(x)
        return 0
    else:
        return 1
j=n
sum=0
while j:
    sum+=judge(a[n-j])
    j-=1
print(sum)

    
