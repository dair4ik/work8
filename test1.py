import pygame
import sys
from pygame.locals import *
from tkinter import Tk, colorchooser

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Create a surface to store drawings
drawing_surface = pygame.Surface((WIDTH, HEIGHT))
drawing_surface.fill(WHITE)

# Variables
color = BLACK
tool = "rectangle"
drawing = False
start_pos = None

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
        elif event.type == MOUSEMOTION and drawing:
            if tool == "eraser":
                pygame.draw.circle(drawing_surface, WHITE, event.pos, 20)
            elif tool == "rectangle":
                pygame.draw.rect(drawing_surface, color, (event.pos[0], event.pos[1], 20, 20))
            elif tool == "circle":
                pygame.draw.circle(drawing_surface, color, event.pos, 10)
        elif event.type == KEYDOWN:
            if event.key == K_r:
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
    
    pygame.display.flip()

pygame.quit()
sys.exit()