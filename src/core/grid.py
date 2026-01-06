import pygame
from node import Node

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([]) # Erstellt die Zeile
        for j in range(rows):
            node = Node(i, j, gap)
            grid[i].append(node) # NUTZE .append() statt grid[i][j]
    return grid

def draw(win, grid):
    win.fill((255, 255, 255)) 

    for row in grid:
        for node in row:
            node.draw(win)

    # Zeichne hier optional Gitterlinien (Grid Lines)
    draw_grid_lines(win, len(grid), grid[0][0].width)
    
    pygame.display.update()

def draw_grid_lines(win, rows, width_per_node):
    """Zeichnet graue Linien zwischen den Nodes für bessere Sichtbarkeit"""
    GAP = width_per_node
    for i in range(rows):
        # Horizontale Linien
        pygame.draw.line(win, (200, 200, 200), (0, i * GAP), (rows * GAP, i * GAP))
        for j in range(rows):
            # Vertikale Linien
            pygame.draw.line(win, (200, 200, 200), (j * GAP, 0), (j * GAP, rows * GAP))

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos # Korrektur: In Pygame ist pos = (x, y)

    row = x // gap
    col = y // gap
    return row, col