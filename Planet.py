from Object import Object
import pygame
from color import WHITE

class Planet(Object):
    def __init__(self, name, x, y, radius, color, image, mass, orbited_star, y_vel=0):
        super().__init__(name, x, y, radius, color, image, mass, y_vel)
        self.orbited_star = orbited_star
        
    def draw_information(self, win, window_width, window_height):
        FONT = pygame.font.SysFont("Arial", 12)
        
        distance_x, distance_y, distance_to_star = self.get_distance_to_object(self.orbited_star)
        x, y = self.get_scaled_coordinate(window_width, window_height)
        
        distance_text = FONT.render(f"{round(distance_to_star/1000, 1)}km", 1, WHITE)
        label = FONT.render(self.name, 1, WHITE)
        
        
        win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
        
        win.blit(label, (x - label.get_width()/2, y - label.get_height()*2))
