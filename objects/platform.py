import pygame as pg
from config import Config as cf
from .staticEntity import StaticEntity


class Platform(StaticEntity):
    def __init__(self, position, size, texture=cf.platform_img):
        super().__init__(position, size, texture)
