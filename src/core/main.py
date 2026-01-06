import pygame
from grid import make_grid, draw, get_clicked_pos

WINDOW_WIDTH = 800
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_WIDTH))
pygame.display.set_caption("Pathfinding Visualizer")

def main():
    ROWS = 50 
    grid = make_grid(ROWS, WINDOW_WIDTH)
    start = None
    end = None
    
    run = True
    while run:
        draw(SCREEN, grid)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

           
            if pygame.mouse.get_pressed()[0]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WINDOW_WIDTH)
                
                if 0 <= row < ROWS and 0 <= col < ROWS:
                    node = grid[row][col]
                    
                    # Logik-Reihenfolge:
                    if not start and node != end:
                        start = node
                        start.make_start()
                    
                    elif not end and node != start:
                        end = node
                        end.make_end()
                    
                    elif node != end and node != start:
                        node.make_wall()

            
            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WINDOW_WIDTH)
                
                if 0 <= row < ROWS and 0 <= col < ROWS:
                    node = grid[row][col]
                    node.reset()
                    if node == start:
                        start = None
                    if node == end:
                        end = None
            
          
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c: # 'c' zum kompletten Leeren
                    start = None
                    end = None
                    grid = make_grid(ROWS, WINDOW_WIDTH)

    pygame.quit()

if __name__ == "__main__":
    main()