import sys

import pygame

from settings import Settings

class AlienInvasion:

    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        #set background color
        self.bg_color = (230,230,230)

    def run_game(self):

        while True:
        # Watch for keyboard and mouse events.
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
# Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
