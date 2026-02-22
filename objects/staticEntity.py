import pygame as pg
from config import Config as cf


class StaticEntity:
    def __init__(self, position, texture):
        self.postion = position
        self.texture = texture
        # set platform with placement
        self.rect = self.texture.get_rect(topleft=position)
        # set mask for the rendering
        self.mask = pg.mask.from_surface(self.texture)

    def draw(self):
        cf.screen.blit(self.texture, self.rect)

    # check if the entity is in range horizontaly
    def is_within_range_x(self, entity_x):
        if self.rect.left <= entity_x <= self.rect.right:
            return True
        return False

    # check if the entity is in range vertically
    def is_within_range_y(self, entity_y):
        if self.rect.top <= entity_y <= self.rect.bottom:
            return True
        return False
