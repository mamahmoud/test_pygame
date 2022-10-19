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
    # setting clock
    clock = pygame.time.Clock()
    # title
    pygame.display.set_caption("Hello pygame by mohamed")
    # adding image icon
    icon = pygame.image.load("startup.png")
    img = pygame.image.load("startup_2.png")
    player_x = 370
    player_y = 500

    # game loop
    i = 0
    while True:
        # change color
        screen1.fill((255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                print(event.key)
                if event.key == 1073741906:
                    player_y -= 10
                    break
                elif event.key == 1073741905:
                    player_y += 10
                    break
                elif event.key == 1073741903:
                    player_x += 10
                    break
                elif event.key == 1073741904:
                    player_x -= 10
                    break

        # draw player
        draw_player(screen1, img, player_x, player_y)
        # draw_player(screen1, img, i, i)
        i += 1
        # update animation
        pygame.display.update()
        clock.tick(240)
