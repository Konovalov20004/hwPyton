a = input().split(" ")
for i in range(len(a)):
    a[i] = list([x for x in a[i] if x == 'а'])
print(a)
if a.count(a[0]) == len(a):
    print("Парам пам-пам")
else: 
    print("Пам парам")