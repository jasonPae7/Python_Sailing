import sys

import pygame
from settings import Settings
from ship import Ship

class AlienInvation:
    #管理游戏
    def __init__(self):
        #初始化
        pygame.init()
        pygame.display.set_caption("Alien Invation")

        self.settings   =   Settings()
        self.screen     =   pygame.display.set_mode((self.settings.screen_width,
                                                      self.settings.screen_height))

        # self.screen     =   pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width  =   self.screen.get_rect().width
        # self.settings.screen_height =   self.screen.get_rect().height

        self.clock      =   pygame.time.Clock()
        self.ship       =   Ship(self)

    def run_game(self):
        #运行游戏
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==  pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type ==  pygame.KEYUP:
                self._check_keyup_evnets(event)

    def _check_keydown_events(self,event):
        if event.key    ==   pygame.K_RIGHT:
            self.ship.moving_right  =   True
        elif event.key  ==   pygame.K_LEFT:
            self.ship.moving_left   =   True
        elif event.key  ==   pygame.K_q:
            sys.exit()

    def _check_keyup_evnets(self,event):
        if event.key    ==  pygame.K_RIGHT:
            self.ship.moving_right  =   False
        elif event.key  ==  pygame.K_LEFT:
            self.ship.moving_left   =   False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvation()
    ai.run_game()

