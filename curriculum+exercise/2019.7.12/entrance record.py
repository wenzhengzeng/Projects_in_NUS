n=int(input())
i=0
d={}
while i<n:
    a=input().split()
    if d.get(a[0],0)==0:
        d.update({a[0]:1})
    else:
        d[a[0]]+=1
    i+=1
l=len(d)
d=sorted(d.items(), key=lambda d:d[0])
for k,v in d:
    print(k,v)

            
    
