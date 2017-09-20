import pygame
from chapter_12.section_5_2.settings import Settings
from chapter_12.section_5_2.ship import Ship
import chapter_12.section_5_2.game_functions as gf


def run_game():

    # 初始化pygame，设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏主循环
    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)



run_game()