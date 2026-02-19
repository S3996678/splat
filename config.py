import pygame as pg


class Config:

    pg.init()

    info = pg.display.Info()
    width = info.current_w / 2
    height = info.current_h / 2
    screen = pg.display.set_mode((width, height))

    # fps
    fps = 60

    # player
    player = pg.Rect(width / 4, 4 * height / 5, 50, 50)
    player_visual = (150, 20, 92)
    player_speed = 5
