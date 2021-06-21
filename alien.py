import pygame
from pygame.sprite import Sprite


PATH_TO_ALIEN_IMAGE = 'C:\\Users\\Microsoft Windows\\Desktop\\VS Programming\\python vs\\pyCrashCourse\\alienInvasion\\images\\badger_resize.bmp'

class Alien(Sprite):
    """ Present a single alien """

    def __init__(self,my_settings,screen):
        ""' Initialize the alien and its starting position '"" 
        super().__init__()
        self.screen = screen
        self.my_settings = my_settings

        # Load alien image + rect attribute
        self.image = pygame.image.load(PATH_TO_ALIEN_IMAGE)
        #self.resize_image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()    
        # alien starts at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact postion
        self.x = float(self.rect.x)

    def blitMe(self):
        """ Draw alien at the current position """
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """ Return true if aliens are at edges of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move the alien right """
        self.x  += (self.my_settings.alien_speed_factor * self.my_settings.fleet_direction)
        self.rect.x = self.x



