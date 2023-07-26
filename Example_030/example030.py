a1 = int(input('Введите перввй элемент арифметической прогрессии: '))
d = int(input('Введите разность арифметической прогрессии: '))
n = int(input('Введите количество элементов арифметической прогрессии: '))
result = []
result.append(a1)
for _ in range(n-1):
    a1 +=d
    result.append(a1)
print(*result)

