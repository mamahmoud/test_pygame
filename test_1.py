import pygame
import sys
import random

WIDTH = 800
HEIGHT = 600


def draw_player(screen, img, x_axis, y_axis):
    # print(x_axis, y_axis)
    screen.blit(img, (x_axis, y_axis))


def draw_enemy(screen, img, x_axis, y_axis):
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
    enemy_image = pygame.image.load("alien.png")
    player_x = 370
    player_y = 500
    enemy_x = 380
    enemy_y = 20
    enemy_speed = 2
    player_speed = 10
    postive_distances = list(range(40, 101, enemy_speed * 5))
    negative_distances = list(range(-90, -29, enemy_speed * 5))
    distance = random.choice(postive_distances + negative_distances)
    # game loop
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
                        player_y -= player_speed
                    break
                # down
                elif event.key == pygame.K_DOWN:
                    if player_y <= 520:
                        player_y += player_speed
                    break
                # right
                elif event.key == pygame.K_RIGHT:
                    if player_x <= 720:
                        player_x += player_speed
                    break
                # left
                elif event.key == pygame.K_LEFT:
                    if player_x >= 20:
                        player_x -= player_speed
                    break
            if event.type == pygame.KEYUP:
                if event.key in [
                    pygame.K_UP,
                    pygame.K_DOWN,
                    pygame.K_RIGHT,
                    pygame.K_LEFT,
                ]:
                    pass

        # draw aplayer
        draw_player(screen1, player_image, player_x, player_y)
        # draw enemy
        if distance == 0:
            distance = random.choice(negative_distances + postive_distances)
        if enemy_x >= 725:
            distance = random.choice(negative_distances)
            distance += enemy_speed
            enemy_x -= enemy_speed
            draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
        elif enemy_x <= 15:
            distance = random.choice(postive_distances)
            distance -= enemy_speed
            enemy_x += enemy_speed
            draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
        elif distance > 0 and enemy_x < 725:
            distance -= enemy_speed
            enemy_x += enemy_speed
            draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
        elif distance < 0 and enemy_x > 15:
            distance += enemy_speed
            enemy_x -= enemy_speed
            draw_enemy(screen1, enemy_image, enemy_x, enemy_y)

        # draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
        # update animation
        pygame.display.update()
        clock.tick(60)
