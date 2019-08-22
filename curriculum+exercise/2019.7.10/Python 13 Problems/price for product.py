a1=input()
a=a1.split()
def same(x,y):
    if(x>y):
        return same(int(0.5*x),y)
    elif(x<y):
        return same(x,int(0.5*y))
    else:
        return x
result=same(int(a[0]),int(a[1]))
print(result)
