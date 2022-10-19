import pygame
import sys

WIDTH = 800
HEIGHT = 600


def draw_player(screen, img, x_axis, y_axis):
    screen.blit(img, (x_axis, y_axis))


if __name__ == "__main__":
    # initialize
    pygame.init()
    # create window
    screen1 = pygame.display.set_mode((WIDTH, HEIGHT))
    # title
    pygame.display.set_caption("Hello pygame by mohamed")
    # adding image icon
    icon = pygame.image.load("startup.png")
    img = pygame.image.load("startup_2.png")

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
        # change color
        screen1.fill((255, 0, 0))
        # draw player
        draw_player(screen1, img, 370, 500)
        # update animation
        pygame.display.update()
