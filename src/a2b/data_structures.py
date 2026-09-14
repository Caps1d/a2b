
import collections
from typing import Protocol


class Graph[Location](Protocol):
    def neighbors(self, id: Location) -> list[Location]:
        raise NotImplementedError




class SimpleGraph[Location]:
    def __init__(self) -> None:
        self.edges: dict[Location, list[Location]] = {}

    def neighbors(self, id: Location):
        return self.edges[id]

# example_graph = SimpleGraph[str]()
#
# example_graph.edges = {
#         'A' : ['B', 'D'],
#         'B' : ['C', 'A'], 
#         'C' : ['D'],
#         'D' : ['C']
#         }



class Queue[Element]:
    def __init__(self) -> None:
        self.elements = collections.deque[Element]()

    def empty(self) -> bool:
        return not self.elements # collections.deque has a truth element — when it has items it returns true, else false

    def put(self, element: Element):
        self.elements.append(element)

    def get(self) -> Element:
        return self.elements.popleft() # pop the first element





GridLocation = tuple[int, int]

class SquareGrid(Graph[GridLocation]):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls: list[GridLocation] = []

    def in_bounds(self, id: GridLocation) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, id: GridLocation) -> bool: 
        return id not in self.walls

    def neighbors(self, id: GridLocation) -> list[GridLocation]:
        (x, y) = id
        neighbors: list[GridLocation] = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        # see "Ugly paths" section for an explanation (https://www.redblobgames.com/pathfinding/a-star/implementation.html#troubleshooting-ugly-path):
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return list(results)

    def draw_grid(self) -> str:
        x, y = 0, 0

        grid = ""
        cols = "  "

        while x < self.width:
            cols += f"{x}  " 
            x += 1
        grid += cols + "\n"

        while y < self.height: 
            row = f"{y}"
            x = 0
            while x < self.width:
                loc: GridLocation = (x, y)
                if not self.passable(loc):
                    row += " # "
                else:
                    row += " * "
                x += 1
            grid += row + "\n"
            y += 1

        return grid



class WeightedGraph[Location](Graph[Location], Protocol):
    def cost(self, from_id: Location, to_id: Location) -> float: raise NotImplementedError

class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.weights: dict[GridLocation, float] = {}

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> float: 
        return self.weights.get(to_node, 1) #1 is the default value in case to_node isn't a key
