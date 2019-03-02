
============================================
============================================
============================================
============================================

============================================
============================================
================ABC67============================
N=int(input())
B=list(map(int,input().split()))
A=[]
for i in range(N):
    A.append(abs(B[i]))

A.sort()
A.reverse()
print(A)
x=0
y=0

for i in range(len(A)):
    if x<=y:
        x=x+int(A[i])
    else:
        y=y+int(A[i])

print(abs(x-y))
============================================
============ABC71C==========================
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

============================================
