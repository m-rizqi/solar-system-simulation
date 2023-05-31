import pygame
import math
from Object import Object

pygame.init()

WIDTH, HEIGHT =  1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)

FONT = pygame.font.SysFont("comicsans", 16)

LARGEST_OBJECT = 32

def main():
	run = True
	clock = pygame.time.Clock()

	sun = Object(0, 0, LARGEST_OBJECT, YELLOW, "images/sun.png", 1.98892 * 10**30)
    mercury = Object(0.387 * Object.AU, 0, 8, DARK_GREY, "images/sun.png",3.30 * 10**23,-47.4 * 1000)
    earth = Object(-1 * Object.AU, 0, LARGEST_OBJECT / 2, BLUE, "images/earth.png", 5.9742 * 10**24, 29.783 * 1000 )

	# mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
	# mars.y_vel = 24.077 * 1000

	# mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
	# mercury.y_vel = -47.4 * 1000

	# venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
	# venus.y_vel = -35.02 * 1000

	objects = [sun, earth]

	while run:
		clock.tick(60)
		WIN.fill((0, 0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for object in objects:
			object.update_position(objects)
			object.draw(WIN, WIDTH, HEIGHT)

		pygame.display.update()

	pygame.quit()


main()