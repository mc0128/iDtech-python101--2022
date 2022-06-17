import pygame


class Berry(pygame.sprite.Sprite):
    IMAGE = pygame.image.load('resources/berry.png')
    SIZE = (20, 10)
    SCREEN_DIM = 600, 500

    def __init__(self, position: tuple):
        super().__init__()
        self.image = Berry.IMAGE
        self.rect = pygame.Rect((0, 0), Berry.SIZE)
        self.rect.center = position
