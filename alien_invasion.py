import sys, pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    # initialize game and create a screen object

    pygame.init()
    pygame.display.set_caption("Alien Invasion")
   
    # adjust the settings
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_width,my_settings.screen_height))    # represent the entire game window
    # Store game statistics
    stats = GameStats(my_settings)
    sb = ScoreBoard(my_settings, screen, stats)
    # import the ship class
    ship = Ship(my_settings,screen)
    bullets = Group()
    aliens = Group()    # a group to hold all aliens of the game
    # create a fleet of aliens
    gf.create_fleet(my_settings,screen,ship,aliens)
    # make the Play button
    play_button = Button(my_settings, screen, "Play")
    # start the main loop for the game

    while True:
        # watch for keyboard and mouse movement
        gf.check_events(my_settings, screen, stats,sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            # get rid of old bullet (bc their y-coordinate just grow increasingly negative)
            gf.update_bullets(aliens,my_settings, screen,stats,sb, ship,bullets )
            print(len(bullets))
            # redraw the screen with bg_color during each event in while loop      
            gf.update_aliens(my_settings,stats,screen,sb,ship,aliens,bullets)      
            gf.update_screen(my_settings, screen, stats, sb, ship, aliens, bullets, play_button)    # gain access to these groups
        
        # always paint the screen (even at the start of the game) because .update_screen in stats.game_active is not called when the game starts
        gf.update_screen(my_settings, screen, stats, sb, ship, aliens, bullets, play_button) 


run_game()
