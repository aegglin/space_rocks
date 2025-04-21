# space_rocks/game.py
import pygame
from utils import load_sprite

class SpaceRocks:
    def __init__(self):
        # Initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption('Space Rocks')

        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False) # background doens't need alpha channel

    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()
    
    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()
