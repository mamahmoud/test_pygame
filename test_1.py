from pickle import FALSE
import pygame
import sys

if __name__ == "__main__":
    pygame.init()
    screen1 = pygame.display.set_mode((500, 500))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
