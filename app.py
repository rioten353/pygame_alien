import sys
import pygame

from player.ship import Ship
from setting import Setting


class Alien:
    def __init__(self):
        pygame.init()

        self.setting = Setting()

        pygame.display.set_caption(self.setting.title)
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        self.bg_color = self.setting.bg_color

        self.ship = Ship(self)



    def run(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_event(event)
            elif event.type == pygame.KEYUP:
                self._check_uo_down_event(event)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blit()
        pygame.display.flip()

    def _check_key_down_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.ship_moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.ship_moving_left = True

    def _check_uo_down_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.ship_moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.ship_moving_left = False

    def _quit(self):
        pygame.quit()
        sys.exit()

