import timeit
from Deixtra import Deixtra

def test():
    graph = {
        'A': {'B': 3, 'D': 2},
        'B': {'A': 3, 'C': 1},
        'C': {'B': 1, 'D': 6},
        'D': {'A': 2, 'C': 6,
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