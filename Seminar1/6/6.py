a = int(input())
b = a % 1000
c = a // 1000
sc = 0
sb = 0
while c != 0 and b != 0:
    sb += b % 10
    b //= 10
    sc += c % 10
    c //= 10
    print(sc, sb)

if sc == sb:
    print("yes")
else:
    print("no")