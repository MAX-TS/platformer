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
        hero.update_position(platforms)
        hero.draw(win)

        hero2.update_position(platforms)
        hero2.draw(win)

        for platform in platforms:
            platform.draw(win)

    pygame.display.update()


run = True
game_over = False

def reset_game():
    global hero, hero2
    hero = Hero(50, 424, 10, (0, 0, 255), 1)
    hero2 = Hero(100, 424, 10, (0, 255, 0), 1)

platforms = [

    Platform(0, 450, 200, 20, (255, 0, 0)),
    Platform(300, 450, 200, 20, (255, 0, 0)),

]

reset_game()

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # control hero
    if keys[pygame.K_UP]:
        hero.jump()

    if keys[pygame.K_LEFT]:
        hero.left()
    elif keys[pygame.K_RIGHT]:
        hero.right()
    else:
        hero.stop()

    # control hero2
    if keys[pygame.K_w]:
        hero2.jump()

    if keys[pygame.K_a]:
        hero2.left()
    elif keys[pygame.K_d]:
        hero2.right()
    else:
        hero2.stop()

    if hero.y > 499 or hero2.y > 499:
        game_over = True

    if keys[pygame.K_SPACE] and game_over:
        game_over = False
        reset_game()

    drawWindow()



pygame.quit()
