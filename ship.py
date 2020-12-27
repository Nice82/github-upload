import pygame


class Ship():

    def __init__(self,th_settings, screen):
        """自机"""
        self.screen = screen
        self.th_settings = th_settings

        # load image
        self.image = pygame.image.load(
            'C:/Users/MyPC/Desktop/New_project/Nice8/images/reimu.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 自机放置于版底中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.bottom

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.shift = False
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.shift:
            self.th_settings.ship_speed = self.th_settings.ship_speed_low
        else:
            self.th_settings.ship_speed = self.th_settings.ship_speed_high
        if self.moving_right:
            self.center_x += self.th_settings.ship_speed
        if self.moving_left:
            self.center_x -= self.th_settings.ship_speed
        if self.moving_up:
            self.center_y -= self.th_settings.ship_speed
        if self.moving_down:
            self.center_y += self.th_settings.ship_speed

        #123
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
