from simulation_setting import *

class BUTTON:

    def __init__(self, direction):
        self.direction  = direction
        w = 100
        h = 70
        if direction == "right":
            x = 10
            y = (7*(HEIGHT//3))//4
            self.zone  = (x, y-h//2, w, h)

        elif direction == "up":
            x = (7*(WIDTH//3))//4
            y = HEIGHT - 10 - h
            self.zone  = (x-w//2,y , w, h)

        elif direction == "left":
            x = WIDTH - 10 - w
            y = (5*(HEIGHT//3))//4
            self.zone  = (x, y-h//2, w, h)

        elif direction == "down":
            x = (5*(WIDTH//3))//4
            y = 10
            self.zone  = (x-w//2, y, w, h)

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.zone)