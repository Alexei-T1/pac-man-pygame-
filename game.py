
import pygame

SCREEN_SIZE = (800, 600)
back_ground_color = pygame.color.Color(255, 255, 255)

def take_events(pg):
        pass

def game():
   

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    pygame.display.set_caption("PAC MAN")

    is_running = True
    dt = 0.1

    player_pac = ()
    game_map = ()

    


    while is_running:
        screen.fill(back_ground_color)

        is_running = take_events(pygame)

        dt = max(0.001, min( 0.1, clock.tick(50)/1000 ) )
    

    pygame.quit()






