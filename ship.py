
import pygame
from settings import Settings
from pygame.sprite import Sprite
PATH_TO_SHIP_IMAGE = 'C:\\Users\\Microsoft Windows\\Desktop\\VS Programming\\python vs\\pyCrashCourse\\alienInvasion\\images\\resize_nhim.bmp'


class Ship(Sprite):

    def __init__(self,my_settings,screen):
        super().__init__()
        """ Initialize the ship and set starting position """
        self.screen = screen
        self.my_settings = my_settings
        # load the ship image and get its rect
            # load the image
        self.image = pygame.image.load(PATH_TO_SHIP_IMAGE) 
        #self.resize_image = pygame.transform.scale(self.image,(64,64))
            # treat the image + the screeN as an rectangle (an advantage of pygame)
        self.rect = self.image.get_rect()   
        self.screen_rect = screen.get_rect()

        # start each new ship at the middle of the screen
        self.rect.centerx = self.screen_rect.centerx # center at the x axis (horizontally)
        self.rect.bottom = self.screen_rect.bottom
        #self.rect.centery = self.screen_rect.centery  # to work with edges of the window + move vertically
        self.horizon_center = float(self.rect.centerx)
        #self.vertical_center = float(self.rect.centery)
        #movement flag
        self.moving_right = False  
        self.moving_left = False
        '''
        self.moving_up = False
        self.moving_down = False
        '''

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.horizon_center += self.my_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.horizon_center -= self.my_settings.ship_speed_factor
        '''
        if self.moving_up and self.rect.top > 0:
            self.vertical_center -= self.my_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.vertical_center += self.my_settings.ship_speed_factor
        '''
        # update rect object from self.center
        self.rect.centerx = self.horizon_center # only the integer portion of center is stored in rect.centerx
        #self.rect.centery = self.vertical_center # only the integer portion of center is stored in rect.centerx
   
    def blitMe(self):
        """ Draw the ship at the current location """
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx