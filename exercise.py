x = 2
print(x * 3)

print('###########################################')

a = 100
b = 200
a,b = b, a
print(a, b)

print('###########################################')

a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print('###########################################')

a = 5
b = 3
print(a % b)

print('###########################################')

a = 5
b = 10
print(a ** b)

print('###########################################')

a = 5
b = 10

if a < b:
    print(b)
else:
    print(a)

print('###########################################')

a = 5
print(a % 2 == 0)

print('###########################################')

a = 'py'
b = 'thon'
print(a + b)

print('###########################################')

a = 5
b = 3
# print(str(a) + '%'+ str(b) + '=2')
ans = "{}%{}={}".format(a, b, a%b)
print(ans)

print('###########################################')

str = 'some1'
str = str.replace('1', 'one')
print(str)

print('###########################################')

str = 'This Is A Sentence .'
str = str.lower()
print(str)

print('###########################################')

str = 'This Is A Sentence .'
str = str.upper()
print(str)

print('###########################################')

str = 'How many characters?'
print(len(str))

print('###########################################')

a = '34'
b = '43'
ans = int(a) + int(b)
print(ans)

print('###########################################')

l =[1, 2, 3, 4, 5]
print(l[2])

print('###########################################')

l1 = [1, 2, 3]
l2 = [4, 5]
print(l1 + l2)

print('###########################################')

l =[1, 2, 3, 4, 5]
l.append(6)
l.append(7)
print(l)

print('###########################################')

l = [1, 2, 3, 4, 5]
l.insert(1, 100)
print(l)

print('###########################################')

l = [1, 2, 3, 4, 5]

for i in l:
    if i %2 == 0:
        print(i)

print('###########################################')

l = [1, 2, 3, 4, 5]
for idx, elem in enumerate(l):
    if idx %2 == 0:
        print(elem)

print('###########################################')

l = [11, 22, 33, 44, 55, 66]
print(len(l))

print('###########################################')

l = [11, 22, 33, 44, 55]
if 44 in l:
    print(True)
else:
    print(False)

print('###########################################')

l = [1, 2, 3, 4, 5]
t = (l[0], l[-1])
print(t)

print('###########################################')

d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print(d)

print('###########################################')

d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print(list(d.keys()))

print('###########################################')

d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print(list(d.values()))

print('###########################################')

d= {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
print(list(d.items()))

print('###########################################')

d={'apple': 10, 'grape': 20, 'orange': 30}
d['apple'] = d.get('apple', -1)
d['pineapple'] =d.get('pineapple', -1)
print(d)

print('###########################################')

a = 'training'
print(a[1:5])

print('###########################################')

s = 'understand'
print(s[1::2])

print('###########################################')

l = [1, 2, 3, 4, 5]
print(l[::-1])

print('###########################################')

li = [1, 2, 3, 4, 5]
print(set(li))

print('###########################################')

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 & set2)

print('###########################################')

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 | set2)

print('###########################################')

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 - set2)

print('###########################################')

data1 = {'A': 1, 'B': 2}
data2 = 'hoge'
data3 = {1, 2, 3, 4, 5}
print(type(data1))
print(type(data2))
print(type(data3))