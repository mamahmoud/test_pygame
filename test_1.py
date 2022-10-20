"""
Space game
"""
import sys
import random
import pygame


WIDTH = 800
HEIGHT = 600
ENEMY_SPEED = 2
PLAYER_SPEED = 10
BULLET_SPEED = 10


def draw_player(screen, img, x_axis, y_axis):
    """
    Draw player
    """
    # print(x_axis, y_axis)
    screen.blit(img, (x_axis, y_axis))


def draw_enemy(screen, img, x_axis, y_axis):
    """
    Draw enemy
    """
    # print(x_axis, y_axis)
    screen.blit(img, (x_axis, y_axis))


def draw_bullet(screen, img, x_axis, y_axis):
    """
    Draw bullet
    """
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
    background_image = pygame.image.load("background.jpg")
    bullet_image = pygame.image.load("bullet.png")
    player_x = 370
    player_y = 500
    enemy_x = 380
    enemy_y = 20
    bullet_on = False
    enemy_alive = True
    postive_distances = list(range(40, 101, ENEMY_SPEED * 5))
    negative_distances = list(range(-90, -29, ENEMY_SPEED * 5))
    distance = random.choice(postive_distances + negative_distances)
    # game loop
    while True:
        # background
        screen1.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                # up
                if event.key == pygame.K_UP:
                    if player_y >= 30:
                        player_y -= PLAYER_SPEED
                # down
                elif event.key == pygame.K_DOWN:
                    if player_y <= 520:
                        player_y += PLAYER_SPEED
                # right
                elif event.key == pygame.K_RIGHT:
                    if player_x <= 720:
                        player_x += PLAYER_SPEED
                # left
                elif event.key == pygame.K_LEFT:
                    if player_x >= 20:
                        player_x -= PLAYER_SPEED
            if (
                (event.type == pygame.KEYDOWN)
                and (event.key == pygame.K_a)
                and (not bullet_on)
            ):
                bullet_on = True
                bullet_x, bullet_y = player_x + 24, player_y
                print(bullet_x, bullet_y)

        # draw aplayer
        draw_player(screen1, player_image, player_x, player_y)
        if bullet_on:
            if bullet_y > 20:
                bullet_y -= BULLET_SPEED
                draw_bullet(screen1, bullet_image, bullet_x, bullet_y)
            else:
                bullet_on = False

        # draw enemy
        if enemy_alive and bullet_on:
            if (abs(bullet_x - enemy_x) < 20) and (abs(bullet_y - enemy_y) < 20):
                enemy_alive = False
                bullet_on = False
        if enemy_alive:

            if distance == 0:
                distance = random.choice(negative_distances + postive_distances)
            if enemy_x >= 725:
                distance = random.choice(negative_distances)
                distance += ENEMY_SPEED
                enemy_x -= ENEMY_SPEED
                draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
            elif enemy_x <= 15:
                distance = random.choice(postive_distances)
                distance -= ENEMY_SPEED
                enemy_x += ENEMY_SPEED
                draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
            elif distance > 0 and enemy_x < 725:
                distance -= ENEMY_SPEED
                enemy_x += ENEMY_SPEED
                draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
            elif distance < 0 and enemy_x > 15:
                distance += ENEMY_SPEED
                enemy_x -= ENEMY_SPEED
                draw_enemy(screen1, enemy_image, enemy_x, enemy_y)

        # draw_enemy(screen1, enemy_image, enemy_x, enemy_y)
        # update animation
        pygame.display.update()
        clock.tick(60)
