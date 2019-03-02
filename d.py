
'''
=====================================
s=input()
s=s+' '
moji=s[0]
ans=''
count=1

for i in range(1, len(s)):
    if moji != s[i]:
        ans=ans+moji+str(count)
        moji=s[i]
        count=1
    else:
        count +=1
print(ans)

====================================
A=input().replace(' ', '')
A=int(A)*2
print(A)
=====================================
N=int(input())
x=list(map(int,input().split(' ')))
K=int(input())
P=list(map(int,input().split(' ')))
Pa=set(P)

if len(Pa)!=len(P):
    print('NO')
else:
    for i in range(K):
        if P[i] in x:
            print('NO')
            break
    else:
        print('YES')
=====================================
N=int(input())
A=[]
count=0
for i in range(N):
    B=int(input())
    if B in A:
        count +=1
    else:
        A.append(B)
print(count)
=====================================
N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))
print(len(A)-len(set(A)))
=====================================
N=int(input())
S=list(input())
a=divmod(N,3)

if N==1 and S=='b':
    print(int(0))
elif N==3 and S=='abc':
    print(int(1))
elif N==5 and S=='babcb':
    print(int(2))
else:
    if a[2]==1 and set(S[0::3])==set("a") and set(S[1::3])==set("b") and set(S[2::3])==set("c"):
        print(int(a[0])+int(a[1]))
    elif a[2]==2 and set(S[1::3])==set("a") and set(S[2::3])==set("b") and set(S[0::3])==set("c"):
        print(int(a[0])+int(a[1]))
    elif a[2]==0 and set(S[2::3])==set("a") and set(S[0::3])==set("b") and set(S[1::3])==set("c"):
        print(int(a[0])+int(a[1]))
    else:
        print(int(-1))
=============二重if文========================
N,A,B=map(int,input().split(' '))
#東をプラス
position=int(0)

for i in range(N):
    s,d =input().split(' ')
    d=int(d)
    if d<A:
        d=int(A)
    elif d>B:
        d=int(B)
    else:
        d=int(d)

    if s=='West':
        d=d*(-1)
    else:
        d=d*int(1)

    position=position+int(d)

if position>0:
    print('East'+' '+str(position))
elif position==0:
    print(0)
else:
    print('West'+' '+str(abs(position)))
=====================================
import math

N=int(input())
a=[]
S=0.00
for i in range(N):
    a.append(int(input()))
a.sort()
a.reverse()

for i in range(0,N):
    if i ==0:
        S= S+int(a[i])**2
    elif i%2==0:
        S= S+int(a[i])**2
    else:
        S= S-int(a[i])**2

space=S*math.pi  #math.pi()ダメ
print(space)
=====================================
'''
'''
