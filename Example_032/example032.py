my_list = input('Введите список чисел: ').split()
min_el = int(input('Введите минимальный элемент: '))
max_el = int(input('введите максимальный элемент: '))
list_result = []
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
    if min_el<=my_list[i]<=max_el:
        list_result.append(i)
print(*list_result)
