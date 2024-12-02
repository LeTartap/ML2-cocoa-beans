import pygame
class Item:
    def __init__(self,WINDOW, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 4
        self.direction = 1
        self.color = (255, 0, 0)
        self.WINDOW = WINDOW
    def move(self):
        self.y += self.speed * self.direction
        if self.y < 0 or self.y + self.height >self.WINDOW.get_height():
            self.direction = -self.direction
    def draw(self):
        pygame.draw.rect(self.WINDOW, self.color, (self.x, self.y, self.width, self.height))
    