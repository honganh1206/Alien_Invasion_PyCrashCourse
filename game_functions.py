import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


""" Events related """


def check_events(my_settings, screen, stats,sb, play_button, ship, aliens, bullets):
    """ respond to key presses and mouse event """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
        # respond if pygame detects a KEYDOWN (keys are entered) event
        elif event.type == pygame.KEYDOWN:  # buttons are pressed
            check_keydown_events(event,my_settings,screen,ship, bullets)
        elif event.type == pygame.KEYUP:    # buttons are released
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # start game when the player clicks anywhere on the screen
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(my_settings, screen, stats,sb, play_button,ship, aliens, bullets, mouse_x,mouse_y)

def check_play_button(my_settings, screen, stats,sb, play_button,ship, aliens, bullets, mouse_x,mouse_y):
    # see if the point of the mouse click overlaps the region defined by the Play buttons' rect
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:  
        # reset the game's Settings
        my_settings.initialize_dynamic_settings()
        # hide the mouse cursor
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # reset the sb
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet + center the ship
        create_fleet(my_settings, screen, ship, aliens)
        ship.center_ship()

def check_keyup_events(event,ship):
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    '''
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    '''
def check_keydown_events(event,my_settings,screen, ship, bullets):  
    if event.key == pygame.K_RIGHT:
        # move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(my_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    '''
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    '''                     
def check_high_scores(stats,sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

""" Bullets related """


def update_screen(my_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(my_settings.bg_color)
    # redraw bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()    
    
    ship.blitMe()   # draw the ship
    aliens.draw(screen)  # draw alien
        # make the recently drawn screen visible
    # draw play button if the game is inactive
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()   # when making an event, .flip() will update the screen to show new elem

def update_bullets(aliens,my_settings, screen,stats,sb, ship,bullets):
    """ Update the position of the bullet and get rid of the bullet """
    # Update bullet position
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) 

    check_bullet_alien_collision(my_settings, screen, stats,sb, ship, aliens, bullets)

def fire_bullet(my_settings,screen,ship,bullets):
    """ Firing bullet within limit"""
    # create a new bullet and add it to the bullet group, fire bullet with space bả
    if len(bullets) < my_settings.bullets_allowed:
        new_bullet = Bullet(my_settings,screen,ship)    # create a new bullet as Bullet instance
        bullets.add(new_bullet)                          # add to group bullet


    """ Aliens related"""


def check_bullet_alien_collision(my_settings,screen,stats,sb,ship,aliens,bullets):
    # check for collision between bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)   # True arguments tell Pygame to delete the bullets and aliens after collisions
    if collisions:
        for aliens in collisions.values():
            stats.score += my_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_scores(stats, sb)
    
    if len(aliens) == 0:
        # destroy existing bullets + create new fleets
        # if destroy the entire fleet => next level
        bullets.empty()
        my_settings.increase_speed()
        # increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(my_settings, screen, ship, aliens)


def create_fleet(my_settings,screen,ship,aliens):
    # create an alien and find the number of aliens in a row
    # spacing between aliens = one alien's width
    alien = Alien(my_settings,screen)   # create 1 alien for measurement only
    number_aliens_x = get_number_aliens_x(my_settings, alien.rect.width)
    number_rows = get_number_rows(my_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):   # count from 0 to the number of row we want
        for alien_number in range(number_aliens_x):
        # create an alien and put it in the first row
            create_alien(my_settings, screen, aliens, alien_number,row_number)

def get_number_aliens_x(my_settings,alien_width):
    """ Determine num of aliens that fit in a row """
    available_space_x = my_settings.screen_width - 2 * alien_width  # space for 1 row of alien
    number_aliens_x = int(available_space_x / (2 * alien_width))    # no partial row of aliens
    return number_aliens_x

def create_alien(my_settings,screen,aliens,alien_number,row_number):
    alien = Alien(my_settings,screen) 
    # create a row of alien  
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    # create a number of rows of aliens
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(my_settings,ship_height,alien_height):
    """ Determine the number of rows of aliens that fit on the screen """
    available_space_y = (my_settings.screen_height) - (3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def update_aliens(my_settings,stats,screen, sb, ship,aliens,bullets):
    """ check if fleet is at an edges, and then update positions of all aliens in the fleet """
    check_fleet_edges(my_settings, aliens)
    aliens.update()

    # look for collision

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(my_settings, stats, screen, sb, ship, aliens, bullets)
    # look for aliens at bottom
    check_aliens_bottom(my_settings, stats, screen,sb, ship, aliens, bullets)

def check_fleet_edges(my_settings,aliens):
    """ Respond if aliens hit edges """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(my_settings,aliens)
            break

def change_fleet_direction(my_settings,aliens):
    """ Drop the entire fleet + change the fleet's direction """
    for alien in aliens.sprites():
        alien.rect.y += my_settings.fleet_drop_speed
    my_settings.fleet_direction *= -1

def check_aliens_bottom(my_settings,stats,screen,sb,ship,aliens,bullets):
    """ check if any alien is at the bottom of the screen """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # the same as ship gets hit
            ship_hit(my_settings, stats, screen,sb, ship, aliens, bullets)
            break
""" Ship related """

def ship_hit(my_settings,stats,screen,ship,aliens,bullets):
    if stats.ship_left > 0:    
    
        # decrement ship left
        stats.ship_left -= 1

        #update scoreboard
        sb.prep_ships()

        # empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet + center the ship
        create_fleet(my_settings, screen, ship, aliens)
        ship.center_ship()

        #pause
        sleep(.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


