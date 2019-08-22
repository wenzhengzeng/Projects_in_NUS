n=input().split()
if n[1]=='0':
    for i in range(1,int(n[0])+1):
        print(i)
else:
    a=input().split()
    i=1
    b=[]
    while i<=int(n[0]):
        b.append(str(i))
        i+=1
    i=0
    sum=0
    while i<int(n[0]):
        if b[i] not in a:
            print(b[i])
            sum+=1
        i+=1
    if sum==0:
        print('0')
