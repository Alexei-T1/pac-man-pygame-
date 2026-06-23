
import pygame

from game_mape import generate_mape

SCREEN_SIZE = (800, 600)
back_ground_color = pygame.color.Color(255, 255, 255)

def take_events(pg):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
             
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        return False
    
    return True

def game():
   

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    pygame.display.set_caption("PAC MAN")

    is_running = True
    dt = 0.1

    player_pac = ()
    game_map = generate_mape(screen)
   

    while is_running:
        screen.fill(back_ground_color)

        is_running = take_events(pygame)
        dt = max(0.001, min( 0.1, clock.tick(50)/1000 ) )

        game_map.draw(screen)

        pygame.display.update()

    pygame.quit()






