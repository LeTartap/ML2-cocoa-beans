import pygame, sys, random
import gym
from pygame.locals import *
from actor import Actor
from item import Item
from package import Package
from zone import Zone
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
DOT_COLOR = (0, 0, 255)
 
# Game Setup
FPS = 120
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 


WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
#get the hegiht and width of the window
pygame.display.set_caption('My Game!')



    
item1 = Item(WINDOW,150,150)
actor1 = Actor(WINDOW,0,0)
pkg1 = Package(WINDOW,200,200)
pkg2 = Package(WINDOW,100,100)
pkgs = [pkg1,pkg2]
objs = [item1,actor1,pkg1,pkg2]
winZone = Zone(WINDOW, WINDOW_WIDTH - 40, 0, 100, WINDOW_HEIGHT, True)
#check collision
def check_collision(obj1,obj2):
    distance = ((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)**0.5
    if distance < 10: 
        print("Collision")
        return True
    return False

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
    pkg1.getPicked(actor1)
    pkg2.getPicked(actor1)
    for pkg in pkgs:
        winZone.checkInside(pkg)

    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    check_collision(actor1,item1)
    for obj in objs:
        obj.draw()
    winZone.draw()
  
    
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()
