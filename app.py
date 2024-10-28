import sys
import pygame

from bullets.bullet import Bullet
from player.ship import Ship
from setting import Setting


class Alien:
    def __init__(self):
        pygame.init()

        self.setting = Setting()

        pygame.display.set_caption(self.setting.title)
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.setting.screen_width = self.screen.get_rect().width
        self.setting.screen_height = self.screen.get_rect().height

        self.bg_color = self.setting.bg_color

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()



    def run(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._remove_old_bullet()
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
        self._draw_bullets()
        pygame.display.flip()

    def _check_key_down_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.ship_moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.ship_moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullts()

    def _check_uo_down_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.ship_moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.ship_moving_left = False

    @staticmethod
    def _quit():
        pygame.quit()
        sys.exit()

    def _fire_bullts(self):
        if len(self.bullets) < self.setting.bullet_allow:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _remove_old_bullet(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _draw_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

