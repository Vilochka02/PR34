print("Задание №1")
a =int (input())
b =int (input())
c =int (input())
d =int (input())
for g in range (c,d+1):
    print('\t'+str(g),end='')
print(end='\n')
for i in range (a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(i*j),end='\t')
    print(end='\n')

print("Задание №2")
a = 0
while a<=100:
  a = int (input())
  if a > 100:
    break
  if a<10:
    continue
  print(a)

print("Задание №3")
data = int(input())
res = 0
while data != 0:
    res += data
    data = int(input())
print (res)

print("Задание №4")
a = int(input())
b = int(input())
res = a
while res % b != 0:
    res += a
print(res)

print("Задание №5")
a = int (input())
b = int (input())
s = 1
k = 2
while s<k:
  if s % a == 0 and s % b == 0:
    k=s
  else:
    s=s+1
    k=k+1
print(s)

print("Задание №6")
a =  input() # input auto use type str
s1 = a.upper().count('c'.upper())
s2 = a.upper().count('g'.upper())
S=s1+s2
print(S/len(a)*100)

print("Задание №7")
s = str(input())
l = len(s)-1
c = 1
t = ''
if len(s)==1:
    t = t +s+str(c)
else:
    for i in range(0,l):
        if s[i]==s[i+1]:
            c +=1
        elif s[i]!=s[i+1]:
            t = t + s[i]+str(c)
            c = 1
    for j in range(l,l+1):
        if s[-1]==s[-2]:
            t = t +s[j]+str(c)
        elif s[-1]!=s[-2]:
            t = t +s[j]+str(c)
            c = 1
print(t)

print("Задание №8")
s = [ int(i) for i in input().split()]
summ = 0 
l = len(s)-1
for i in range(0,l+1):
    summ = summ + s[i]
print(summ)

print("Задание №8")
s = [ int(i) for i in input().split()]
t = []
l = len(s)-1
k = 0
i = 0
if len(s)==0:
    print(str(0))
else:
    for st in s:
        if len(s)>1:
            if i==0:
                k = s[i+1] + s[-1]
                t.append(k)
            elif i>0 and i<l:
                k=s[i-1]+s[i+1]
                t.append(k)
            elif i==l:
                k = s[i-1]+s[0]
                t.append(k)
        elif len(s)==1:
            k = s[i]
            t.append(k)       
        i +=1
    j = 0
    for st2 in t:
        print(str(t[j])+' ',end='')
        j +=1

print("Задание №9")
s = [ int(i) for i in input().split()]
t = []
s.sort()
l = len(s)-1
k = 100000
if len(s)!=1:
    for i in range(0,l):
        if s[i]==s[i+1] and s[i]!=k:
            t.append(s[i])
            k=s[i]
    for j in range(l,l+1):
        if s[-1]==s[-2] and s[j]!=k:
            t.append(s[j])
n = len(t)
for g in range(0,n):
    print(t[g],end=' ')

print("Задание №10")
a1 = int (input())
s= a1
s2 = 0+abs(a1**2)
while s!=0:
    a1 = int(input())
    s = s + a1
    s2 = s2+abs(a1)**2
    if s==0:
        break
print(s2)

print("Задание №11")
p = []
t = []
M = []
n = int(input())
l = len(t)
k = 0
m = 2
for h in range(1,n+1):
    p.append(str(h))
for i in range(0,len(p)):
    if i==0:
        t.insert(l,p[i])
        k = 0
    elif i==1:        
        while i>=k:
            l = len(t)
            t.insert(l,p[i])
            k +=1
        k -=2
    elif i>1:
        while i>=k:
            l = len(t)
            t.insert(l,p[i])
            k +=1
        k =i-m
        m +=1
    l = len(t)
x = len(t)
if len(t)==1:
    print(1)
else:
    for j in range (0,x-1):
        M.append(t[j])
    for g in range(0,n):
        print(M[g],end=' ')
        
print("Задание №12")
lst = [int(i) for i in input().split()]
x = int(input())

for i in range(len(lst)):
	if x == lst[i]:
		print(i, end=' ')

if x not in lst:
    print('Отсутствует')
    
print("Задание №13")
n = ''
m = []
while True:
    n = str(input()) # ввод строк
    if n == 'end':
        break
    m.append([int(s) for s in n.split()]) 
li, lj = len(m), len(m[0])
new = [[sum([m[i-1][j], m[(i+1)%li][j], m[i][j-1], m[i][(j+1)%lj]]) for j in range(lj)] for i in range(li)]

for i in range (li):
    for j in range (lj):
        print(new[i][j], end =' ')
    print()
    

