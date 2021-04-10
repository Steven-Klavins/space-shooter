# Import pygame libraries
import pygame
import sys

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))

# Update method sets spaceship rect center to match mouse pos    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        self.screen_constrain()

# Create constraints left and right based on rect pos   
    def screen_constrain(self):
        if self.rect.right >= 1280:
            self.rect.right = 1280 
        if self.rect.left <= 0:
            self.rect.left = 0  
        
class Meteor(pygame.sprite.Sprite):
    def __init__(self, path, x_pos, y_pos, x_speed, y_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (x_pos, y_pos))
        
# Initialize pygame at 720P
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

# Create spaceship from spaceship class
spaceship = SpaceShip('spaceship.png', 640, 500, 10)


meteor1 = Meteor('Meteor1.png', 200, 405, 10, 10 )
meteor2 = Meteor('Meteor2.png', 700, 25, 10, 10 )
meteor3 = Meteor('Meteor3.png', 400, 205, 10, 10 )

# Add spaceship to a single group
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

meteor_group = pygame.sprite.Group()
meteor_group.add(meteor1)
meteor_group.add(meteor2)
meteor_group.add(meteor3)
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
    
    meteor_group.draw(screen)
    
    # Use update method to move spaceship
    spaceship_group.update()    
    
    pygame.display.update()
    # Set frame rate
    clock.tick(120)