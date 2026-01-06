#node.py
import pygame


#definiere die Farben 

WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)
ROT = (255, 0, 0)
GRÜN = (0, 255, 0)

class Node:
    def __init__(self, row, col, width):
        self.row = row        # Zeile im Gitter
        self.col = col        # Spalte im Gitter
        self.x = row * width  # Tatsächliche Pixel-Position X
        self.y = col * width  # Tatsächliche Pixel-Position Y
        self.color = WEISS    # Startfarbe
        self.width = width    # Quadratgröße

    def draw(self, screen):
        # Zeichne ein ausgefülltes Quadrat an der Position x, y
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def make_start(self):
        self.color = GRÜN

    def make_end(self):
        self.color = ROT

    def make_wall(self):
        self.color = SCHWARZ

    def is_wall(self):
        return self.color == SCHWARZ
    
    def reset(self):
        self.color = WEISS