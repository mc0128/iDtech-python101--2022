import pygame
from log import Log


class Bird(pygame.sprite.Sprite):
    IMAGE = pygame.image.load('resources/New Piskel.png')
    STARTING_POSITION = (300, 490)
    SIZE = (20, 10)
    SCREEN_DIM = 600, 500
    move_dist = 10

    def __init__(self):
        super().__init__()
        self.image = Bird.IMAGE

        self.rect = pygame.Rect((0, 0), Bird.SIZE)
        self.rect.center = Bird.STARTING_POSITION
        self.lives = 3

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Bird.move_dist

    def move_down(self):
        if self.rect.bottom <= Bird.SCREEN_DIM[1] - 20:
            self.rect.centery += Bird.move_dist

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Bird.move_dist

    def move_right(self):
        if self.rect.right <= Bird.SCREEN_DIM[0] - 20:
            self.rect.centerx += Bird.move_dist

    def reset_position(self):
        self.rect.center = Bird.STARTING_POSITION
        self.lives -= 1

    def move_on_log(self, log: Log):
        # Log moving right
        if log.direction == 'Right':
            self.rect.centerx += Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.left >= Log.SCREEN_DIM[0]:
                diff = log.rect.right - self.rect.centerx
                self.rect.centerx = -diff
        # Log moving left
        else:
            self.rect.centerx -= Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.right <= 0:
                diff = abs(log.rect.left - self.rect.centerx)
                self.rect.centerx = Bird.SCREEN_DIM[0] + diff



