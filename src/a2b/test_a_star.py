from a2b.data_structures import *

wG = GridWithWeights(10, 10)

# Impassable cells.
wG.walls = [
    (3, 1), (3, 2), (3, 3), (3, 4),
    (6, 2), (6, 3), (6, 4), (6, 5),
    (1, 6), (2, 6), (3, 6), (4, 6),
    (7, 7), (7, 8),
]

# Cost to enter these cells; all other non-wall cells cost 1.
wG.weights = {
    (1, 1): 5, (2, 1): 5,
    (1, 2): 5, (2, 2): 5,
    (4, 4): 8, (5, 4): 8,
    (4, 5): 8, (5, 5): 8,
    (8, 2): 3, (8, 3): 3, (8, 4): 3,
    (1, 8): 6, (2, 8): 6, (3, 8): 6,
}





def test_draw_grid(grid: SquareGrid):
    return grid.draw_grid()


# class Cell:
#     def __init__(self) -> None:
#         self.parent_x = 0
#         self.parent_y = 0
#         self.f = float('inf')
#         self.g = float('inf')
#         self.h = 0
#
#
# def testAStar():
#     pass
