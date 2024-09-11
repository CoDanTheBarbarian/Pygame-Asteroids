from constants import *
from circleshape import CircleShape
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v_1 = self.velocity.rotate(angle)
        v_2 = self.velocity.rotate(0 - angle)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_1 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, split_radius)
        asteroid_1.velocity = v_1 * 1.2
        asteroid_2.velocity = v_2 * 1.2
