'''
Created on 2017年3月21日

@author: pengchengzhang
'''
import sys

import pygame

from ship import Ship

from settings import Settings

def check_events():
    #监视键盘和鼠标
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
def update_screen(ai_settings,screen,ship):
    """更新屏幕上的图像，并切换到新屏幕"""
     #每次循环时都会重画屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
            
        #让最近绘制的屏幕可见
    pygame.display.flip()
