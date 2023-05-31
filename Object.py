import pygame
import math

class Object:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 250 / AU 
    TIMESTEP = 3600*24
    
    def __init__(self, x, y, radius, color, image, mass, y_vel=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.image = image

        self.orbit = []

        self.x_vel = 0
        self.y_vel = y_vel
    
    def draw(self, win, window_width, window_height):
        x = self.x * self.SCALE + window_width / 2
        y = self.y * self.SCALE + window_height / 2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + window_width / 2
                y = y * self.SCALE + window_height / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, int(self.radius * 0.7))
        
        image = pygame.image.load(self.image)
        image = pygame.transform.scale(image, (self.radius * 2, self.radius * 2))
        image_rect = image.get_rect(center=(x, y))
        win.blit(image, image_rect)
    
    def attraction_force(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, objects):
        total_fx = total_fy = 0
        for object in objects:
            if self == object:
                continue

            fx, fy = self.attraction_force(object)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))