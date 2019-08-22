
n = int(input())
i=1
q=[]
while i<=n:
    q.append(input().split())
    i+=1
d={}
for e in q:
    if d.get(e[0],1)==1:
        d[e[0]]=int(e[1])
    elif d[e[0]]<int(e[1]):
        d[e[0]]=int(e[1])
dic=sorted(d.items(), key=lambda d:d[0]) 
for e,f in dic:
    print(e,f)
