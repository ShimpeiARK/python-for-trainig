import math
N=int(input())
d=[]
h=int(0)

for k in range(1,N+1):
    x, y=map(int, input().split(' '))
    d.append((x,y))

for i in range(0,N):
    for j in range(0,N):
            h=max(h,pow(d[i][0]-d[j][0],2)+pow(d[i][1]-d[j][1],2))

print("%.8f" % math.sqrt(h))
==================================================
N=int(input())
if N%3==0:
    print('YES')
else:
    print('NO')


a,b =map(int,input().split(' '))
c=b//a

print(c)

==================================================
N=int(input())

cou=divmod(N,2)
cou=int(cou[0])+int(cou[1])

print(cou)
==================================================
N=input()
M=N+'pp'
print(M)
==================================================



'''
W=list(input())
for x in W:
    if x not in ["a","i","u","e","o"]:
        print(x, end="")
print()
for i in range (1,30):
    if i >15:
        print(i)

=====================================
class MyClass:
def __init__(self,text):
    slef.value =text

def print_value(self):
    print(self.value)

if __name__=="__main__":
    a = MyClass("123")
    b = MyClass("abc")

print(a.value) #123
a.print_value() #123
=====================================
N=int(input())
lst=[]
for x in range(1,N+1):
    lst.append(int(input()))
min_value=min(lst)
print(min_value)
=====================================
C=[]
for _ in range(4):
    C.append(input())
print(C)
for i in reversed(range(4)):
    print(C[i][::-1])
=====================================
=====================================
=====================================
=====================================
=====================================
W=input()
H=W.replace('a','')
H=W.replace('i','')
H=W.replace('u','')
H=W.replace('e','')
H=W.replace('o','')
print(H)

'''
'''
z=int(input())
m=z/1000
W=int(0)
if m<0.1:
    print('00')
elif m<=5:
    W=m*10
    print("{0:2d}".format(W))
elif m<=30:
    W=m+50
    print(W)
elif m<70:
    W=(m-30)/5+80
    print(W)
else:
    W=89
    print(W)
'''
'''
W=list(input())
for x in W:
    if x not in ["a","i","u","e","o"]:
        print(x, end="")
print()
'''
==================================================
==================================================
