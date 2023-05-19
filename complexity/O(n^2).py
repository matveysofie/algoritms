# Сложность O(n^2) - квадратичная сложность:
# Описание: Время выполнения алгоритма увеличивается квадратично с размером входных данных.
# Примеры: Сортировка пузырьком (Bubble Sort), сортировка выбором (Selection Sort).

def quadratic_algo(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i], arr[j])


# Пример использования:
my_list = [1, 2, 3]
quadratic_algo(my_list)
# Вывод:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3
