import random
from pygame import sprite

from constats import *
from game_aux import *
from game_aux import get_image
from Base_sprite import Base_moveable


class Player_sprite(Base_moveable):
    def __init__(self, type_player = PLAYER):
        super().__init__()

        self.player = type_player
        self.set_game_image()
        
        self.way = None

    def set_game_image(self):

        self.right_pac_ = get_image((2,0))
        self.left_pac_ = get_image((0,0))
        self.up_pac_ = get_image((6,0))
        self.down_pac_ = get_image((4,0))

        self.image = self.right_pac_

    def set_game_way(self, keys):
        self.way = keys

    def change_game_image(self, x, y):
            if self.player:
                if x < 0:
                    self.image = self.left_pac_
                if x > 0:
                    self.image = self.right_pac_
                if y < 0:
                    self.image = self.up_pac_
                if y > 0:
                    self.image = self.down_pac_


    def update(self, dt, speed, keys = None, group_walls = None, group_enemeis = None):
        if self.collision_take(group_enemeis):
            return True
        if type(keys) != tuple:
            return False
        self.set_game_way(keys)
        step = next_move(self.way, dt, speed)
        temp = self.pre_step_temp(step, group_walls)

        self.check_collision(temp, group_walls)
        if self.collision_take(group_enemeis):
            return True
                  
        x, y = self.way    
        self.change_game_image(x, y)

        self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
        return False
    
    def check_collision(self, temp, group_walls):
        if temp:
            if self.get_game_collision(group_walls, temp):
                    self.current_x, self.current_y = temp
                    self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
                    return True
        return False

    def get_game_collision(self, group_walls, temp):
        if self.collision_take(group_walls) or self.current_x < 0 or self.current_x > SCREEN_SIZE[0] -  MOVE_IMAGE_SIZE\
                or self.current_y < 0 or self.current_y > SCREEN_SIZE[1] - MOVE_IMAGE_SIZE:
            self.current_x, self.current_y = temp
            self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
            return True
        return False
    
    def pre_step_temp(self, step, group_walls):
        if step:
            temp = (self.current_x, self.current_y)
            if group_walls == None:
                raise Exception("No map!")
            x, y = step
            self.current_x += x
            self.current_y += y
            self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
            return temp
        return False 


class Ghost_sprite(Player_sprite):
    def __init__(self, x = 150, y= 0, type_player = GHOST):
        super().__init__()

        self.current_x = x 
        self.current_y = y
        self.player = type_player
        self.rect = self.image.get_rect(left = x, top = y)

        self.list_way = (LEFT, RIGHT, UP, DOWN)

        self.timer_ghost = 0
        self.timer_time = 5 * random.uniform(0.5, 2.0)

    def set_game_image(self):

        self.right_ghost_ = get_image((10,6))
        self.image = self.right_ghost_

    def set_game_way(self, dt):
        if self.way == None:
            self.change_way_random()

        self.timer_ghost += dt
        if self.timer_ghost > self.timer_time:
            self.timer_ghost = 0
            self.timer_time = 5 * random.uniform(0.5, 2.0)
            self.change_way_random()

    def change_way_random(self):
        if self.way == None:
            self.way = self.list_way[random.randint(0, len(self.list_way)-1)]
        else:
            temp_list_way = [way for way in self.list_way if self.way != way]
            self.way = temp_list_way[random.randint(0, len(temp_list_way)-1)] 
    
    def update(self, dt, speed, group_walls = None, group_enemeis = None):
        self.set_game_way(dt)
        group_sprites_not_this = self.check_ghost_collision(group_enemeis)
        step = next_move(self.way, dt, speed)
        temp = self.pre_step_temp(step, group_walls)

        self.check_collision(temp, group_walls, group_sprites_not_this, dt, speed)

        x, y = self.way    
        self.change_game_image(x, y)

        self.rect = self.image.get_rect(left = self.current_x, top = self.current_y)
        return True

    def check_collision(self, temp, group_walls, group_sprites_not_this, dt, speed):
        if temp:  
            while self.get_game_collision(group_walls, temp) or self.get_game_collision(group_sprites_not_this, temp):
                self.change_way_random()
                step = next_move(self.way, dt, speed)
                self.pre_step_temp(step, group_walls)

    def check_ghost_collision(self, group_enemeis):
        group_sprites_not_this = sprite.Group(*group_enemeis)
        group_sprites_not_this.remove(self)

        return group_sprites_not_this
