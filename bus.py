import pygame


class Bus(pygame.sprite.Sprite):
    IMAGE = pygame.image.load('resources/New Piskel (1).png')


    STARTING_POSITION = (300, 250)
    SIZE = (30, 15)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 2

    def __init__(self, starting_position: tuple, direction: str):
        super().__init__()
        self.image = Bus.IMAGE
        self.rect = pygame.Rect((0, 0), Bus.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        self.rect.centerx -= Bus.MOVE_DIST
        if self.rect.right <= 0:
            self.rect.centerx = Bus.SCREEN_DIM[0] + (Bus.SIZE[0] / 2)

