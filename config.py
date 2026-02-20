import pygame as pg


class Config:

    pg.init()

    info = pg.display.Info()
    width = info.current_w / 2
    height = info.current_h / 2
    screen = pg.display.set_mode((width, height))

    # fps
    fps = 60

    # Environment variables
    gravity_pull_speed = 3

    # player

    player_height = 50
    player_width = 50

    player_img = pg.image.load("./assets/images/main_char.png").convert_alpha()
    player_img = pg.transform.scale(player_img, (player_width, player_height))

    player = pg.Rect(width / 4, 4 * height / 5, player_height, player_width)
    player_visual = (150, 20, 92)
    player_speed = 5
    player_jump_speed = 6
    jump_threashold = 120
