# Сложность O(2^n) - экспоненциальная сложность:
# Описание: Время выполнения алгоритма увеличивается экспоненциально с размером входных данных.
# Примеры: Решение задачи коммивояжера методом полного перебора, генерация всех подмножеств множества.

def exponential_algo(n):
    if n <= 0:
        return
    print("Hello")
    exponential_algo(n - 1)
    exponential_algo(n - 1)


# Пример использования:
exponential_algo(3)
# Вывод:
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello
