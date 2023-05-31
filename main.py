import pygame
import math
from Object import Object

pygame.init()

screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Solar System Simulation")

SUN_COLOR = (255, 255, 0)
MERCURY_COLOR = (80, 78, 81)
VENUS_COLOR = (255, 255, 255)
EARTH_COLOR = (100, 149, 237)
MARS_COLOR = (188, 39, 50)
JUPITER_COLOR = (255, 165, 0)
SATURN_COLOR = (210, 180, 140)
URANUS_COLOR = (0, 128, 128)
NEPTUNE_COLOR = (0, 0, 139)

FONT = pygame.font.SysFont("comicsans", 16)

SUN_SIZE = 32

def main():
	run = True
	clock = pygame.time.Clock()
 
	sun = Object(0, 0, SUN_SIZE, SUN_COLOR, "images/sun.png", 1.98892 * 10**30)
 
	mercury = Object(0.387 * Object.AU, 0, SUN_SIZE/16, MERCURY_COLOR, "images/mercury.png",3.30 * 10**23, -47.4 * 1000)
 
	venus = Object(0.723 * Object.AU, 0, SUN_SIZE/12, VENUS_COLOR, "images/venus.png", 4.8685 * 10**24, -35.02 * 1000)
	
	earth = Object(1 * Object.AU, 0, SUN_SIZE/10, EARTH_COLOR, "images/earth.png", 5.9742 * 10**24, -29.783 * 1000)
 
	mars = Object(1.524 * Object.AU, 0, SUN_SIZE/14, MARS_COLOR, "images/mars.png", 6.39 * 10**23, -24.077 * 1000)
 
	jupiter = Object(5.20 * Object.AU, 0, SUN_SIZE/2, JUPITER_COLOR, "images/jupiter.png", 1.90 * 10**27, -13.07 * 1000)
 
	saturn = Object(9.58 * Object.AU, 0, SUN_SIZE/4, SATURN_COLOR, "images/saturn.png", 5.68 * 10**26, -9.69 * 1000)
	
	uranus = Object(19.18 * Object.AU, 0, SUN_SIZE/6, URANUS_COLOR, "images/uranus.png", 8.68 * 10**25, -6.81 * 1000)
	
	neptune = Object(30.07 * Object.AU, 0, SUN_SIZE/8, NEPTUNE_COLOR, "images/neptune.png", 1.02 * 10**26, 5.43 * 1000)
	
	objects = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
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