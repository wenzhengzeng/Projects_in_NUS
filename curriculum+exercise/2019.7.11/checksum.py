n=input()
k=len(n)
n1=n[::-1]
def sum1(n):
    i=1
    sum2=0
    while i-1<k:
        if(i%2!=0):
            if 2*int(n[i-1])>=10:
                x=str(2*int(n[i-1]))
                sum2+=int(x[0])
                sum2+=int(x[1])
            else:
                sum2+=2*int(n[i-1])
        else:
            sum2+=int(n[i-1])
        i+=1
    return str((10-sum2%10)%10)
x=sum1(n1)
print(n+x)
                
    
