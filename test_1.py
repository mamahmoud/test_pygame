import pygame
import sys

WIDTH = 800
HEIGHT = 600


def draw_player(screen, img, x_axis, y_axis):
    # print(x_axis, y_axis)
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
    player_image = pygame.image.load("space-invaders.png")
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
            if event.type == pygame.KEYDOWN:
                # up
                if event.key == pygame.K_UP:
                    if player_y >= 30:
                        player_y -= 10
                    break
                # down
                elif event.key == pygame.K_DOWN:
                    if player_y <= 520:
                        player_y += 10
                    break
                # right
                elif event.key == pygame.K_RIGHT:
                    if player_x <= 720:
                        player_x += 10
                    break
                # left
                elif event.key == pygame.K_LEFT:
                    if player_x >= 20:
                        player_x -= 10
                    break
            if event.type == pygame.KEYUP:
                if event.key in [
                    pygame.K_UP,
                    pygame.K_DOWN,
                    pygame.K_RIGHT,
                    pygame.K_LEFT,
                ]:
                    pass

        # draw player
        draw_player(screen1, player_image, player_x, player_y)
        # update animation
        pygame.display.update()
        clock.tick(240)
