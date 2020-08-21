import pygame

class Hero():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity_x = 0
        self.velocity_y = 0
        self.touching = False

    def jump(self):
        if self.touching:
            self.velocity_y = -15

    def left(self):
        self.velocity_x = -5

    def right(self):
        self.velocity_x = 5

    def stop(self):
        self.velocity_x = 0

    def update_position(self, platforms):
        self.x += self.velocity_x
        if self.velocity_y >= 0:
            for platform in platforms:
                platform_y = platform.touch(self.x, self.y)
                if platform_y:
                    self.velocity_y = 0
                    self.y = platform_y
                    self.touching = True
                    return

        self.y += self.velocity_y
        self.velocity_y += 1
        self.touching = False

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y - self.radius), self.radius)
