'''Write a function to find the shortest path from a source vertex to all other 
vertices in a graph using Dijkstra's algorithm.
Sample Test Case
Input: graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}, source = 0 Output: {0: 0, 1: 3, 2: 1, 3: 4}'''

import sys
import heapq

def dijkstra(graph, source):
    
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[source] = 0

    
    pq = [(0, source)]

    while pq:
        
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            tentative_distance = distances[current_vertex] + weight
            
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                heapq.heappush(pq, (tentative_distance, neighbor))

    return distances

#Output
graph = {0: {1: 4, 2: 1}, 1: {3: 1}, 2: {1: 2, 3: 5}, 3: {}}
source = 0
print(dijkstra(graph, source))  