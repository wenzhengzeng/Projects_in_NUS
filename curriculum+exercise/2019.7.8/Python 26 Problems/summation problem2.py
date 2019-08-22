n=int(input())
m=input()
m1=m.split()
l1=len(m1)
j=0
sum=0
x=1
while j<=l1-1:
    sum=0
    x=1
    k=int(m1[j])
    while x<=k:
        sum+=x**2
        x+=1
    print(sum)
    j+=1    
