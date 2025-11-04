WHITE = (255, 255, 255)
BLUE = (70, 130, 255)
GREEN = (100, 255, 10)
RED = (255, 0, 0)

# ------------------ Node Klasse ------------------
class Node:
    def __init__(self, pos: tuple, g_cost: float = 0, h_cost: float = 0):
        self.pos = pos          # (row, col)
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = self.g_cost + self.h_cost
        self.parent = None
        self.color = WHITE
        self.neighbors = []

    def update_neighbors(self, grid):
        self.neighbors = []
        row, col = self.pos
        # Oben
        if row > 0 and grid[row-1][col].color != BLUE:
            self.neighbors.append(grid[row-1][col])
        # Unten
        if row < len(grid)-1 and grid[row+1][col].color != BLUE:
            self.neighbors.append(grid[row+1][col])
        # Links
        if col > 0 and grid[row][col-1].color != BLUE:
            self.neighbors.append(grid[row][col-1])
        # Rechts
        if col < len(grid[0])-1 and grid[row][col+1].color != BLUE:
            self.neighbors.append(grid[row][col+1])
