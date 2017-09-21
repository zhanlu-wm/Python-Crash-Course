import pygame
from pygame.sprite import Group
from chapter_12.section_8_3.settings import Settings
from chapter_12.section_8_3.ship import Ship
import chapter_12.section_8_3.game_functions as gf


def run_game():

    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:

        gf.check_events(ship)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship)



run_game()