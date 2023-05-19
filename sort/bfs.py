from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)  # Можно добавить дополнительную обработку вершины здесь

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)


# Пример использования:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')


# Алгоритм поиска в ширину (Breadth-First Search, BFS) используется для обхода или поиска в графе. Он начинает с заданной вершины и посещает все смежные вершины на текущем уровне,
# прежде чем переходить к следующему уровню.
