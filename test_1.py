import pygame
import sys

WIDTH = 800
HEIGHT = 600


def draw_player(screen, img, x_axis, y_axis):
    print(x_axis, y_axis)
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
            if event.type == pygame.KEYDOWN:
                print(event.key)
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

        # draw player
        draw_player(screen1, img, player_x, player_y)
        # update animation
        pygame.display.update()
        clock.tick(240)
