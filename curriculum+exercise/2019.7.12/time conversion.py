n=input().split()
m=int(input())
i=0
a=[]
while i<m:
    a.append(input())
    i+=1
'''def convert(x,n):
    l=len(x)
    i=0
    j=0
    a=[]
    while i<l:
        if x[i]!=':':
            a[j]+=x[i]
        else:
            j+=1
            a.append('')
        i+=1
    return int(n[2])*int(a[2])+int(n[1])*int(a[1])+int(n[1])*int(a[1])
i=0
while i<m:
    print(convert(a[i],n))'''
    
def convert(x,n):
    '''while i<l:
      if x[i]==':':
            x[i]=' '''
    x=x.replace(':',' ')
    x=x.split()
    return int(x[0])*int(n[1])*int(n[2])+int(x[1])*int(n[2])+int(x[2])
i=0
while i<m:
    print(convert(a[i],n))
    i+=1
