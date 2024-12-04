import pygame


class Zone:
    def __init__(self, WINDOW, x, y, sizex, sizey, winning):
        self.x = x
        self.y = y
        self.sizex = sizex
        self.sizey = sizey
        self.winning = winning
        if self.winning == True:
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 0)
        self.WINDOW = WINDOW

    def draw(self):
        pygame.draw.rect(
            self.WINDOW, self.color, (self.x, self.y, self.sizex, self.sizey)
        )

    def checkInside(self, package):
        return (
            self.winning
            and package.x > self.x
            and package.x < (self.x + self.sizex)
            and package.y > self.y
            and package.y < (self.y + self.sizey)
        )
