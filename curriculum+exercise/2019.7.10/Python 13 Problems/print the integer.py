def search(x,y):
    l=len(x)
    i=0
    while i<=l-1:
        if x[i]==y:
            return 1
        i+=1
    return 0
def multi(x,y):
    if x%y==0:
        return 1
    else:
        return 0
n1=input()
n=n1.split()
a=1
x=1
while a<=int(n[0]):
    b=search(str(a),str(3))
    c=search(str(a),str(5))
    d=multi(a,3)
    e=multi(a,5)
    if b+c+d+e==0 and int(n[1])>=x:
        print(a)
        x+=1
    if x>int(n[1]):
        break
    a+=1
