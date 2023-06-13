x = int(input())
y = int(input())
def operation(x,y):
    a = [a for a in range(x)]
    print(a)
    for i in range(y):
        b = list(map(lambda x: x * (i + 1), a))
        print(b)
operation(x, y)