class Settings():
    """ Store all settings for Alien Invasion game """

    def __init__(self):
        # screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (54, 59, 63)
        
        #ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5    # to encourage player to shoot correctly

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10  # controil how quickly the fleet drops down
        # fleet_direction of 1 means right, -1 means left
        self.fleet_direction = 0.5

        # how quickly the game speeds up
        self.speedup_scale = 1.2
        # how quickly alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize setting that change throughout the game + increase these speeds """
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1    # aliens always move right at the beginning of the game
        self.alien_points = 50

    def increase_speed(self):
        """ increase these speeds """       
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)



        