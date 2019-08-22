n=input()
a=input().split()
a=list(map(int,a))
sum=0
sum1=sum2=0
i=0
while i<len(a):
    sum+=a[i]
    i+=1
i=0
while i<len(a):
    sum1+=a[i]
    if(abs(sum-2*sum1)<abs(sum-2*sum2)):
        sum2=sum1
    i+=1
print(abs(sum-2*sum2))
