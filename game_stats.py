class GameStats():
    """ Track statistics """
    def __init__(self,my_settings):
        self.my_settings = my_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0
        self.level = 1
    def reset_stats(self):
        """ Initialize statistics that can change during the game """
        self.ship_left = self.my_settings.ship_limit
        self.score = 0  # reset the score each time new game starts