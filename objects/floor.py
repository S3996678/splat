import pygame as pg
from config import Config as cf
from .platform import Platform


class Floor:
    def __init__(self, tile_num, size):
        self.floor = []
        width = size[0]
        height = size[1]
        for i in range(tile_num):
            tile = Platform(
                [
                    i * (width - 1),
                    cf.screen_height - (height - 3),
                ],
                size,
                cf.floor_img,
            )
            self.floor.append(tile)

    def draw(self):
        for tile in self.floor:
            tile.draw()
