def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Пример использования:
my_list = [5, 2, 8, 12, 3]
sorted_list = quick_sort(my_list)
print(sorted_list)  # Вывод: [2, 3, 5, 8, 12]

# Алгоритм быстрой сортировки использует стратегию "разделяй и властвуй".
# Он выбирает элемент, называемый опорным, и разделяет список на две подгруппы: элементы, меньшие опорного, и элементы, большие опорного.
# Затем алгоритм рекурсивно применяется к каждой из подгрупп.
