import pygame as pg


class Config:

    pg.init()

    info = pg.display.Info()
    screen_width = 3 * info.current_w / 4
    screen_height = 3 * info.current_h / 4
    screen = pg.display.set_mode((screen_width, screen_height))

    # fps
    fps = 60

    # Environment variables
    gravity_pull_speed = 3

    # player

    player_height = 100
    player_width = 100

    player_img = pg.image.load("./assets/images/main_char.png").convert_alpha()
    player_img = pg.transform.scale(player_img, (player_width, player_height))

    player = pg.Rect(
        screen_width / 4, 4 * screen_height / 5, player_height, player_width
    )
    player_visual = (150, 20, 92)
    player_speed = 5
    player_jump_speed = 6
    jump_threashold = 120
