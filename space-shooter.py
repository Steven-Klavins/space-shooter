# Import pygame libraries
import pygame
import sys

# Initialize pygame at 720P
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

# Start game loop
while True:
    for event in pygame.event.get():
        # Allow player to quit and close window
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
            
    pygame.display.update()
    # Set frame rate
    clock.tick(120)