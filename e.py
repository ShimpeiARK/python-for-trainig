N=int(input())
A=list(map(str, input().split(' ')))
F=A[0::2]
L=A[1::2]

ans=[]
an=''
if N%2==0:
    L.reverse()
    ans=L+F
else:
    F.reverse()
    ans=F+L

for i in range(N):
    an=an+' '+str(ans[i])
print(an)

'''
============================
============================
============================
import math
N, M =map(int,input().split())
ans=0

if abs(N-M)==0:
    ans=math.factorial(N)*math.factorial(M)*2
elif abs(N-M)==1:
    ans=math.factorial(N)*math.factorial(M)
else:
    ans=0

ans=ans%(10**9+7)

print(ans)
============================
============================
============================
============================
============================
============================
============================
============================
============================
N, M =map(int,input().split())
F=[]
L=[]


for i in range(M):
    a, b=map(int,input().split())
    if a==1:
        F.append(b)

    if b==N:
        L.append(a)

FF=set(F)
LL=set(L)

for _ in FF:
    if _ in LL:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')
============================
N=input()
n=int(N)
sum=0
for i in range(len(N)):
    sum= sum +int(N[i])

if n%sum==0:
    print('Yes')
else:
    print('No')
============================
N=int(input())
dict ={}
sum=0
max=0
name=' '
for i in range(N):
    SP=list(map(str, input().split(' ')))
    dict[SP[0]]=int(SP[1])
    sum = sum +int(SP[1])
    if max<int(SP[1]):
        max=int(SP[1])
        name=SP[0]
ave=sum/2

if max<=ave:
    print('atcoder')
else:
    print(name)
============================
s=input()
k=int(input())
key=set([])
A=''
if k>len(s):
    print(0)
else:
    for i in range(len(s)-k+1):
        A=s[i:k+i]
        key.add(A)
    print(len(key))

============================
L, H = map(int,input().split())
N=int(input())

for i in range(N):
    A=int(input())
    if A<L:
        print(L-A)
    elif L<=A<=H:
        print(0)
    else:
        print(-1)


==========手芸王（わからん)==================
N=int(input())
S=list(input())
r=divmod(N,3)

X=set(S[0::3])
Y=set(S[1::3])
Z=set(S[2::3])

if N==1 and S==['b']:
    print(int(0))
elif N==3 and S==['a','b','c']:
    print(int(1))
elif N==5 and S==['b','a','b','c','b']:
    print(int(2))
else:
    if r[1]==1 and Z==set("a") and X==set("b") and Y==set("c"):
        print(int((N-1)/2))
    elif r[1]==2 and X==set("a") and Y==set("b") and Z==set("c"):
        print(int((N-1)/2))
    elif r[1]==0 and Y==set("a") and Z==set("b") and X==set("c"):
        print(int((N-1)/2))
    else:
        print(int(-1))

============================
S=input()
dict={'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0}

for i in S:
    if i =='A':
        dict['A'] =int(dict['A'])+1
    elif i =='B':
        dict['B'] =int(dict['B'])+1
    elif i =='C':
        dict['C'] =int(dict['C'])+1
    elif i =='D':
        dict['D'] =int(dict['D'])+1
    elif i =='E':
        dict['E'] =int(dict['E'])+1
    else:
        dict['F'] =int(dict['F'])+1

print(str(dict['A'])+" "+str(dict['B'])+" "+str(dict['C'])+" "+str(dict['D'])+" "+str(dict['E'])+" "+str(dict['F']))
============================
count=0

for i in range(12):
    a=input()
    if 'r' in a:
        count +=1

print(count)
============================
m, n=map(int, input().split(' '))
angle=[0.0, 0.0]

if m>=12:
    m=m-12

angle[0]=m*30+(0.5)*n
angle[1]=n*6

ANGLE=abs(angle[0]-angle[1])

print(abs(min(ANGLE, 360-ANGLE)))

============================
N,A,B=map(int, input().split())

print(min(N*A, B))
============================
# coding: utf-8
# 整数の入力
a, b, c, d = [int(i) for i in input()]
# 計算
if a+b+c+d == 7:
    s = "{}+{}+{}+{}=7"
elif a+b+c-d == 7:
    s = "{}+{}+{}-{}=7"
elif a+b-c+d == 7:
    s = "{}+{}-{}+{}=7"
elif a+b-c-d == 7:
    s = "{}+{}-{}-{}=7"
elif a-b+c+d == 7:
    s = "{}-{}+{}+{}=7"
elif a-b+c-d == 7:
    s = "{}-{}+{}-{}=7"
elif a-b-c+d == 7:
    s = "{}-{}-{}+{}=7"
elif a-b-c-d == 7:
    s = "{}-{}-{}-{}=7"
# 出力
print(s.format(a, b, c, d))
============================
N=int(input())
A=list(map(int,input().split(' ')))
B=list(map(int,input().split(' ')))
C=list(map(int,input().split(' ')))
cnt=0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if A[i]<B[j] and B[j]<C[k]:
                cnt +=1
print(cnt)
============================
N=int(input())
A=list(map(int, input().split(' ')))
A.sort()
A.reverse()
a=0
b=0
for i in range(N):
    if A.count(A[i])>=4:
        print(int(A[i])**2)
        break
    elif A.count(A[i])>=2 and a==0:
        a=int(A[i])
        continue
    elif A.count(A[i])>=2 and a!=A[i]:
        b=int(A[i])
        print(a*b)
        break
    else:
        continue
else:
    print(0)
============================
from collections import Counter
N=int(input())
A=list(map(int, input().split(' ')))

C=Counter(A)
print(C)

ans=0
for i in range(max(A)+1):
    print(i)
    ans=max(C[i]+C[i-1]+C[i+1],ans)

print(ans)
============================
n, X = map(int,input().split())
a=list(map(int,input().split(' ')))
ans=[]

X=str(format(X, 'b').zfill(n))
X=X[::-1]

for i in range(len(X)):
    if X[i]=='1':
        ans.append(a[i])

print(sum(ans))
'''
