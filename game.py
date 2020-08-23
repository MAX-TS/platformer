import pygame

from hero import Hero
from platform import Platform

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("platformer 1.0")


bg = pygame.image.load('images/pygame_bg.jpg')

clock = pygame.time.Clock()


def drawWindow():
    win.blit(bg, (0, 0))

    if game_over:
        font = pygame.font.SysFont('comicsansms', 72, bold=True)
        text = font.render("GAME OVER!", 1, (0, 0, 0))
        place = text.get_rect(center=(250, 250))
        win.blit(text, place)
        font = pygame.font.SysFont('comicsansms', 36, bold=False)
        text = font.render("Press SPACE to reset.", 1, (0, 0, 0))
        place = text.get_rect(center=(250, 300))
        win.blit(text, place)
    else:
        for hero in heroes:
            hero.update_position(platforms)
            hero.draw(win)

        for platform in platforms:
            platform.draw(win)

    pygame.display.update()


run = True
game_over = False


def create_heroes():
    return [
        Hero(
            x=50, y=424, radius=10,
            color=(0, 0, 255),
            key_up=pygame.K_UP,
            key_left=pygame.K_LEFT,
            key_right=pygame.K_RIGHT
        ),
        Hero(
            x=100, y=424,radius=10,
            color=(0, 255, 0),
            key_up=pygame.K_w,
            key_left=pygame.K_a,
            key_right=pygame.K_d
        ),
        Hero(
            x=150, y=424, radius=10,
            color=(255, 255, 0),
            key_up=pygame.K_i,
            key_left=pygame.K_j,
            key_right=pygame.K_l
        )
    ]


platforms = [

    Platform(0, 450, 200, 20, (255, 0, 0)),
    Platform(300, 450, 200, 20, (255, 0, 0)),

]

heroes = create_heroes()

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    for hero in heroes:
        hero.control(keys)
        if hero.y > 499:
            game_over = True

    if keys[pygame.K_SPACE] and game_over:
        game_over = False
        heroes = create_heroes()

    drawWindow()


pygame.quit()
