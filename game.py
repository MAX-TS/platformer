import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("platformer 1.0")


bg = pygame.image.load('images/pygame_bg.jpg')

clock = pygame.time.Clock()

class Hero():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity_x = 0
        self.velocity_y = 0

    def jump(self):
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
                    return

        self.y += self.velocity_y
        self.velocity_y += 1


    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y - self.radius), self.radius)


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


def drawWindow():
    win.blit(bg, (0, 0))

    hero.update_position(platforms)
    hero.draw(win)

    hero2.update_position(platforms)
    hero2.draw(win)

    for platform in platforms:
        platform.draw(win)

    pygame.display.update()


run = True
hero = Hero(50, 424, 10, (0, 0, 255), 1)
hero2 = Hero(100, 424, 10, (0, 255, 0), 1)
platforms = [

    Platform(0, 450, 200, 20, (255, 0, 0)),
    Platform(300, 450, 200, 20, (255, 0, 0)),

]

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hero.jump()
    if keys[pygame.K_SPACE]:
        hero2.jump()

    if keys[pygame.K_LEFT]:
        hero.left()
    elif keys[pygame.K_RIGHT]:
        hero.right()
    else:
        hero.stop()



    drawWindow()



pygame.quit()
