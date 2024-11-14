"""Q.2) Write a Python program to implement A* algorithm. Refer
 the following graph as an Input for the program.
 [Start vertex is A and Goal Vertex is G]"""

from queue import PriorityQueue

def a_star_algorithm(graph, heuristic, start, goal):
    open_list = PriorityQueue()
    open_list.put((0, start))
    g_costs = {start: 0}
    parents = {start: None}

    while not open_list.empty():
           current = open_list.get()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            g_cost = g_costs[current] + cost
            if neighbor not in g_costs or g_cost < g_costs[neighbor]:
                g_costs[neighbor] = g_cost
                f_cost = g_cost + heuristic[neighbor]
                open_list.put((f_cost, neighbor))
                parents[neighbor] = current
    return None

graph = {
    'A': [('B', 9), ('C', 4), ('D', 21)],
    'B': [('A', 9), ('E', 11)],
    'C': [('A', 4), ('E', 17), ('F', 12)],
    'D': [('A', 21), ('F', 14)],
    'E': [('B', 11), ('C', 17), ('G', 5)],
    'F': [('C', 12), ('D', 14), ('G', 9)],
    'G': [('E', 5), ('F', 9)]
}

heuristic = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'G': 0
}

path = a_star_algorithm(graph, heuristic, 'A', 'G')
print("Path from A to G:", path)


#python3 a_star_algorithm.py

"""Output:
Path from A to G: ['A', 'C', 'F', 'G']"""