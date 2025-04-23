import timeit
from Deixtra import Deixtra

def test():
    graph = {}
    
    start_time = timeit.default_timer()
    result = Deixtra(graph, 'A')
    elapsed_time = timeit.default_timer() - start_time
    
    print("Кратчайшие расстояния:")
    for vertex, distance in result.items():
        print(f"{vertex}: {distance}")
    
    print(f"\nВремя выполнения: {elapsed_time:.6f} секунд")

if name == "__main__":
    test()