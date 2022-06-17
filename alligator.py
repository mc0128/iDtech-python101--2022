import pygame
from log import Log


class Alligator(Log):
    IMAGE = pygame.image.load('resources/alligator.png')

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__(starting_position, direction)
        self.image = Alligator.IMAGE if self.direction == 'Left' else pygame.transform.flip(Alligator.IMAGE, True,
                                                                                            False)

