


'''
==============キー=======================
from collections import Counter

n=int(input())
ans=''
counter={}
for i in range(1,n+1):
    if i==1:
        s=input()
        counter=Counter()
        counter=Counter(s)
    else:
        s=input()
        counter=Counter(s)&counter

for (word, cnt)in counter.items():
    ans=ans+word*cnt

if len(ans)==0:
    ans2=""
else:
    ans2=str(ans)

print(ans2)
=====================================
A, B, C, D=map(int,input().split(' '))

if A+B>C+D:
    print('Left')
elif A+B==C+D:
    print('Balanced')
else:
    print('Right')
=====================================
N, A, B=map(int,input().split(' '))
sum=0
ans=0
for i in range(1, N+1):
    s=list(str(i))
    for j in range(len(s)):
        sum =int(sum)+int(s[j])
    if A<=int(sum)<=B:
        ans = int(ans)+i
    sum=0
    s=0

print(ans)
=====================================
N, A, B =map(int,input().split(' '))

m=B-A-1

if m%2==1:
    print('Alice')
elif m%2==0:
    print('Borys')
else:
    print('Draw')
==============グランドテスト　ぼつ=======================
K=int(input())
A=list(map(int,input().split(' ')))
ans1=2
ans2=3
j=0
k=0
ans=0
A.reverse()


for i in range(len(A)-1):
    if int(A[i])<int(A[i+1]) and int(A[i])*2>int(A[i+1]):
        ans1=max(ans1,int(A[i+1]))
        ans2=max(ans2,int(A[i+1]))
    elif int(A[i])<int(A[i+1]) and int(A[i])*2<int(A[i+1]):
        ans=-1
        break
    elif int(A[i])>int(A[i+1]):
        while ans1<=int(A[i+1])*2-1:
            j=j+1
            ans1=int(A[i+1])*j
        while ans2<ans1:
            k=k+1
            ans2=ans2+int(A[i+1]-1)*k
    elif A[i]==A[i+1]:
        continue
    else:
        ans2=-1

if ans==-1:
    print('-1')
elif ans1==ans2:
    ans2=ans1+1
    print(ans1, ans2)
else:
    print(ans1, ans2)
=====================================
=====================================


X, Y=map(int,input().split(' '))
cnt=0

while X<=Y:
    cnt +=1
    X= X*2

print(cnt)
=====================================
N=int(input())
ng=[]
for i in range(3):
    ng.append(input())

ng.sort()
a=ng[0]
b=ng[1]
c=ng[2]
count=0
while N>=0:
    if N-3>=0 and N-3 !=a and N-3 !=b and N-3 !=c:
        N =N-3
        count =count+1
        continue
    elif N-2>=0 and N-2 !=a and N-2 !=b and N-2 !=c:
        N=N-2
        count =count+1
        continue
    elif N-1>=0 and N-1 !=a and N-1 !=b and N-1 !=c:
        N=N-1
        count=count +1
        continue
    else:
        print('?')

if count>100:
    print('NO')
else:
    print('YES')

=============ワーシャルフロイド方========================
H, W=map(int,input().split())
c=[list(map(int,input().split())) for _ in range(10)]
a=[list(map(int,input().split())) for _ in range(H)]
ans=0

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j]=min(c[i][j],c[i][k]+c[k][j])

for i in range(H):
    for j in range(W):
        if a[i][j]>=0:
            ans += c[a[i][j]][1]

print(ans)
=====================================
N=input()
dst = N.replace('2017', '2018')
print(dst)
=====================================
N=int(input())
d=[]
for i in range(N):
    d.append(input())

a=set(d)

print(len(a))
=====================================
N, Y=map(int,input().split())
flag=False

for i in range(0,N+1):
    for j in range(0, N+1):
        if Y==10000*(N-i-j)+5000*i+1000*j and i+j=<N:
            flag=True
            print(N-i-j, i, j)
            break
    if flag:
        break
else:
    print('-1 -1 -1')

=====================================
import bisect
N, H=map(int,input().split(' '))
a=[]
b=[]
D=0
cnt=0
c=0
for i in range(N):
    aa,bb=map(int,input().split(' '))
    a.append(aa)
    b.append(bb)
am=max(a)
b.sort()
bisect.insort_left(b, am)
c=bisect.bisect_left(b, am)
d=len(b)-c
b.reverse()

for i in range(d):
    D=int(D)+int(b[i])
    cnt=cnt+1
    if D>=H:
        print(cnt)
        break
if D<H:
    while D>=H:
        D=D+am
        cnt=cnt+1
        if D>=H:
            print(cnt)
            break


=============ボツ========================
import math
S=list(str(input()))
a=['1','1','1']
b=0
one=0
zero=0
c=0
ansone=len(S)
anszero=len(S)
if S==a:
    print(int(3))
elif len(S)==3:
    print(2)
else:
    b=1

for i in range(0, len(S)-1):
    if S[i]=='1' and S[i+1]=='1':
        one +=1
        continue
    elif S[i]=='0' and S[i+1]=='0':
        zero +=1
        continue
    elif S[i]=='1' and S[i+1]=='0':
        ansone=min(ansone, one)
        one=0
        continue
    elif S[i]=='0' and S[i+1]=='1':
        anszero=min(anszero, zero)
        zero=0
        continue
    else:
        c=1
ansone=min(ansone, one)
anszero=min(anszero, zero)
if anszero==0 and b==1:
    print(ansone+1)
elif anszero !=0 and b==1:
    print(anszero+1)
else:
    b=1
=====================================
from collections import Counter

n=int(input())
ans=''
counter={}
for i in range(1,n+1):
    if i==1:
        s=input()
        counter=Counter()
        counter=Counter(s)
    else:
        s=input()
        counter=Counter(s)&counter

for c in [chr(i) for i in range(ord('a'), ord('z')+1)]:
    ans=ans+c*counter[c]
print(ans)
=====================================
N, T=map(int,input().split(' '))
t=list(map(int,input().split(' ')))
s=0
m=0

for i in range(N-1):
    m=t[i+1]-t[i]
    s=s+min(m, T)
print(s+T)
=====================================
N=int(input())
S=[]
table=[2**i for i in range(7)]

for i in range(N):
    s=int(input())
    S.append(s)
S.sort()
a=sum(S)

if a%10 !=0:
    print(a)
else:
    for i in range(N):
        if S[i]%10 !=0:
            a=a-int(S[i])
            print(a)
            break
    else:
        print(0)
'''
