n=input()
a=list(map(int,input().split()))
m=int(input())
b=[]
for i in range(0,m):
    b.append(int(input()))
    
a.sort()
for i in range(0,m):
    for j in range(1,len(a)):
        if a[0]>b[i]:
            print('0')
            break
        elif a[j]-a[j-1]>b[i]:
            print(a[j-1])
            break
        elif j==len(a)-1:
            print(a[j])
    
    
            

    
