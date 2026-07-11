
from pygame import sprite
from pygame.sprite import Sprite
from pygame import Surface

class Base_wall(Sprite):
    def __init__(self, color='black', w=40, h=40, x = 0, y= 0):
        super().__init__()

        self.image = Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect(left = x, top = y)

class Base_moveable(Sprite):
    def __init__(self, color='yellow', w=20, h=20, x = 0, y= 0):
        super().__init__()

        self.image = Surface([w, h])
        self.image.fill(color)

        self.current_x = x
        self.current_y = y
        self.width_s = self.image.get_width()
        self.height_s = self.image.get_height()

        self.rect = self.image.get_rect(left = x, top = y)

    def move(self, step = None):
        x, y = step
        if step == None or (x == 0 and y == 0):
            return False
        
        self.current_x += x
        self.current_y += y
        self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
        return True

    def update(self, new_point_xy = None, group_walls = None):
        if new_point_xy:
            if group_walls == None:
                raise Exception("No map!")
            if self.collision_take(group_walls):
                return False
            self.current_x, self.current_y = new_point_xy
            self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
            return True
        return False
    
    def collision_take(self, group_walls):
        collied_list = sprite.spritecollide(self, group_walls, False) 
        return collied_list


