import pygame, sys, random
import gym
from pygame.locals import *
from actor import Actor


pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
DOT_COLOR = (0, 0, 255)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')


class item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 4
        self.direction = 1
        self.color = (255, 0, 0)
    def move(self):
        self.y += self.speed * self.direction
        if self.y < 0 or self.y + self.height > WINDOW_HEIGHT:
            self.direction = -self.direction
    def draw(self):
        pygame.draw.rect(WINDOW, self.color, (self.x, self.y, self.width, self.height), 1)
    def check_collision(self, dot_pos):
        distance = ((dot_pos[0] - self.x)**2 + (dot_pos[1] - self.y)**2)**0.5
        if distance < 10:
            return True
        return False
    
item1 = item(150,150)
actor1 = Actor(0,0)

#check collision
def check_collision(rect_pos, dot_pos):
    distance = ((dot_pos[0] - rect_pos[0])**2 + (dot_pos[1] - rect_pos[1])**2)**0.5
    if distance < 10:
        return True
    return

dot_pos = [WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2]
rect_pos = [0, 0]
rec_speed = [0, 1]

dot_speed = [2, 2]
dot_radius = 10
# The main function that controls the game
def main () :
  looping = True
  
  # The main game loop
  while looping :
    # Get inputs
    for event in pygame.event.get() :
      if event.type == QUIT :
        pygame.quit()
        sys.exit()

    #draw the item
    item1.move()
    actor1.movement()
    
    
    if item1.check_collision(dot_pos):
        print("Collision")

    

      
      
      
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    item1.draw()
    actor1.draw(WINDOW)
    
   
  
    
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()
