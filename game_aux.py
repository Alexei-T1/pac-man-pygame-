
import random
from pygame import sprite
from pygame import image
from pygame import Rect

from constats import *
from Base_sprite import Base_wall

def take_events(pg):            
    keys = pg.key.get_pressed()  
    if keys[pg.K_w]:
        return UP
    if keys[pg.K_a]:
        return LEFT
    if keys[pg.K_d]:
        return RIGHT
    if keys[pg.K_s]:
        return DOWN
    
    return True

def take_events_window_quit(pg, list_events):
    for event in list_events:
        if event.type == pg.QUIT:
            return False 
    return True

def take_events_window_pause(pg, list_events):           
    for event in list_events:
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            return True   
    return False
# 

def next_move(keys, dt, ds = 10):
    if type(keys) == tuple:
        x, y = keys
        step = (x*dt*ds, y*dt*ds)
        return step
    return None


def get_image(cord_image, size_image = 32 ):
    
    x, y = cord_image
    x *= BASE_IMAGE_TITE
    y *= BASE_IMAGE_TITE
        
    base_image = image.load('./images/spritesheet.png').convert()
    base_image.set_colorkey(base_image.get_at((0,0)))
    base_image.set_clip(Rect(x, y, size_image, size_image))

    return base_image.subsurface(base_image.get_clip())


def generate_mape(screen):

    group_wall = sprite.Group()
    one_b = Base_wall()

    _, _, width, height = screen.get_rect()

    col_b, row_b = width // one_b.image.get_width(), height // one_b.image.get_height()
    
    map_list = [ [ False if random.random() < 0.75 else group_wall.add(Base_wall(x = one_b.image.get_width()*c, y = one_b.image.get_height()*r)) 
                  for c in range(col_b) ] for r in range(1, row_b)]
    
    return group_wall





