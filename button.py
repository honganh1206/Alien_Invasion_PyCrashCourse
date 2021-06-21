import pygame.font

class Button():
    def __init__(self,my_settings,screen,msg):
        """ initialize button attributes """
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # set dimensions + properties of buttons
        self.width, self.height = 200, 50
        self.button_color = (163, 214, 212)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,40)
        
        # build button's rect
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # the button msg needs to be prepped only once
        self.prep_msg(msg)  # pygame works with text by rendering the string you want to display as an image

    def prep_msg(self,msg):
        """ Turn msg to a rendered image + center on the button """
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)   # true for antialiasing (make the edges of the text smoother)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
