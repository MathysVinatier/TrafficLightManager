from simulation_setting import *

class CROSSROAD:

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.color = RED
        self.circle_size = 13

    def change_color(self, new_color):
        self.color = new_color

    def draw(self, screen):
        x_start = self.position[0]-self.circle_size
        y_start = self.position[1]-self.circle_size
        pygame.draw.rect(screen, BLACK, (x_start-5, y_start-5, 36, 36))
        pygame.draw.circle(screen, self.color,self.position, self.circle_size, self.circle_size)

