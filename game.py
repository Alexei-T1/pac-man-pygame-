
import pygame

from game_mape import generate_mape

from Base_sprite import Base_moveable

SCREEN_SIZE = (800, 600)
back_ground_color = pygame.color.Color(255, 255, 255)

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

def game():
   

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    pygame.display.set_caption("PAC MAN")

    is_running = True
    dt = 0.1
    speed = 100
    
    player_pac = Base_moveable()
    player_pac_group = pygame.sprite.Group(player_pac)
    game_map = generate_mape(screen)
   

    while is_running:
        screen.fill(back_ground_color)

        is_running = take_events(pygame)
        dt = max(0.001, min( 0.1, clock.tick(50)/1000 ) )

        player_pac.move(next_move(is_running, dt, speed))

        game_map.draw(screen)
        player_pac_group.draw(screen)
        pygame.display.update()

    pygame.quit()






