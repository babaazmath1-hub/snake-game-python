import pygame
from settings import BLOCK_SIZE, GREEN

class Snake:
    def __init__(self):
        self.body = [[100, 100], [80, 100], [60, 100]]
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        head = self.body[0].copy()

        if self.direction == "UP":
            head[1] -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head[1] += BLOCK_SIZE
        elif self.direction == "LEFT":
            head[0] -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head[0] += BLOCK_SIZE

        self.body.insert(0, head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for i, segment in enumerate(self.body):
            color = (0, 255 - i*5, 100 + i*3)
            pygame.draw.rect(screen, color, (*segment, BLOCK_SIZE, BLOCK_SIZE))

    def check_collision(self, width, height):
        head = self.body[0]
        return (
            head[0] < 0 or head[0] >= width or
            head[1] < 0 or head[1] >= height or
            head in self.body[1:]
        )