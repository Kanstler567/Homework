import timeit
from Deixtra import Deixtra

def test():
    graph = {
        'A': {'B': 3, 'D': 2, 'E': 5},
        'B': {'A': 3, 'C': 1, 'F': 4},
        'C': {'B': 1, 'D': 6, 'G': 2},
        'D': {'A': 2, 'C': 6, 'E': 1, 'H': 3},
        'E': {'A': 5, 'D': 1, 'F': 2, 'I': 4},
        'F': {'B': 4, 'E': 2, 'G': 3, 'J': 1},
        'G': {'C': 2, 'F': 3, 'H': 5},
        'H': {'D': 3, 'G': 5, 'I': 2},
        'I': {'E': 4, 'H': 2, 'J': 3},
        'J': {'F': 1, 'I': 3}
    }
    
    start_time = timeit.default_timer()
    result = Deixtra(graph, 'A')
    elapsed_time = timeit.default_timer() - start_time
    
    print("Кратчайшие расстояния от A:")
    for vertex in sorted(result.keys()):
        print(f"{vertex}: {result[vertex]}")
    
    print(f"\nВремя выполнения: {elapsed_time:.6f} секунд")

if name == "__main__":
    test()