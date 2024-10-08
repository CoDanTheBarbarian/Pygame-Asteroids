import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroid_field import *
from shot import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (updateable, drawable, shots)

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for j in updateable:
            j.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if shot.detect_collision(asteroid):
                    asteroid.splits()
                    shot.kill()
        screen.fill('black')
        for i in drawable:
            i.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()