import numpy as np
N=int(input())
s=np.array([0,0,0])
u=np.array([0,0,0])
X=True
for i in range(N):
    t=np.array(list(map(int,input().split())))
    u=t-s
    if u[1]+u[2]==u[0]:
        continue
    elif (abs(u[1]+u[2]-u[0]))%2==0 and u[0]>=u[1]+u[2]:
        continue
    else:
        X=False
        print('No')
if X==True:
    print('Yes')



'''
============================

a, b, c, d, e, f = map(int, input().split())

c=c-a
d=d-b
e=e-a
f=f-b

S=abs((c*f-d*e)/2)
print(S)
============================
N,K=map(int,input().split())
R=list(map(int,input().split()))
R.sort()
A=list(R[N-K:N])

rate=0
for i in range(K):
    rate= (rate+A[i])/2

print(rate)
============================
s=[1,2,3,4,5,6]
N=int(input())
suji=''
for i in range(N):
    l=i%5+1
    r=i%5+2
    s[l], s[r]=s[r], s[l]

for i in range(6):
    suji= suji +str(s[i])

print(suji)
==========全探索==================
# coding :utf-8
N=int(input())

F=[]
P=[]

table = [2**i for i in range(10)]

for i in range(N):
    lis = list(map(int, input().split()))
    F.append(lis)
#print(F)
for i in range(N):
    lis = list(map(int, input().split()))
    P.append(lis)
#print(P)

maxx=-1000000000001


for i in range(1,1024):
    total=0
    for j in range(N):
        n=0
        for k in range(10):
            n +=(1 if i&table[k] !=0 else 0)*F[j][k]
        total += P[j][n]
    if total >maxx:
        maxx= total
print(maxx)

=========？？？===================

N,Q=map(int, input().split())
S=[]
moji=''
a=int(0)
b=int(1)
for i in range(N):
    S.append(a)

for j in range(Q):
    l, r =map(int,input().split())
    if l==r:
        S[l-1]=S[l-1]+1
        continue
    for k in range(l-1,r):
        S[k]=S[k]+1
print(S)

for i in range(N):
    if S[i]%2==0:
        moji=moji+str(0)
    else:
        moji=moji+str(1)

print(moji)
============================
R=input()
count=0

for _ in R:
    if _ =='1':
        count=count+1
print(count)
============================
N=int(input())
A=list(map(int,input().split()))
count=[0 for i in range(N)]

for i in range(N):
    while A[i]%2==0:
        A[i]=A[i]/2
        count[i]=int(count[i])+1

print(min(count))
============================
from collections import Counter

N,K=map(int,input().split())
A=list(map(int,input().split()))
count=0
S=set(A)
c=Counter(A)
L=c.most_common(len(S))

x=len(S)-1
for _ in range(len(S)-K):
    count=count+int(L[x][1])
    x=x-1

print(count)
============================
R=input()
count=0

for _ in R:
    if _ =='1':
        count=count+1
print(count)

============================
import math
a,b=map(str,input().split())
c=a+b
c=int(c)
d=math.sqrt(c)
if d==int(d):
    print('Yes')
else:
    print('No')

============================
============================
'''
