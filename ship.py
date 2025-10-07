import pygame

class Ship:
    """Class to manage ship"""
    def __init__(self, ai_game):
        """starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship and get its rect
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Start ship at bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.x +=3
        if self.moving_left:
            self.rect.x -=3
    def blitme(self):
        #draw a ship at current location
        self.screen.blit(self.image, self.rect)

