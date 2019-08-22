
def D01(pos,size):
    global f_list
    global func_list
    if func_list[0]=='0':
        if len(func_list)>1:
            func_list=func_list[1:]
        for i in range(size):
            for j in range(size):
                f_list[pos+i*N+j]=0
    elif func_list[0]=='1':
        if len(func_list)>1:
            func_list=func_list[1:]
        for i in range(size):
            for j in range(size):
                f_list[pos+i*N+j]=1
    elif func_list[0]=='D':
        if len(func_list)>1:
            func_list=func_list[1:]
        D01(pos,size//2)
        D01(pos+size//2,size//2)
        D01(pos+size//2*N,size//2)
        D01(pos+size//2*N+size//2,size//2)
N=int(input())
func_list=list(input())
f_list=[0]*(N*N+1)
D01(1,N)
for i in range(N):
   for j in range(N-1):
       print(f_list[i*N+j+1],end=' ')
   print(f_list[i*N+N])
    

