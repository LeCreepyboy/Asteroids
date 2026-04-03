from circleshape import *
from constants import *
from main import *
#import math
import pygame

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, rotation):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0) 
        self.rotation = rotation
        self.start_pos = pygame.Vector2(0, 0)
        self.tip_position = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        direction = pygame.Vector2(0, 1)
        self.start_pos = self.position + direction.rotate(self.rotation) * (PLAYER_SHOOT_LENGTH - 30)
        self.tip_position = self.position + direction.rotate(self.rotation) * PLAYER_SHOOT_LENGTH

    def draw(self, screen):
        pygame.draw.line(screen, "white", self.start_pos, self.tip_position, LINE_WIDTH)

