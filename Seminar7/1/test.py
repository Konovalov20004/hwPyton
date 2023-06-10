a = input().split(" ")
# for i in range(len(a)):
#     a[i] = list([x for x in a[i] if x == 'a'])
a = list( i for i in range(len(a)) for x in a[i] if x == 'a')
print(a)