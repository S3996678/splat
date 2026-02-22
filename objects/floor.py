import pygame as pg
from config import Config as cf
from .platform import Platform


class Floor:
    def __init__(self, tile_num):
        self.floor = []
        for i in range(tile_num):
            tile = Platform(
                [
                    i * (cf.platform_size_xy - 1),
                    cf.screen_height - (cf.platform_size_xy - 3),
                ],
                cf.floor_img,
            )
            self.floor.append(tile)

    def draw(self):
        for tile in self.floor:
            tile.draw()
