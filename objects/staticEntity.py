import pygame as pg
from config import Config as cf


class StaticEntity:
    def __init__(self, position, size, texture):
        self.postion = position
        self.texture = pg.transform.scale(texture, (int(size[0]), int(size[1])))
        # set platform with placement
        self.rect = self.texture.get_rect(topleft=position)
        # set mask for the rendering
        self.mask = pg.mask.from_surface(self.texture)

    def draw(self):
        cf.screen.blit(self.texture, self.rect)
