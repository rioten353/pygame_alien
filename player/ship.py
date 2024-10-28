import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.setting = ai_game.setting
        self.screen_rect = ai_game.screen.get_rect()

        self.ship_image = pygame.image.load('images/player.gif')
        self.ship_image_rect = self.ship_image.get_rect()

        self.ship_image_rect.midbottom = self.screen_rect.midbottom

        self.ship_moving_right = False
        self.ship_moving_left = False

        self.x = float(self.ship_image_rect.x)

    def update(self):
        if self.ship_moving_right and self.screen_rect.right > self.ship_image_rect.right:
            self.x += self.setting.ship_speed

        if self.ship_moving_left and self.screen_rect.left < self.ship_image_rect.left:
            self.x -= self.setting.ship_speed

        self.ship_image_rect.x = self.x

    def blit(self):
        self.screen.blit(self.ship_image, self.ship_image_rect)
