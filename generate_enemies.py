from pygame import sprite
from constats import *
from Moveable_sprite import Ghost_sprite

def generate_enemies(screen, counts = 2):

    _, _, width, height = screen.get_rect()
    cord_x = width // 2
    cord_y = 0
 
    list_enemeis = [Ghost_sprite(cord_x + MOVE_IMAGE_SIZE*i, cord_y) for i in range(counts)]

    group_nemies = sprite.Group(*list_enemeis)

    return group_nemies