import pygame

class Actor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 1
        self.direction = 1
        self.color = (0, 0, 0)

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, window):
        pygame.draw.ellipse(window, self.color, (self.x, self.y, self.width, self.height))

    def check_collision(self, dot_pos):
        distance = ((dot_pos[0] - self.x)**2 + (dot_pos[1] - self.y)**2)**0.5
        if distance < 10:
            return True
        return False