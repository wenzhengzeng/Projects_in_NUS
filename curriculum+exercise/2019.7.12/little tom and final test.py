n=list(map(int,input().split()))
a={}
c={}
b=[]
d={}
for i in range(0,n[1]):
    b.append(input().split())
    a.update({b[i][0]:b[i][1]})
for i in range(0,n[0]):
    d.update({str(i+1):-1})
for i in range(0,n[0]):
    k=str(i+1)
    c=d.copy()   '''一定要copy,否则认为c,d是同一个字典'''
    while a.get(k,0)!=0:
        if c[k]==-1:
            c[k]=0
            '''print(i+1,'k is',k)'''
            k=a[k]
            '''print(i+1,'k is',k)
            print('11111',c)
            print('1111d',d)'''
        else:
            print('Never Stop')
            break
    if a.get(k,0)==0:
        print(k)
