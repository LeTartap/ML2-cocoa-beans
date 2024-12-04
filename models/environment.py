import pygame
import sys, random

sys.path.append("../")
from utils.utils import getDistance
from models.package import Package


class Environment:
    def __init__(self, WINDOW, actors, packages, items, zones):
        self.actors = []
        self.packages = []
        self.items = []
        self.zones = []

        self.WINDOW = WINDOW
        self.actors = actors
        self.packages = packages
        self.items = items
        self.zones = zones

    def moveItems(self):
        for item in self.items:
            item.move()

    def moveActors(self):
        for actor in self.actors:
            actor.movement()

    def movePackages(self):
        for package in self.packages:
            for actor in self.actors:
                package.getPicked(actor)

    def checkDeliveries(self):
        for actor in self.actors:
            for package_id in actor.holding:
                package = [p for p in self.packages if p.id == package_id][0]
                for zone in self.zones:
                    if zone.checkInside(package):
                        package.deliver(actor)
                        self.packages.remove(package)
                        del package

    def checkCollisions(self):
        # TODO collions for other objects
        for actor in self.actors:
            for item in self.items:
                if getDistance(actor, item) < 10:
                    actor.points -= 1

    def spawnPackage(self):
        valid_centroid = False

        while valid_centroid == False:
            central_x = random.randint(50, self.WINDOW.get_width() - 50)  
            central_y = random.randint(50, self.WINDOW.get_height() - 50)
            
            package = Package(self.WINDOW, central_x, central_y)
            for zone in self.zones:
                if getDistance(zone, package) > 100:
                   valid_centroid = True
                                    

        

        for _ in range(random.randint(1, 5)):
            spawned = False
            while not spawned:
                x = random.randint(max(0, central_x - 20), min(self.WINDOW.get_width(), central_x + 20))
                y = random.randint(max(0, central_y - 20), min(self.WINDOW.get_height(), central_y + 20))

                package = Package(self.WINDOW, x, y)

                # Check if the package is far enough from delivery zones
                for zone in self.zones:
                    if getDistance(zone, package) > 50:
                        spawned = True
                        self.packages.append(package)

