# сортировка слиянием
def merge_sort(array): # "разделяй"
    if len(array) < 2: # если кусок массива меньше 2,
        return array[:] # выходим из рекурсии
    else:
        middle = len(array) // 2 # ищем середину
        left = merge_sort(array[:middle]) # рекурсивно делим левую часть
        right = merge_sort(array[middle:]) # и правую
        return merge(left, right) # выполняем слияние

def merge(left, right): # "властвуй"
    result = [] # результирующий массив
    i,j = 0,0 # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

# двоичный поиск
def binary_search(array, element, left, right):
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует

    middle = (right+left) // 2
    # находим номер позиции элемента, который меньше введенного пользователем числа,
    # а следующий за ним больше или равен этому числу
    if array[middle-1] < element and element <= array[middle]:
        return middle-1
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)


array = list(map(int, input("Введите последовательность чисел (через пробел): ").split()))

sorted_array = merge_sort(array) # сортируем массив
print(sorted_array) # выводим отсортированный массив

left = min(sorted_array)  # нижняя граница массива
right = max(sorted_array)   # верхняя граница массива

while True:
    try:
        element = int(input("Введите любое число: "))
        if element < left or element > right:
            print("Указанное число не входит в диапазон списка!")
        if element < 0:
            raise Exception
        break
    except ValueError:
        print("Необходимо ввести целое число.")
    except Exception:
        print("Необходимо ввести положительное число.")


print("Номер позиции элемента, который меньше введенного числа,\n а следующий за ним больше или равен этому числу:", binary_search(sorted_array, element, 0, len(sorted_array)-1))

#5 1 4 7 3 6 9 0 2 8
