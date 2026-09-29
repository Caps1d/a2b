import unittest

from a2b.algos import *
from a2b.data_structures import *


class TestAStar(unittest.TestCase):
    weightedGrid = GridWithWeights(10, 10)

    # Impassable cells.
    weightedGrid.walls = [
        (3, 1), (3, 2), (3, 3), (3, 4),
        (6, 2), (6, 3), (6, 4), (6, 5),
        (1, 6), (2, 6), (3, 6), (4, 6),
        (7, 7), (7, 8),
    ]

    # Cost to enter these cells; all other non-wall cells cost 1.
    weightedGrid.weights = {
        (1, 1): 5, (2, 1): 5,
        (1, 2): 5, (2, 2): 5,
        (4, 4): 8, (5, 4): 8,
        (4, 5): 8, (5, 5): 8,
        (8, 2): 3, (8, 3): 3, (8, 4): 3,
        (1, 8): 6, (2, 8): 6, (3, 8): 6,
    }
 
    weightedGraph = GraphWithWeights()

    # edges
    weightedGraph.edges = {
            'A' : ['B'],
            'B' : ['C'],
            'C' : ['A', 'D'],
            'D' : ['C', 'E', 'F'],
            'E' : ['F', 'G'], 
            'F' : [],
            'G' : ['H'], 
            'H' : []
            }

    # weights
    weightedGraph.weights = {
            ('A', 'B') : 2, 
            ('A', 'C') : 3, 
            ('B', 'C') : 2, 
            ('C', 'A') : 3,
            ('C', 'D') : 1, 
            ('D', 'C') : 1, 
            ('D', 'E') : 4, 
            ('D', 'F') : 2, 
            ('E', 'D') : 4, 
            ('E', 'F') : 1, 
            ('E', 'G') : 2, 
            ('G', 'H') : 1
            }

    def test_aStar_weightedGrid(self): 
        aStar = A_Star()

        start: GridLocation = (1,1)
        goal: GridLocation = (5,5)


        (came_from, costs) = aStar.search(self.weightedGrid, start, goal, aStar.manhattan_distance)

        path: list[tuple] = aStar.reconstruct_path(came_from, start, goal)

        print(path)
        print(f"start: {path[-1]}, finish: {path[0]}")
