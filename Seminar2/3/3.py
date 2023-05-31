score = (1, 2, 3, 4, 5, 8, 10)
point = ("AEIOULNSTRАВЕИНОРСТ", "DGДКЛМПУ", "BCMPБГЁЬЯ", "FHVWYЙЫ", "KЖЗХЦЧ", "JXШЭЮ", "QZФЩЪ")
x = str(input())
c = 0
for i in x:
    b = 0
    while b < len(point):
        if i in point[b]:
            c += score[b]
        b += 1
print(c)