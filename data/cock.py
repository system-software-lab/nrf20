import random
import time

def bubr(a,n):
    for p in range(1,n):
        for s in range(n,p,-1):
            if a[s]<a[s-1]:
                a[s],a[s-1]=a[s-1],a[s]

def bub(a,n):
    for e in range(n,1,-1):
        for r in range(1,e):
            if a[r]>a[r+1]:
                a[r],a[r+1]=a[r+1],a[r]

def check(a,n):
    for i in range(1,n):
        if a[i]>a[i+1]:
            return 0
    return 1

def cock(a,n):
    y=n
    for t in range(1,y):
        for u in range(t,y):
            if a[u]>a[u+1]:
                a[u],a[u+1]=a[u+1],a[u]
        for u in range(y-1,t,-1):
            if a[u]<a[u-1]:
                a[u],a[u-1]=a[u-1],a[u]
        y=y-1

def exch(a,n):
    for t in range(1,n):
        for y in range(t+1,n+1):
            if a[t]>a[y]:
                a[t],a[y]=a[y],a[t]

c=[-1,7,4,8,2,9,1,3,10,5,6]

a=[]
a.append(-1)
n=5000
for i in range(1,n+1):
    b=random.randint(1,10000)
    a.append(b)


#exch(c,10)
#bubr(a,n)
#exch(a,n)
st_time=time.time()
cock(a,n)
print(" {}ms ".format((time.time()-st_time)*1000))
print(check(a,n))

