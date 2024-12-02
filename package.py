import pygame
import random
class Package:
    def __init__(self,WINDOW, x, y):
        self.id = random.randint(0,1000)
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.speed = 4
        self.direction = 1
        self.color = (0, 255, 255)
        self.WINDOW = WINDOW
    def getPicked(self,actor):
        if actor.grabbing and len(actor.holding) == 0:
            distance = ((actor.x - self.x)**2 + (actor.y - self.y)**2)**0.5
            if distance < 20:
                self.x = actor.x
                self.y = actor.y
                actor.holding.append(self.id)
        elif self.id in actor.holding:
            self.x = actor.x
            self.y = actor.y
            
            
        
            
    def draw(self):
        pygame.draw.rect(self.WINDOW, self.color, (self.x, self.y, self.width, self.height))
    def check_collision(self, dot_pos):
        distance = ((dot_pos[0] - self.x)**2 + (dot_pos[1] - self.y)**2)**0.5
        if distance < 10:
            return True
        return False