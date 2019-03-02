
'''
============ループ=========================
S=list(input())
T=list(input())
X=list('atcorde@')

for i in range(len(S)):
    if S[i]==T[i]:
        continue
    elif S[i]=='@' and T[i] in X:
        continue
    elif S[i] in X and T[i]=='@':
        continue
    else:
        print('You will lose')
        break
else:
    print('You can win')
===============入力重要！！======================
N=int(input())
a=list(map(int,input().split(' ')))
count=0

for i in range(N):
    if a[i]%6==0:
        count +=3
        continue
    elif a[i]%5==0:
        count +=2
        continue
    elif a[i]%4==0:
        count +=1
        continue
    elif a[i]%2==0:
        count +=1
        continue
    else:
        continue
print(count)
===============ゼロフィル=====================
N=int(input())
a=[N,0,0]
a[1]=divmod(N,3600)
a[2]=divmod(a[1][1],60)
print(str(a[1][0]).zfill(2)+":"+str(a[2][0]).zfill(2)+":"+str(a[2][1]).zfill(2))

==============入力数のカウント=======================
N=int(input())
a=[]
b=[]
for i in range(N):
    a.append(input())

for j in range(N):
    c=a.count(a[j])
    b.append(c)
print(a[max(b)])
============トリナボッチ=========================
a=[0, 0, 1]
N=int(input())
if N<=3:
    print(a[N-1])
else:
    for i in range(N-3):
        a.append(sum(a)%10007)
        a.pop(0)

    print(a[-1])
============バグ=========================
import math

N=int(input())
a=list(map(int,input().split(' ')))
b=0

sum=0
ave=0

for i in range(N):
    if a[i]==0:
        b=b+1
        continue
    else:
        sum=sum+a[i]

ave=math.ceil(sum/(N-b))
print(ave)
============鍵=========================
a=int(input())
b=int(input())
c=abs(a-b)

if c<5:
    print(c)
else:
    if a>b:
        print(10+b-a)
    else:
        print(10+a-b)
============A+B=========================
X=list(map(int,input().split(' ')))

if X[0]+X[1]!=X[2] and X[0]-X[1]!=X[2]:
    print('!')
elif X[0]+X[1]==X[2] and X[0]-X[1]==X[2]:
    print('?')
elif X[0]+X[1]==X[2]:
    print('+')
else:
    print('-')
============リストの順番・スライス================
S=list(input())
N=int(input())
print(S)

for i in range(N):
    r,l=map(int,input().split(' '))
    S=S[:r-1]+S[r-1:l][::-1]+S[l:]


print(S)

============辞書=========================
n=int(input())
Names={}
suji=0
ans=""

for i in range(n):
    Simei=input()
    if Simei in Names:
        Names[Simei] =int(Names[Simei])+1
    else:
        Names[Simei]=1

for j in Names:
    if Names[j] >suji:
        suji=Names[j]
        ans=j
print(ans)
===========pop==========================
N=int(input())
ryouri=[0,0]

for i in range(N):
    menu=int(input())
    if menu>ryouri[1]:
        ryouri.append(menu)
        ryouri.pop(0)
        continue
    elif ryouri[1]>menu>ryouri[0]:
        ryouri.insert(1,menu)
        ryouri.pop(0)
        continue
    else:
        continue

print(ryouri[0])
===========セット（重複しない）==========================
N=int(input())
menu=set()

for i in range(N):
    menu.add(int(input()))
print(sorted(menu)[-2])
=====================================
'''
