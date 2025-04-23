def dexter(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph):
        current_vertex = None
        min_distance = float('infinity')
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                current_vertex = vertex
        
        if current_vertex is None:
            break
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances