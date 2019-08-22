'''n=int(input())
a=[]
i=n
while i:
    a.append(input())
    i-=1
def judge(x):
    x1=x.split()
    if len(x1)==3:
        print(x)
        if x[1]=='male':
            return 0,int(x[2]),0
        else:
            return 0,0,int(x[2])
    else:
        return 1
j=0
sum1=0
sum2=0
while j<=n-1:
    q=judge(a[j])
    if(q[0]=='0'):
        if(q[1]=='0'and int()):
            sum2+=int(q[2])
        else:
            sum1+=int(q[1])
    j+=1
j=0

while j<=n-1:
    k=judge(a[j])
    if k[0]==1:
        if(a[j][1])=='male':'''
n=int(input())
a=[]
i=0
while i<n:
    a.append(input().split())
    i+=1
mf=0
mm=0
summ=sumf=0
i=0
while i<n:
    k=len(a[i])
    if k==3 :
        if int(a[i][2])<=150 and int(a[i][2])>=20:
            if a[i][1]=='male':
               summ+=int(a[i][2])
               mm+=1
            else:
                sumf+=int(a[i][2])
                mf+=1
        else:
            del a[i]
            i-=1     '''这两行很重要，因为删掉了元素，i受影响'''
            n=n-1
    i+=1
avm=avf=0
if mm:
    avm=summ/mm
if mf:
    avf=sumf/mf
print(len(a))
def judge(x):
    i=0
    while i<len(x):
        if len(x[i])==3:
            print(x[i][0],x[i][1],x[i][2])
        elif x[i][1]=='male':
            if avm:
                print(x[i][0],x[i][1],avm)
            else:
                print(x[i][0],x[i][1],70)
        else:
            if avf:
                print(x[i][0],x[i][1],avf)
            else:
                print(x[i][0],x[i][1],50)
        i+=1
judge(a)
       
    

    
        
    
    
