import pygame


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
