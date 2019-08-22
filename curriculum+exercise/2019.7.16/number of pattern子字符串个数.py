n=input().split()
l=len(n[1])
sum=0
i=0
while i<len(n[0])-l+1:
    x=n[0]
    if x[i:i+l]==n[1]:
        sum+=1
    i+=1
print(sum)
