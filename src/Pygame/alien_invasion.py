'''
Created on 2017年3月21日

@author: pengchengzhang
'''

import pygame

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    Screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    
    screen = pygame.display.set_mode((1200,800))
    ship = Ship(ai_settings,screen)
    
    #设置背景色

    bg_color= (230,230,230)
    
    
    #开始游戏的主循环
    while True:
        #调用gf中的函数
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
       
        
run_game()