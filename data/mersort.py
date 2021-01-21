import random
import time

def bubr(a,n):
    for p in range(1,n):
        for s in range(n,p,-1):
            if a[s]>a[s-1]:
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

def merge(a,aux,l,m,r):
    for k in range(l,r):
        aux[k]=a[k]
    i=l
    j=m

    for k in range(l,r):
        if i>=m:
            a[k]=aux[j]
            j+=1
        elif j>=r:
            a[k]=aux[i]
            i+=1
        elif aux[j]<aux[i]:
            a[k]=aux[j]
            j+=1
        else:
            a[k]=aux[i]
            i+=1
def mersort(a,aux,lo,hi):
    if hi<=lo+1:
        return
    m=int(lo+(hi-lo)/2)
    mersort(a,aux,lo,m)
    mersort(a,aux,m,hi)
    merge(a,aux,lo,m,hi)

def run(a,n):
    b=[]
    b.append([])
    c=0
    for i in range(1,n+1):
        b[c].append(a[i])
        if i==n:
            break
        if a[i]>a[i+1]:
            b.append([])
            c+=1
    #print(b)
    return b,c

def run2(aa,n):
    bb=[]
    bb.append([])
    c=0
    a=1
    b=2

    while b<n+1:
        if aa[b]<aa[b-1]:
            #print('a: %d b: %d \n' % (a,b))
            bb[c]=aa[a:b]
            bb.append([])
            c+=1
            if b==n:
                bb[c].append(aa[n])
                c+=1
            a=b
            b+=1
        elif b==n:
            #bb[c]=aa[n-1:n+1]
            bb[c]=aa[a:n+1]
            c+=1
            break
        else:
            b+=1
    #print(bb)
    #print(c)
    return bb,c

def runmer(aa,cnt):
    num2=cnt*2-1
    num=0
    while cnt<num2:
        aa.append([])
        cnt+=1
        #while len(aa[num])<n:
        while len(aa[num])!=0 or len(aa[num+1])!=0:
            #print('len(aa[num]): %d, and len(aa[num+1]): %d \n' %(len(aa[num]),len(aa[num+1])))
            if len(aa[num])==0:
                aa[cnt-1].append(aa[num+1][0])
                aa[num+1].pop(0)
                #continue
            elif len(aa[num+1])==0:
                aa[cnt-1].append(aa[num][0])
                aa[num].pop(0)
                #continue
            elif aa[num][0]<aa[num+1][0]:
               # print(aa[num][0])
               # print(aa[num+1][0])
                aa[cnt-1].append(aa[num][0])
                aa[num].pop(0)
            else:
                aa[cnt-1].append(aa[num+1][0])
                aa[num+1].pop(0)
            #print('a:len(aa[num]): %d, and len(aa[num+1]): %d \n' %(len(aa[num]),len(aa[num+1])))
            #print('cnt: %d' % cnt)
        num+=2
        #print(aa)
    return aa[cnt-1]

c=[-1,7,4,8,2,9,1,3,10,5,6]
cc=[-1,9,8,3,5,8,6,8,9,2,1]
cc2=[-1, 9, 5, 9, 4, 7, 2, 5, 8, 9, 7]
cc3=[-1, 7, 5, 4, 5, 7, 3, 2, 8, 8, 9]
d=[0,0,0,0,0,0,0,0,0,0,0,0]

a=[]
a.append(-1)
n=1000
for i in range(1,n+1):
    b=random.randint(1,10)
    a.append(b)

#print(a)
#exch(c,10)
#bubr(a,n)
#print(a)
bub(a,n)
'''
st_time=time.time()
bb,cnt=run(a,n)
cnt+=1

#mersort(c,d,1,11)
#cock(a,n)
print("run: {}ms \n".format((time.time()-st_time)*1000))

'''
st_time=time.time()
bb,cnt=run2(a,n)


#print(bb)
#print(cnt)

result=runmer(bb,cnt)
result.insert(0,-1)
print("run2: {}ms \n".format((time.time()-st_time)*1000))

print(check(result,n))
#print(result)


#print(c)

