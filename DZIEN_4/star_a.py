import heapq

def gready_best_first_search(graph,start,goal,h):
    #inicjalizacja kopca
    frontier = []
    heapq.heappush(frontier,(h(start,goal)),start)

    #słownik przechowujący informację skąd przyszliśmy do danego węzła
    came_from = {}
    came_from[start] = None

    while frontier:
        #pobranie węzła o najmniejszej wartości heurystyki h
        _, current = heapq.heappop(frontier)

        #jesli osiągnięto cel - rekonstrukcja ścieżki
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

    return None

def heuristic(a,b):
    #funkcja heurystyczna - odległośc Manhattan
    (x1,y1) = a
    (x2,y2) = b
    return abs(x1-x2) + abs(y1-y2)


graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(1, 0): 1, (0, 1): 1, (2, 2): 1},
    (2, 2): {}
}
