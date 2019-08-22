n=list(map(int,input().split()))
def digui(n,m):
    if m==3:
        return n-2
    else:
        return (n-1)**(m-2)-digui(n,m-1)
print(digui(n[0],n[1]))
