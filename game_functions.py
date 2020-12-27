import pygame
import sys


def check_keydown_events(event, ship):
    if event.key == pygame.K_LSHIFT:
        ship.shift = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True


def check_keyup_event(event, ship):
    if event.key == pygame.K_LSHIFT:
        ship.shift = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ship):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(th_settings, screen, ship):

    # 帧处理
    screen.fill(th_settings.bg_color)
    ship.blitme()

    # 帧显示
    pygame.display.flip()
