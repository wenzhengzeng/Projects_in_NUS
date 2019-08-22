n=int(input())
a=[]
b=[]
for i in range(0,n):
    a.append(int(input()))
    b.append(input().split())
for i in range(0,n):
    if a[i]:
        k=len(b[i])
        j=1
        if b[i][0]=='1':
            x=1
        else:
            x=0
        while j<k:
            for h in range(0,int(b[i][j])):
                print(x,end=' ')
            j+=1
            x=x^1
        print('')
    else:
        x=int(b[i][0])
        print(x,end=' ')
        sum=0
        j=0
        while j<len(b[i]):
            
            if b[i][j]==str(x) :
                sum+=1
                j+=1
           
            else:
                x=x^1
                print(sum,end=' ')
                sum=1
                j+=1
        print(sum)
        
            
        
        
            
