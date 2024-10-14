from simulation_setting import *

class CAR:

    def __init__(self, position, direction):
        self.driving    = False
        if direction in ["up", "down"]:
            self.w, self.h = (40, 60)

        elif direction in ["left", "right"]:
            self.w, self.h = (60, 40)

        self.x, self.y  = (position[0]+position[2]//2-self.w//2, position[1]+position[3]//2-self.h//2)
        self.direction  = direction
    
    def move(self):
        if self.direction == "up":
            self.y -= 1
        elif self.direction == "down":
            self.y += 1
        elif self.direction == "left":
            self.x -= 1
        elif self.direction == "right":
            self.x += 1
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, (self.x, self.y, self.w, self.h))

