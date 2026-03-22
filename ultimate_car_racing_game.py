import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Car Racing Game")

clock = pygame.time.Clock()

player_x = 280
player_y = 580
player_speed = 7

enemy_cars = []

for i in range(3):
    x = random.randint(50,500)
    y = random.randint(-600,-100)
    enemy_cars.append([x,y])

enemy_speed = 6

score = 0
font = pygame.font.SysFont(None,40)

road_lines = []
for i in range(10):
    road_lines.append([300,i*80])

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 510:
        player_x += player_speed

    screen.fill((30,30,30))

    pygame.draw.rect(screen,(80,80,80),(50,0,500,700))

    for line in road_lines:
        pygame.draw.rect(screen,(255,255,255),(line[0],line[1],10,40))
        line[1]+=10
        if line[1] > HEIGHT:
            line[1] = -40

    for car in enemy_cars:

        car[1] += enemy_speed

        if car[1] > HEIGHT:
            car[1] = random.randint(-400,-100)
            car[0] = random.randint(60,500)
            score += 1

        pygame.draw.rect(screen,(255,0,0),(car[0],car[1],40,70))

        if (player_x < car[0] + 40 and
            player_x + 40 > car[0] and
            player_y < car[1] + 70 and
            player_y + 70 > car[1]):

            running = False

    pygame.draw.rect(screen,(0,255,0),(player_x,player_y,40,70))

    score_text = font.render("Score: " + str(score), True, (255,255,255))
    screen.blit(score_text,(10,10))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
