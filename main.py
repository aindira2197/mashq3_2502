# 1
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
print(s)

# 2
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i ** 2 + i)

# 3
a = int(input())
b = int(input())
c = 0
for i in range(a, b + 1):
    if i % 4 == 0:
        c += i
print(c)

# 4
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 2 == 1:
        print(i)

# 5
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i * 3)
