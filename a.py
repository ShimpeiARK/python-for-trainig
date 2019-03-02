#!/usr/bin/python
# -*- Coding: utf-8 -*-





array = list(map(int, input(),split(' ')))
2転換距離





'''
=============================
import random
def randomlist(size):
    list＝[]
    for i in range(1,size+1):
        list.append(random.randint(0,100)):
    return list
print (list)
=============================
list=["A","B","C"]
list.append("D")
print(list)
============================
a=input()
for i in range(int(a)):
    print('Hello!')
=============================
import sys
m=0
for i in range (30):
    if m%15==0:
        print('fizzbuzz')
        m+=1
    elif m%3==0:
        print('fizz')
        m+=1
    elif m%5==0:
        print('buzz')
        m+=1
    else:
        print(m)
        m+=1
=============================
sum=0
for x in range (1,51):
    sum += x
print (sum)
=============================
def checkio(number):
    if number%5 ==0 and number%3 ==0:
        print("Fizz Buzz")
    elif number%5 ==0:
        print("Buzz")
    elif number%3 ==0:
        print("Fizz")
    else:
        print(str(number))
=============================
max=int(10)
x,y=int(1),int(1)
for i in range(max):
    print (x,y)
    x=x+y
    y=x+y
=============================
int(input())

if sei%100==0 and sei%400 !=0:
    print('heinenn')
elif sei%4 ==0:
    print('uruudosi')
else:
    print('heinenn')
=============================
s=0
for i in range(1,50):
    s= s+i
print(s)
=============================
#!/usr/bin/python
# coding: utf-8

def keisan(a,b):
  if a > b:
    while b != 0:
      r = a
      a = b
      b = r % b

    return a

  else:
      print ("AにはBより大きい数字を入れて下さい。")
      exit()

a = int(input())
b = int(input())
c = keisan(a,b)
print (a,"と",b,"の最大公約数は",c,"です。")
=============================
import math
a =input()
b=math.sqrt(int(a))
print ("%.5f"% (b))
=============================
N=int(input())
c=int(input())
a=[0]
for N in set(c):
    a.append(c.count(N))
print(max(a),min(a))
=============================
N=int(input())
c=list(int(input()))

ans=[0,0,0,0]
for i in range(N):
    if c[i]==1:
        ans[0]+=1
    elif c[i]==2:
        ans[1]+=1
    elif c[i]==3:
        ans[2]+=1
    else:
        ans[3]+=1

ans.sort()

print(str(ans[3])+""+str(ans[0]))

=============================
N=int(input())
c=input()

ans_max=0
ans_min=N

for i in range(1,5):
    tmp=c.count(str(i))
    ans_max=max(ans_max,tmp)
    ans_min=min(ans_min,tmp)

print(ans_max,ans_min)

=============================
A,B = map(int, input().split())

C=abs(A-B)
co=int(0)

while C>=8:
    co+=1
    C-=10
while 3<=C<8:
    co+=1
    C-=5
C=abs(C)

print(C+co)
=============================
N=int(input())
c=input()
GPA=int(0)

for i in c:
    if i=="A":
        GPA+=4
    elif i=="B":
        GPA+=3
    elif i=="C":
        GPA+=2
    elif i=="D":
        GPA+=1
    elif i=="F":
        GPA+=0

GPA=GPA/N
print(GPA)

=============================
A,B=map(int,input().split(" "))
if A>=B:
    print(A)
else:
    print(B)

'''

if A[0]>=A[1]:
    print(A[0])
else:
    print(A[1])

'''


A=input().split(" ")

if int(A[0])>=int(A[1]):
    print(A[0])
else:
    print(A[1])

=============================
N=int(input())
s=0
for i in range(1,N+1):
    s+=10000*i*(1/N)
print(s)

=============================
N=int(input())

if N%100==0 and N%400 !=0:
    print('NO')
elif N%4 ==0:
    print('YES')
else:
    print('NO')
=============================
a,b = input(), input()
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
print (gcd(int(a),int(b)))
=============================
'''
