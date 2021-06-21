import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,my_settings,screen,ship):
        """ Create a bullet obj from the ship's position """
        super().__init__()
        self.screen = screen
        """ Create a bullet rect at (0,0) and then set correct position """
        self.rect = pygame.Rect(0, 0, my_settings.bullet_width, my_settings.bullet_height) # create bullet's rect attribute
        self.rect.centerx = ship.rect.centerx   # move the bullet accordingly with the ship
        #self.rect.centery = ship.rect.centery   # set bullet's center to be the same as the ship's rect.center
        self.rect.top = ship.rect.top           # set the top of the bullet's rect to match the top of the ship's rect

        # store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = my_settings.bullet_color
        self.speed_factor = my_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen """
        # update the decimal position
        self.y -= self.speed_factor
        # update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw the bullet on the screen """
        pygame.draw.rect(self.screen,self.color,self.rect) 