a = int(input())
b = int(input())
def summ(a, b):
    if b == 0:
        return a
    a += 1
    b -= 1
    return summ(a, b)

print(summ(a, b))