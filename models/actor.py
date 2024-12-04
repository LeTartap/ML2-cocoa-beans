import pygame

class Actor:
    def __init__(self,WINDOW, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 1
        self.direction = 1
        self.color = (0, 0, 0)
        self.WINDOW = WINDOW
        self.holding = []
        self.grabbing = False
        self.points = 0
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.grabbing = True
        else:
            self.grabbing = False
            self.holding = []
        if keys[pygame.K_LEFT] and self.x - self.speed >= 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.width + self.speed <= self.WINDOW.get_width():
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.speed >= 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + self.height + self.speed <= self.WINDOW.get_height():
            self.y += self.speed

    def draw(self):
        pygame.draw.ellipse(self.WINDOW, self.color, (self.x, self.y, self.width, self.height))

    