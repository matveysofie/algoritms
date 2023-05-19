# Сложность O(n log n) - линейно-логарифмическая сложность:
# Описание: Время выполнения алгоритма увеличивается пропорционально произведению размера входных данных на логарифм этого размера.
# Примеры: Быстрая сортировка (Quick Sort), сортировка слиянием (Merge Sort).

def nlogn_algo(arr):
    sorted_arr = sorted(arr)
    return sorted_arr


# Пример использования:
my_list = [5, 3, 1, 4, 2]
result = nlogn_algo(my_list)
print(result)  # Вывод: [1, 2, 3, 4, 5]
