import pygame

class Platform():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def touch(self, x, y):
        if (self.x <= x <= self.x + self.width
            and self.y <= y <= self.y + self.height):
            return self.y
        return None

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
