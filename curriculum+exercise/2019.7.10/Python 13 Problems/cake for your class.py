n,k=list(map(int,input().split()))
bg=list(map(int,input().split()))
cake=list(map(int,input().split()))

for i in range(k//2+k%2):
    j=0
    while j<2*n:
        if bg[j]>=cake[2*i]:
            print(j+1)
            break
        else:
            j+=2
    if not(k%2!=0 and i==k//2):
        j=2*n-1
        while j>0:
            h=cake[2*i+1]
            if bg[j]>=h:#cake[2*i+1]:
                print(j+1)
                break
            else:
                j-=2
