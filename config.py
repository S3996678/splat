import pygame as pg


class Config:

    pg.init()
    print("called")

    info = pg.display.Info()
    screen_width = int(3 * info.current_w / 4)
    screen_height = int(3 * info.current_h / 4)
    screen = pg.display.set_mode((screen_width, screen_height))
    print(screen_height, screen_width)

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
    jump_threashold = (7 / 36) * screen_height

    # platform
    tmp_platform_img = pg.image.load("./assets/images/platform.png").convert_alpha()
    platform_img = tmp_platform_img.subsurface(tmp_platform_img.get_bounding_rect())

    # floor
    tmp_floor_img = pg.image.load("./assets/images/floor.png").convert_alpha()
    floor_img = tmp_floor_img.subsurface(tmp_floor_img.get_bounding_rect())
