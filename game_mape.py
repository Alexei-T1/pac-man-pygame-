
import random
from pygame import sprite

from Base_sprite import Base_wall

def generate_mape(screen):

    group_wall = sprite.Group()
    one_b = Base_wall()

    _, _, width, height = screen.get_rect()

    col_b, row_b = width // one_b.image.get_width(), height // one_b.image.get_height()
    
    map_list = [ [ False if random.random() < 0.75 else group_wall.add(Base_wall(x = one_b.image.get_width()*c, y = one_b.image.get_height()*r)) 
                  for c in range(col_b) ] for r in range(1, row_b)]
    
    return group_wall