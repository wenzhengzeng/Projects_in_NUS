def judge(a):
    i=0
    while i<len(a):
        if (a[i] not in['+','-','*']) and (a[i+1] not in ['+','-','*']):           
            if a[i-1]=='*':
                return int(a[i])*int(a[i+1]),i
            if a[i-1]=='+':
                return int(a[i])+int(a[i+1]),i
            if a[i-1]=='-':
                return int(a[i])-int(a[i+1]),i
        i+=1
def change(x):
    k,i=judge(x)
    del x[i-1]
    del x[i-1]
    x[i-1]=str(k)
    return x
p=input().split()
while len(p)>=3:
    p=change(p)
print(int(p[0]))


    
