from Object import Object
import pygame
from color import WHITE

class Star(Object):
    def __init__(self, name, x, y, radius, color, image, mass, y_vel=0):
        super().__init__(name, x, y, radius, color, image, mass, y_vel)
    def draw_information(self, win, window_width, window_height, camera_offset_x, camera_offset_y):
        FONT = pygame.font.SysFont("Arial", 12)
        label = FONT.render(self.name, 1, WHITE)
        x, y = self.get_scaled_coordinate(self.x, self.y, window_width, window_height, camera_offset_x, camera_offset_y)
        win.blit(label, (x - label.get_width()/2, y - self.get_scaled_radius()))