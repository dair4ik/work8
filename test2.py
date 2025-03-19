import pygame
import sys
from pygame.locals import *
from tkinter import Tk, colorchooser

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Create a surface to store drawings
drawing_surface = pygame.Surface((WIDTH, HEIGHT))
drawing_surface.fill(WHITE)

# Variables
color = BLACK
tool = "brush"
drawing = False
start_pos = None
brush_size = 5

# Function to choose color
def choose_color():
    global color
    Tk().withdraw()  # Hide the root window
    color = colorchooser.askcolor()[0]
    if color:
        color = tuple(map(int, color))

# Main loop
running = True
while running:
    screen.blit(drawing_surface, (0, 0))  # Keep previous drawings
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
        elif event.type == MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos
            if tool == "rectangle":
                rect = pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                pygame.draw.rect(drawing_surface, color, rect, 2)
            elif tool == "circle":
                radius = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])) // 2
                center = (start_pos[0] + (end_pos[0] - start_pos[0]) // 2, start_pos[1] + (end_pos[1] - start_pos[1]) // 2)
                pygame.draw.circle(drawing_surface, color, center, radius, 2)
        elif event.type == MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(drawing_surface, color, event.pos, brush_size)
            elif tool == "eraser":
                pygame.draw.circle(drawing_surface, WHITE, event.pos, brush_size + 5)
        elif event.type == KEYDOWN:
            if event.key == K_m:
                tool = "brush"
                print("Tool changed to: Brush")
            elif event.key == K_n:
                tool = "rectangle"
                print("Tool changed to: Rectangle")
            elif event.key == K_c:
                tool = "circle"
                print("Tool changed to: Circle")
            elif event.key == K_e:
                tool = "eraser"
                print("Tool changed to: Eraser")
            elif event.key == K_p:
                choose_color()
                print(f"Color changed to: {color}")
            elif event.key == K_r:
                color = RED
                print("Color changed to: Red")
            elif event.key == K_g:
                color = GREEN
                print("Color changed to: Green")
            elif event.key == K_b:
                color = BLUE
                print("Color changed to: Blue")
            elif event.key == K_l:
                brush_size += 2
                print(f"Brush size increased to: {brush_size}")
            elif event.key == K_w and not pygame.key.get_mods() & KMOD_CTRL:
                brush_size = max(1, brush_size - 2)
                print(f"Brush size decreased to: {brush_size}")
            elif event.key == K_w and pygame.key.get_mods() & KMOD_CTRL:
                running = False
            elif event.key == K_F4 and pygame.key.get_mods() & KMOD_ALT:
                running = False
    
    pygame.display.flip()

pygame.quit()
sys.exit()
