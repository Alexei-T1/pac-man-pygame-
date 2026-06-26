
import pygame

from constats import *
from game_mape import generate_mape
from Moveable_sprite import Player_sprite


def take_events(pg):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
             
    keys = pg.key.get_pressed()

    if keys[pg.K_ESCAPE]:
        return False
    
    if keys[pg.K_w]:
        return (0, -1)
    if keys[pg.K_a]:
        return (-1, 0)
    if keys[pg.K_d]:
        return (1, 0)
    if keys[pg.K_s]:
        return (0, 1)
    
    return True

def next_move(keys, dt, ds = 10):
    if type(keys) == tuple:
        x, y = keys
        step = (x*dt*ds, y*dt*ds)
        return step
    return None

def run_game():
   

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    pygame.display.set_caption("PAC MAN")

    is_running = True
      
    player_pac = Player_sprite()
    player_pac_group = pygame.sprite.Group(player_pac)
    game_map = generate_mape(screen)
   

    while is_running:
        screen.fill(back_ground_color)

        is_running = take_events(pygame)
        dt = max(0.001, min( 0.1, clock.tick(50)/1000 ) )

        player_pac.update(next_move(is_running, dt, SPEED), game_map)

        game_map.draw(screen)
        player_pac_group.draw(screen)
        pygame.display.update()

    pygame.quit()






