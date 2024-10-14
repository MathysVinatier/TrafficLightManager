from CAR import *
from CROSSROAD import *
from BUTTON import *
import time

pygame.init()

left_traffic    = CROSSROAD((WIDTH//3-30, 2*HEIGHT//3+15), "right")
down_traffic    = CROSSROAD((2*WIDTH//3+16, 2*HEIGHT//3+27), "up")
right_traffic   = CROSSROAD((2*WIDTH//3+27, HEIGHT//3-17), "left")
up_traffic      = CROSSROAD((WIDTH//3-15, HEIGHT//3-25), "down")

feux = [left_traffic, down_traffic, right_traffic, up_traffic]

left_button  = BUTTON("right")  
down_button  = BUTTON("up")
right_button = BUTTON("left")
up_button    = BUTTON("down")

buttons = [left_button, down_button, right_button, up_button]

voitures = []

running = True
clock = pygame.time.Clock()
car_number = 1

start_time = time.time()
def clock_watch():
    return int(time.time() - start_time)


def draw_crossroad(screen):
    
    # Dessiner la route (carrefour gris)
    pygame.draw.rect(screen, GRAY, (WIDTH // 3, 0, WIDTH // 3, HEIGHT))
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 3, WIDTH, HEIGHT // 3))
    
    # Dessiner les lignes pointillées jaunes (verticales)
    for i in range(0, HEIGHT):
        if i < 2*HEIGHT//3 and i > 1*HEIGHT//3:
            pass
        else :
            pygame.draw.line(screen, YELLOW, (WIDTH // 2, i), (WIDTH // 2, i), 1) 
        
        
    for i in range(0, WIDTH):
        if i < 2*WIDTH//3 and i > 1*WIDTH//3:
            pass
        else :
            pygame.draw.line(screen, YELLOW, (i, HEIGHT // 2), (i, HEIGHT // 2), 3) 

start_time = time.time()
while running:

    screen.fill(GREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons :
                if button.zone[0] <= mouse_pos[0] <= (button.zone[0]+button.zone[2]) and button.zone[1] <= mouse_pos[1] <= (button.zone[1]+button.zone[3]):
                    voitures.append(CAR(button.zone, button.direction))
                    car_number += 1

    draw_crossroad(screen)

    for button in buttons:
        button.draw(screen)

    for feu in feux:
        feu.draw(screen)

    for voiture in voitures:
        for feu in feux:
            if feu.direction == voiture.direction :
                if feu.color == RED :
                    print("red")
                    if voiture.direction=="up" or voiture.direction=="down":
                        print("up/down")
                        print(f'{feu.position[1]}/{voiture.position[1]}={feu.position[1] == voiture.position[1]}')
                        if feu.position[1] == voiture.position[1]:
                            voiture.driving = False
                    else :
                        print("left/right")
                        if feu.position[0] == voiture.position[0]:
                            voiture.driving = False

                if feu.color == GREEN:
                    voiture.driving = True

        if voiture.driving :
            voiture.move()

        voiture.draw(screen)

    pygame.display.flip()
    clock.tick(60)



    for t in range(1,5):
        if (clock_watch()%(t+1))==1:
            feux[t-1].change_color(GREEN)
        else:
            feux[t-1].change_color(RED)

pygame.quit()