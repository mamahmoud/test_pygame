from pickle import FALSE
import pygame
import sys

if __name__ == "__main__":
    # initialize
    pygame.init()
    # create window
    screen1 = pygame.display.set_mode((500, 500))
    # title
    pygame.display.set_caption("Hello pygame by mohamed")
    # adding image icon
    icon = pygame.image.load("startup.png")
    pygame.display.set_icon(icon)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
