import pygame as pg


class Config:

    pg.init()

    info = pg.display.Info()
    width = info.current_w / 2
    height = info.current_h / 2
    screen = pg.display.set_mode((width, height))

    # fps
    fps = 60
