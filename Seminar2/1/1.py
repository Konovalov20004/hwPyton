a = []
b = int(input())
c = 0
for i in range(b):
    c += 1
    a.append(c)

print(a)
x = int(input())
print(a.count(x))