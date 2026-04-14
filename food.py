import pygame
import random
from settings import WIDTH, HEIGHT, BLOCK_SIZE, RED

class Food:
    def __init__(self):
        self.position = self.spawn()

    def spawn(self):
        return [
            random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)
        ]

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))