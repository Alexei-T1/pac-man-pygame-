
from turtle import left

from pygame.sprite import Sprite
from pygame import Surface

class Base_wall(Sprite):
    def __init__(self, color='black', w=40, h=40, x = 0, y= 0):
        super().__init__()

        self.image = Surface([w, h])
        self.image.fill(color)
        self.rect = self.image.get_rect(left = x, top = y)