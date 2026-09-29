import unittest

from a2b.data_structures import * 
from a2b.algos import *

class TestDataStructures(unittest.TestCase): 
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

    def test_draw_graph(self):
        grid = self.weightedGrid
        print(2*'\n', grid.draw_grid())

    def test_draw_grid_with_path(self):
        aStar = A_Star()

        start: GridLocation = (1,1)
        goal: GridLocation = (5,5)

        grid = self.weightedGrid
        (came_from, costs) = aStar.search(grid, start, goal, aStar.manhattan_distance)

        path: list[tuple] = aStar.reconstruct_path(came_from, start, goal)
        print(2*'\n', grid.draw_grid_with_path(path))
 
