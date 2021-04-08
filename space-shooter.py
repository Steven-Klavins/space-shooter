# Import pygame libraries
import pygame
import sys

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

# Initialize pygame at 720P
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

# Create spaceship from spaceship class
spaceship = SpaceShip('spaceship.png', 640, 500, 10)

# Add spaceship to a single group
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

# Start game loop
while True:
    for event in pygame.event.get():
        # Allow player to quit and close window
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
            
    # Set background colour      
    screen.fill((42,45,51))  
    
    # Render spacship
    spaceship_group.draw(screen)     
          
    pygame.display.update()
    # Set frame rate
    clock.tick(120)