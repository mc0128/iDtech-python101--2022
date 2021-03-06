import pygame
import random
from log import Log
from alligator import Alligator


class River:
    SIZE = (600, 30)
    SCREEN_DIM = 600, 500

    def __init__(self, river_height: int, direction: str, number_of_logs: int, number_of_alligators: int):
        self.rect = pygame.Rect((0, river_height), River.SIZE)
        self.logs = []
        self.alligators = []
        self.add_logs(direction, number_of_logs, river_height + 15, number_of_alligators)

    def add_logs(self, direction: str, number_of_logs: int, river_height: int, number_of_alligators: int):
        dp = []
        for _ in range(number_of_logs):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.logs.append(Log((x_pos, river_height), direction))


