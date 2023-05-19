# Сложность O(n!) - факториальная сложность:
# Описание: Время выполнения алгоритма увеличивается факториально с размером входных данных.
# Примеры: Решение задачи коммивояжера методом полного перебора всех перестановок, генерация всех возможных перестановок множества.

import itertools


def factorial_algo(n):
    perms = list(itertools.permutations(range(n)))
    for perm in perms:
        print(perm)


# Пример использования:
factorial_algo(3)
# Вывод:
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1
