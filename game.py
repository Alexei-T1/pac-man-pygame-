
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
    is_pause = False
    game_over = False

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


    font_ob_pause = pygame.font.SysFont(None, PAUSE_FONT_SIZE)
    width_font, height_font = font_ob_pause.size('Pause')
    w_pad = width_font + PADDING*2
    h_pad = height_font + PADDING*2
    surf_bg_text_pause = pygame.Surface((w_pad, h_pad))
    surf_bg_text_pause.fill(black_color)
    surf_text_pause = font_ob_pause.render('Pause', True, green_color, black_color)
    surf_bg_text_pause.blit(surf_text_pause, (PADDING,PADDING))
    cord_x_pause = SCREEN_SIZE[0]//2 - w_pad//2
    cord_y_pause = SCREEN_SIZE[1]//2 - h_pad//2

    game_map = generate_mape(screen)
    enemeis_group = generate_enemies(screen)
      
    player_pac = Player_sprite()
    player_pac_group = pygame.sprite.Group(player_pac)

    
    while is_running:

        list_events = pygame.event.get()
        is_running = take_events_window_quit(pygame, list_events)
        input_key_exit = take_events_window_pause(pygame, list_events)
        
        if input_key_exit or game_over:
            if game_over:
                clock.tick(20)
                is_pause = True
            else:
                if is_pause:
                    clock.tick()
                    is_pause = False
                else:
                    clock.tick(20)
                    is_pause = True
                
        if not is_pause:
            screen.fill(back_ground_color)
            input_keys = take_events(pygame)
            dt = max(0.001, min( 0.1, clock.tick(50)/1000 ))

            is_ghost_collision = player_pac.update(dt, SPEED, keys = input_keys, group_walls = game_map, group_enemeis = enemeis_group)
            enemeis_group.update(dt, SPEED, group_walls = game_map, group_enemeis = enemeis_group)

            game_over = is_ghost_collision

            game_map.draw(screen)
            enemeis_group.draw(screen)
            player_pac_group.draw(screen)
            
            pygame.display.update()
        elif game_over:
            screen.blit(surf_bg_text, (cord_x_game_over, cord_y_game_over))
            pygame.display.update()
        else:
            screen.blit(surf_bg_text_pause, (cord_x_pause, cord_y_pause))
            pygame.display.update()

    pygame.quit()






