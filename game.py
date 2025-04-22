# space_rocks/game.py
import pygame
from utils import load_sprite
from models import GameObject

class SpaceRocks:
    def __init__(self):
        # Initialize pygame and set the title
        pygame.init()
        pygame.display.set_caption('Space Rocks')
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False) # background doens't need alpha channel

        sprite = load_sprite("spaceship")
        self.ship = GameObject((400, 300), sprite, (0, 0))

        sprite = load_sprite("asteroid")
        self.rock = GameObject((50, 300), sprite, (1, 0))

        self.collision_count = 0

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
        self.ship.move()
        self.rock.move()

    def _draw(self):
        # Draw the background and then the ship/rocls
        self.screen.blit(self.background, (0, 0))
        self.ship.draw(self.screen)
        self.rock.draw(self.screen)
        pygame.display.flip()

        if self.ship.collides_with(self.rock):
            self.collision_count += 1
            print(f"Collision #{self.collision_count}")

        self.clock.tick(30)
