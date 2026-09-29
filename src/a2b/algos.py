import math
import heapq
from typing import Dict

from a2b.data_structures import Graph, GridLocation, WeightedGraph


class A_Star:

    def __init__(self):
        pass


    def reconstruct_path(self, came_from: dict, start: Location,  current: Location):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

            if current == start:
                break

        # reversing the path list to return A -> B -> C
        # ans = [path[p] for p in range(len(path)-1, -1)]
        return path




    def search(self, graph: WeightedGraph[Location], start: Location, goal: Location, h):
        frontier = []
        heapq.heapify(frontier)

        came_from: dict[Location: Location] = {}
        cost_so_far: dict[Location: float] = {}

        came_from[start] = start
        cost_so_far[start] = 0

        heapq.heappush(frontier, (0, start))

        while len(frontier) > 0: 
            #heappop returns [cost, value]
            current: Location = heapq.heappop(frontier)[1] 
            
            if current == goal:
                break
            
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + graph.cost(current, next)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    priority = new_cost + h(next, goal)
                    came_from[next] = current
                    cost_so_far[next] = new_cost
                    heapq.heappush(frontier, (priority, next))

        return came_from, cost_so_far

    def getTotalCost(self, costs: dict[Location, float], goal: Location):
        return costs[goal]






    
    # if no blocks in the graph, use Euclidean distance to calc h
    def euclidean_distance(self, start: Location, goal: Location):
        (x1, y1) = start
        (x2, y2) = goal
        delta_x = math.pow(x2 - x1, 2)
        delta_y = math.pow(y2 - y1, 2)
        return math.sqrt(delta_x + delta_y)

    def manhattan_distance(self, start: Location, goal: Location):
        (x1, y1) = start
        (x2, y2) = goal
        return abs(x1 - x2) + abs(y1 - y2)

    # def triangle_inequality(self, wG: WeightedGraph, start: Location, goal: Location, landmark: Location):
    #     delta_start = wG.weights[(start, landmark)]
    #     delta_goal= wG.weights[(start, landmark)]

    def zero_distance(self, start: Location, goal: Location):
        return 0


# class node:
#     x = 0
#     y = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
