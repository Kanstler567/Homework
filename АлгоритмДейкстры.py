import heapq

def dijkstra(graph, start_vertex):
    # Инициализируем массив бесконечных расстояний
    distances = {vertex: float('inf') for vertex in graph}
    
    # Расстояние до самой себя нулевое
    distances[start_vertex] = 0
    
    # Очередь с приоритетом (расстояние, вершина)
    priority_queue = [(0, start_vertex)]
    
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Проверяем, является ли текущее расстояние актуальным
        if current_distance > distances[current_vertex]:
            continue
            
        # Обрабатываем соседей текущего узла
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Если найдена новая лучшая дорога
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances


# Пример задания графа с взвешенными рёбрами
graph = {
    '0': {'1': 2, '2': 3},   # Из вершины 0 дуги ведут в 1 и 2 с соответствующими весами
    '1': {'0': 2, '2': 1},
    '2': {'0': 3, '1': 1},
    '3': {},
    '4': {},
    '5': {},
    '6': {},
    '7': {},
    '8': {},
    '9': {}
}

# Поиск кратчайших путей начиная с вершины '0'
shortest_paths = dijkstra(graph, '0')
print(shortest_paths)