import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化
    pygame.init()
    th_settings = Settings()
    screen = pygame.display.set_mode(th_settings.screen_resolution)
    pygame.display.set_caption('Nice8')

    ship = Ship(th_settings,screen)

    # 游戏主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(th_settings, screen, ship)

        
run_game()
