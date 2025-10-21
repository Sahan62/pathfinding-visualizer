import pygame

pygame.init()

# ------------------ Fenster ------------------
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pathfinding Visualizer')

# ------------------ Farben ------------------
GREY = (60, 60, 60)
BG = (0, 0, 0)
GREEN = (100, 255, 10)  # Start
RED = (255, 0, 0)       # Ziel
BLUE = (70, 130, 255)   # Hindernis
WHITE = (255, 255, 255) # Leer

# ------------------ Grid ------------------
ROWS = 20
TILE_SIZE = SCREEN_WIDTH // ROWS
grid = [[WHITE for _ in range(ROWS)] for _ in range(ROWS)]

# Start- und Zielpunkt
start = None
end = None

# ------------------ Funktionen ------------------
def draw_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            pygame.draw.rect(SCREEN, grid[row][col],
                             (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    # Gitternetzlinien
    for x in range(TILE_SIZE, SCREEN_WIDTH, TILE_SIZE):
        pygame.draw.line(SCREEN, GREY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(TILE_SIZE, SCREEN_HEIGHT, TILE_SIZE):
        pygame.draw.line(SCREEN, GREY, (0, y), (SCREEN_WIDTH, y))

# ------------------ Hauptloop ------------------
running = True
while running:
    SCREEN.fill(BG)
    draw_grid(grid)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ------------------ Maussteuerung ------------------
        if pygame.mouse.get_pressed()[0]:  # Linksklick
            pos = pygame.mouse.get_pos()
            row = pos[1] // TILE_SIZE
            col = pos[0] // TILE_SIZE

            if grid[row][col] == WHITE:
                if not start:
                    start = (row, col)
                    grid[row][col] = GREEN
                elif not end:
                    end = (row, col)
                    grid[row][col] = RED
                else:
                    grid[row][col] = BLUE  # Hindernis

        if pygame.mouse.get_pressed()[2]:  # Rechtsklick
            pos = pygame.mouse.get_pos()
            row = pos[1] // TILE_SIZE
            col = pos[0] // TILE_SIZE
            # Zelle zurücksetzen
            if (row, col) == start:
                start = None
            if (row, col) == end:
                end = None
            grid[row][col] = WHITE

pygame.quit()

