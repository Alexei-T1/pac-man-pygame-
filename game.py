
import pygame

from constats import *
from game_aux import *
from Moveable_sprite import *
from generate_enemies import generate_enemies


def run_game():
   

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    pygame.display.set_caption("PAC MAN")

    is_running = True

    font_ob_gameover = pygame.font.SysFont(None, GAME_OVER_FONT_SIZE)
    width_font, height_font = font_ob_gameover.size('Game over')
    w_pad = width_font + PADDING*2
    h_pad = height_font + PADDING*2
    surf_bg_text = pygame.Surface((w_pad, h_pad))
    surf_bg_text.fill(grey_color)
    surface_text_gameover = font_ob_gameover.render('Game over', True, red_color, grey_color)
    surf_bg_text.blit(surface_text_gameover, (PADDING,PADDING))
    cord_x_game_over = SCREEN_SIZE[0]//2 - w_pad//2
    cord_y_game_over = SCREEN_SIZE[1]//2 - h_pad//2

    game_map = generate_mape(screen)
    enemeis_group = generate_enemies(screen)
      
    player_pac = Player_sprite()
    player_pac_group = pygame.sprite.Group(player_pac)
    
    while is_running:
        screen.fill(back_ground_color)

        is_running = take_events(pygame)
        dt = max(0.001, min( 0.1, clock.tick(50)/1000 ) )

        is_ghost_collision = player_pac.update(dt, SPEED, keys = is_running, group_walls = game_map, group_enemeis = enemeis_group)
        enemeis_group.update(dt, SPEED, group_walls = game_map, group_enemeis = enemeis_group)

        if is_ghost_collision:
            is_running = False

        game_map.draw(screen)
        enemeis_group.draw(screen)
        player_pac_group.draw(screen)
        screen.blit(surf_bg_text, (cord_x_game_over, cord_y_game_over))
        pygame.display.update()
        
    pygame.quit()






