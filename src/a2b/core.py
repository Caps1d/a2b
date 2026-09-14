
from a2b import test_a_star
from a2b.algos import A_Star
from a2b.data_structures import *


def main() -> None:
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

    drawing = test_a_star.test_draw_grid(wG)
    print(drawing)

    start: GridLocation = (1,1)
    goal: GridLocation = (5,5)

    aStar = A_Star()

    (came_from, total_cost) = aStar.search(wG, start, goal, aStar.manhattan_distance)


    path = aStar.reconstruct_path(came_from, start, goal)
    print(path)

    # for loc in path:
    #     print(loc)



if __name__ == "__main__":
    main()
