import pygame
from Object import Object
from Star import Star
from Planet import Planet
from color import *

pygame.init()

screen_info = pygame.display.Info()
WIDTH = screen_info.current_w
HEIGHT = screen_info.current_h
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Solar System Simulation")

sun = Star("Sun", 0, 0, 0.004649 * Object.AU, SUN_COLOR, "images/sun.png", 1.98892 * 10**30)
 
mercury = Planet("Mercury", 0.387 * Object.AU, 0, 0.000016 * Object.AU, MERCURY_COLOR, "images/mercury.png",3.30 * 10**23, sun, -47.4 * 1000)
 
venus = Planet("Venus", 0.723 * Object.AU, 0, 0.000040 * Object.AU, VENUS_COLOR, "images/venus.png", 4.8685 * 10**24, sun, -35.02 * 1000)
	
earth = Planet("Earth", 1 * Object.AU, 0, 0.0000426 * Object.AU, EARTH_COLOR, "images/earth.png", 5.9742 * 10**24, sun, -29.783 * 1000)
 
moon = Planet("Moon", 1.00000257 * Object.AU, 0, 0.000012742 * Object.AU, MOON_COLOR, "images/moon.png", 7.342 * 10**2, sun, -1.022 * 1000)
 
mars = Planet("Mars", 1.524 * Object.AU, 0, 0.0000227 * Object.AU, MARS_COLOR, "images/mars.png", 6.39 * 10**23, sun, -24.077 * 1000)
 
jupiter = Planet("Jupiter", 5.20 * Object.AU, 0, 0.000469 * Object.AU, JUPITER_COLOR, "images/jupiter.png", 1.90 * 10**27, sun, -13.07 * 1000)
 
saturn = Planet("Saturn", 9.58 * Object.AU, 0, 0.000395 * Object.AU, SATURN_COLOR, "images/saturn.png", 5.68 * 10**26, sun, -9.69 * 1000)
	
uranus = Planet("Uranus", 19.18 * Object.AU, 0, 0.000173 * Object.AU, URANUS_COLOR, "images/uranus.png", 8.68 * 10**25, sun, -6.81 * 1000)
	
neptune = Planet("Neptune", 30.07 * Object.AU, 0, 0.000168 * Object.AU, NEPTUNE_COLOR, "images/neptune.png", 1.02 * 10**26, sun, 5.43 * 1000)
	
objects = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

def main():
	run = True
	clock = pygame.time.Clock()
	
	camera_offset_x = 0
	camera_offset_y = 0
 
	camera_speed = 10
	
	zoom_level = 1.0
	zoom_step = 1.0
 
	follow_index = None

	 
	while run:
		clock.tick(60)
		WIN.fill((0, 0, 0))			

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					camera_offset_x -= camera_speed
				if event.key == pygame.K_RIGHT:
					camera_offset_x += camera_speed
				if event.key == pygame.K_UP:
					camera_offset_y += camera_speed
				if event.key == pygame.K_DOWN:
					camera_offset_y -= camera_speed
				if event.key == pygame.K_EQUALS:
					zoom_level += zoom_step
					for object in objects:
						object.SCALE = object.BASE_SCALE * zoom_level
				if event.key == pygame.K_MINUS:
					zoom_level -= zoom_step
					for object in objects:
						object.SCALE = object.BASE_SCALE * zoom_level
				elif event.key == pygame.K_1:
					follow_index = 1
				elif event.key == pygame.K_2: 
					follow_index = 2
		if follow_index is not None:
			if 0 <= follow_index < len(objects):
				object_to_follow = objects[follow_index]
				camera_offset_x = -(object_to_follow.x * object_to_follow.SCALE) + (WIDTH / 2) - (object_to_follow.get_scaled_radius())
				camera_offset_y = -(object_to_follow.y * object_to_follow.SCALE) + (HEIGHT / 2) - (object_to_follow.get_scaled_radius())
		for object in objects:
			object.update_position(objects)
			object.draw(WIN, WIDTH, HEIGHT, camera_offset_x, camera_offset_y)
   
		pygame.display.update()

	pygame.quit()

main()