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
