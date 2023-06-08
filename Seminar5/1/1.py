a = int(input())
b = int(input())
def stepen(a, b, i = a):
    if b == 1:
        return a
    a *= i
    b -= 1
    return stepen(a, b)

if b == 0:
    print(1)
else:
    print(stepen(a, b))