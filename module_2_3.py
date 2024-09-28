my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_index = 0 # задаю переменную: индекс элемента списка my_list
while my_index < len(my_list): # цикл по условию my_index меньше длины списка
    if my_list[my_index] > 0: # условие для вывода положительных элементов и переход на следующий индекс
        print(my_list[my_index])
        my_index = my_index + 1
    elif my_list[my_index] == 0: # условие для перехода на следующий индекс без вывода на экран
        my_index = my_index + 1
    else: # выполняется только при отрицательном элементе
        break
