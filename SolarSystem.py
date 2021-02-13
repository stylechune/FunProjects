import pygame
import random
import math

pygame.init()

# defining colours
BLACK = (0, 0, 0)
PURPLE = (221, 160, 221)
GREEN = (34, 139, 34)
STARRY = (252, 252, 202)
RED = (255, 0, 0)
BROWN = (222, 184, 135)
LBLUE = (152, 242, 245)
YELLOW = (242, 242, 61)

PI = 3.141592653

SCREENW = 720
SCREENH = 720

size = (SCREENW, SCREENH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stars and Planets")

done = False

# creating random lists of coordinates and sizes for stars
stars1 = []
stars2 = []
for s in range (80):
    x_star1 = random.randrange(0, 720)
    y_star1 = random.randrange(0, 720)
    s_star1 = random.randrange(2, 5)
    stars1.append([x_star1, y_star1, s_star1])
    x_star2 = random.randrange(0, 720)
    y_star2 = random.randrange(0, 720)
    s_star2 = random.randrange(2, 5)
    stars2.append([x_star2, y_star2, s_star2])

# variables for planets

# making centre of screen the centre of rotation
centre_of_rotation_x = SCREENW / 2
centre_of_rotation_y = SCREENH / 2

# creating a list of angular velocity with different speeds
omega = []
# creating a list of the same angle to use with omega
angles = []
for o in range(1, 5):
    omega_values = 0.1 / o
    omega.append(omega_values)
    angle = math.radians(45)
    angles.append(angle)

# creating 4 planets, spaced out evenly
planets = []
for p in range (80, 291, 70):
    radius = p
    x = centre_of_rotation_x + radius * math.cos(angle)
    y = centre_of_rotation_y - radius * math.sin(angle)
    planets.append([radius, x, y])

clock = pygame.time.Clock()

# main program loop
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # getting time to make stars blink every half second
    current_time = pygame.time.get_ticks()
    star_time = math.floor(current_time / 500)

    # setting planets to move at different speeds in a circle
    for v in range(4):
        angles[v] += omega[v]
        planets[v][1] = planets[v][1] + planets[v][0] * omega[v] * math.cos(angles[v] + PI / 2)
        planets[v][2] = planets[v][2] - planets[v][0] * omega[v] * math.sin(angles[v] + PI / 2)

    # putting a ring around the blue planet
    back_ring = [planets[1][1] - 30, planets[1][2] - 10, 60, 20]
    front_ring = [planets[1][1] - 30, planets[1][2] - 10, 60, 20]

    screen.fill(BLACK)

    # drawing stars behind everything else
    for s in range(80):
        if star_time % 2 == 0:
            pygame.draw.circle(screen, STARRY, [stars1[s][0], stars1[s][1]], stars1[s][2])
        if star_time % 2 != 0:
            pygame.draw.circle(screen, STARRY, [stars2[s][0], stars2[s][1]], stars2[s][2])

    # drawing sun
    pygame.draw.circle(screen, YELLOW, [360, 360], 50)

    # drawing planets
    pygame.draw.circle(screen, RED, [planets[0][1], planets[0][2]], 8)

    # drawing ring around blue
    pygame.draw.arc(screen, PURPLE, back_ring, 0, PI, 4)
    pygame.draw.circle(screen, LBLUE, [planets[1][1], planets[1][2]], 20)
    pygame.draw.arc(screen, PURPLE, front_ring, PI, 0, 4)

    pygame.draw.circle(screen, BROWN, [planets[2][1], planets[2][2]], 15)
    pygame.draw.circle(screen, GREEN, [planets[3][1], planets[3][2]], 30)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
