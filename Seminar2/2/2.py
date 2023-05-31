a = []
b = int(input())
c = 0
for i in range(b):
    a.append(i+1)

print(a)
x = int(input())
c = 0
for i in a:
    if x == i - 1 or x == i + 1:
        c += 1
        print(i)
    
if c == 0 and max(a) < x:
    print(max(a))
else :
    print(min(a))
