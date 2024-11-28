import pygame, sys, random
import gym
from pygame.locals import *
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
    
    # Processing
    # This section will be built out later
    dot_pos[0] += dot_speed[0]
    dot_pos[1] += dot_speed[1]
    
    rect_pos[1] += rec_speed[1]
    

    # Bounce the rectangle off the edges
    
    if rect_pos[1] < 0 or rect_pos[1] + 20 > WINDOW_HEIGHT:
        rec_speed[1] = -rec_speed[1]

    # Bounce the dot off the edges
    if dot_pos[0] - dot_radius < 0 or dot_pos[0] + dot_radius > WINDOW_WIDTH:
        dot_speed[0] = -dot_speed[0]
    if dot_pos[1] - dot_radius < 0 or dot_pos[1] + dot_radius > WINDOW_HEIGHT:
        dot_speed[1] = -dot_speed[1]
 
    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    pygame.draw.circle(WINDOW, DOT_COLOR, dot_pos, dot_radius)
    pygame.draw.rect(WINDOW, (255, 0, 0), (rect_pos[0]+50, rect_pos[1], 20, 20), 1)
    pygame.draw.rect(WINDOW, (255, 0, 0), (rect_pos[0], rect_pos[1], 20, 20), 1)
    pygame.draw.rect(WINDOW, (255, 0, 0), (rect_pos[0]+150, rect_pos[1], 20, 20), 1)
    distance = ((dot_pos[0] - rect_pos[0])**2 + (dot_pos[1] - rect_pos[1])**2)**0.5
    #display distance in the corner
    font = pygame.font.Font(None, 36)
    text = font.render(str(int(distance)), 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = WINDOW.get_rect().centerx
    WINDOW.blit(text, textpos)
    #display distance in the corner
    
    pygame.display.update()
    fpsClock.tick(FPS)
 
main()
