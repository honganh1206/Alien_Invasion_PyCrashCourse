import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():

    def __init__(self,my_settings,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.my_settings = my_settings
        self.stats = stats

        # font settings
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 40)

        #prepare the score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.my_settings.bg_color)

        # display the score at the top right corner
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 # 20 pixels from the right screen edge
        self.score_rect.top = 20

    def prep_high_score(self):
        """ Turn a highscore to a rendered image """
        high_score = int(round(self.stats.high_score, -1))  # round the highscore to be divisible by 10
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,self.my_settings.bg_color)
      
        # center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):

        self.level_image = self.font.render(str(self.stats.level), True, self.text_color,self.my_settings.bg_color)

        # display the score at the top right corner
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.score_rect.top = self.score_rect.bottom + 15

    def prep_ships(self):
        """ show how many ships are left """
        self.ships = Group() # because we are making a group of ships
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.my_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
        


    