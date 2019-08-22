n=int(input())
a=b=n
sum=0
k=1
while int(b/10):
    b=int(b/10)
    k+=1
    
while n/10:
    sum+=(n%10)**k
    n=int(n/10)
if sum==a:
    print('Yes')
else:
    print('No')

