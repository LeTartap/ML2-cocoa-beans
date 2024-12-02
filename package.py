import pygame
class Package:
    def __init__(self,WINDOW, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 4
        self.direction = 1
        self.color = (255, 0, 0)
        self.WINDOW = WINDOW
    def getPicked(self,actor):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            distance = ((actor.x - self.x)**2 + (actor.y - self.y)**2)**0.5
            if distance < 20:
                self.x = actor.x
                self.y = actor.y
            
    def draw(self):
        pygame.draw.rect(self.WINDOW, self.color, (self.x, self.y, self.width, self.height), 1)
    def check_collision(self, dot_pos):
        distance = ((dot_pos[0] - self.x)**2 + (dot_pos[1] - self.y)**2)**0.5
        if distance < 10:
            return True
        return False