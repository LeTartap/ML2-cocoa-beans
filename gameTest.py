import pygame, sys, random
import gym
from pygame.locals import *

from models.actor import Actor
from models.item import Item
from models.package import Package
from models.zone import Zone
from models.environment import Environment


# -------------------------------------------------------------------------------- #
# Pygame setup
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)
DOT_COLOR = (0, 0, 255)

# Game Setup
FPS = 120
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# get the height and width of the window
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

font = pygame.font.SysFont("Arial", 24)
pygame.display.set_caption("ML2 - testing environment")

# -------------------------------------------------------------------------------- #
# Game Objects
packages = [Package(WINDOW, 100, 100),Package(WINDOW, 200, 200)]
actors = [Actor(WINDOW, 0, 0)]
items = [Item(WINDOW, 150, 150)]
zones = [Zone(WINDOW, WINDOW_WIDTH - 40, 0, 100, WINDOW_HEIGHT, True)]

ENVIRONMENT = Environment(WINDOW,actors, packages, items, zones)

# -------------------------------------------------------------------------------- #
# The main function that controls the game
def main():
    looping = True

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        ENVIRONMENT.moveItems()
        ENVIRONMENT.moveActors()
        ENVIRONMENT.movePackages()
        ENVIRONMENT.checkDeliveries()
        ENVIRONMENT.checkCollisions()
 
        # Render elements of the game
        WINDOW.fill(BACKGROUND)

        for zone in ENVIRONMENT.zones:
            zone.draw()
        for item in ENVIRONMENT.items:
            item.draw()
        for actor in ENVIRONMENT.actors:
            actor.draw()
        for package in ENVIRONMENT.packages:
            package.draw()

        legend_lines = []
        for idx, actor in enumerate(ENVIRONMENT.actors):
            legend_lines.append(f"Actor {idx+1}: {actor.points} points")
        legend_text = "\n".join(legend_lines)
        legend_surface = font.render(legend_text, True, (0, 0, 0))
        WINDOW.blit(legend_surface, (10, 10))

        pygame.display.update()
        fpsClock.tick(FPS)


main()
