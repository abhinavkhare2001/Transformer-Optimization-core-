import math
def func(H,wt,h,k,n,ht,lst):
    print(n,k)

    if(n==0):
        return [0,lst]
    if(k==0):
        return [0,lst]
    if(H==0):
        return [0,lst]
    else:
        v = func(H, wt, h, k, n - 1, ht, lst)
        lstcopy=lst[:]
        lstcopy.append([wt[n-1],h[n-1]-ht])
        u=func(H,wt,h,k-1,n-1,h[n-1],lstcopy)
        u[0]+=wt[n-1]*(h[n-1]-ht)
        if(v[0]>u[0]):
            return v
        else:
            return u

D=int(input("Enter the diameter of the core:  "))
K=int(input("Enter the maximum number of steps you want:   "))
wt=[D]
hmax=[0]
R=D/2
D=D-10
while(D!=0):
    wt.append(D)
    wr=D/2
    max1=math.sqrt(R*R-wr*wr)
    hmax.append(int(max1))
    D-=10

wt.reverse()

hmax.reverse()
print(wt,hmax)
t=[]

for i in range(len(wt)+1):
    lst=[]
    for j in range(K+1):
        lst2=[]
        for p in range(int(R)+1):
            lst2.append(-1)
        lst.append(lst2)
    t.append(lst)
area=func(R,wt,hmax,K,len(wt),0,[])
final=3.14*R*R
print(area[1])
print(area[0])
print(2*area[0]/final)


