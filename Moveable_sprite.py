
from pygame import Surface
from pygame import sprite
from pygame import image
from pygame import Rect

from constats import *
from Base_sprite import Base_moveable

def get_image(cord_image, size_image = 32 ):
    
    x, y = cord_image
    x *= BASE_IMAGE_TITE
    y *= BASE_IMAGE_TITE

        
    base_image = image.load('./images/spritesheet.png').convert()
    base_image.set_colorkey(base_image.get_at((0,0)))
    base_image.set_clip(Rect(x, y, size_image, size_image))

    return base_image.subsurface(base_image.get_clip())

class Player_sprite(Base_moveable):
    def __init__(self):
        super().__init__()

        self.right_pac_ = get_image((2,0))
        self.left_pac_ = get_image((0,0))
        self.up_pac_ = get_image((6,0))
        self.down_pac_ = get_image((4,0))

        self.image = self.right_pac_


    def update(self, step = None, group_walls = None):
        if step:
            temp = (self.current_x, self.current_y)
            if group_walls == None:
                raise Exception("No map!")
            x, y = step
            self.current_x += x
            self.current_y += y
            self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
            if self.collision_take(group_walls) or self.current_x < 0 or self.current_x > SCREEN_SIZE[0] -  MOVE_IMAGE_SIZE\
                or self.current_y < 0 or self.current_y > SCREEN_SIZE[1] - MOVE_IMAGE_SIZE:
                self.current_x, self.current_y = temp
                self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
                return False
            if x < 0:
                self.image = self.left_pac_
            if x > 0:
                self.image = self.right_pac_
            if y < 0:
                self.image = self.up_pac_
            if y > 0:
                self.image = self.down_pac_ 

            self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
            return True
        return False
    
    def collision_take(self, group_walls):
        collied_list = sprite.spritecollide(self, group_walls, False) 
        return collied_list
