import pygame
import math

class Object:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    BASE_SCALE = 250 / AU
    SCALE = BASE_SCALE
    IMAGE_SCALE = 1
    TIMESTEP = 3600*24
    
    def __init__(self, name, x, y, radius, color, image, mass, y_vel=0):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.image = image

        self.orbit = []

        self.x_vel = 0
        self.y_vel = y_vel
    
    # View Stuff
    def draw(self, win, window_width, window_height, camera_offset_x, camera_offset_y):
        x, y = self.get_scaled_coordinate(window_width, window_height, camera_offset_x, camera_offset_y)
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + window_width / 2 + camera_offset_x
                y = y * self.SCALE + window_height / 2 + camera_offset_y
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, int(self.get_scaled_radius() * 0.7))
                
        image = pygame.image.load(self.image)
        image = pygame.transform.scale(image, (self.get_scaled_radius() * 2, self.get_scaled_radius() * 2))
        image_rect = image.get_rect(center=(x, y))
        win.blit(image, image_rect)
        self.draw_information(win, window_width, window_height, camera_offset_x, camera_offset_y)
    
    def draw_information(self, win, window_width, window_height, camera_offset_x, camera_offset_y):
        pass   
    
    def get_scaled_coordinate(self, window_width, window_height, camera_offset_x, camera_offset_y):
        x = (self.x * self.SCALE) + (window_width / 2)  + camera_offset_x
        y = (self.y * self.SCALE) + (window_height / 2) + camera_offset_y
        return x, y
    
    def get_scaled_radius(self):
        return self.radius * self.SCALE * self.IMAGE_SCALE
    
    # Pyhsics Stuff 
    def attraction_force(self, other):
        distance_x, distance_y, distance = self.get_distance_to_object(other)

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y, force
    
    def get_distance_to_object(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        return distance_x, distance_y, distance
    
    def update_position(self, objects):
        total_fx, total_fy = self.get_total_attraction_force(objects)

        self.calculate_velocity(total_fx, total_fy)
        self.calculate_position()
        
        self.orbit.append((self.x, self.y))
    
    def get_total_attraction_force(self, objects):
        total_fx = total_fy = 0
        for object in objects:
            if self == object:
                continue

            fx, fy, f= self.attraction_force(object)
            total_fx += fx
            total_fy += fy
        return total_fx, total_fy
    
    def calculate_velocity(self, total_fx, total_fy):
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
    
    def calculate_position(self):
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        