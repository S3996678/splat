import pygame as pg


class Config:

    pg.init()
    print("called")

    info = pg.display.Info()
    screen_width = 4 * info.current_w / 4
    screen_height = screen_width / 2
    grid_split_ratio_x = 20
    grid_split_ratio_y = 10

    # map
    floor_length = 1300

    block_height = screen_height / grid_split_ratio_y

    screen = pg.display.set_mode((screen_width, screen_height))
    print(screen_height, screen_width)

    # fps
    fps = 60

    # Environment variables
    gravity_pull_speed = 3

    # player

    player_height = block_height
    player_width = block_height

    player_img = pg.image.load("./assets/images/main_char.png").convert_alpha()
    player_img = pg.transform.scale(player_img, (player_width, player_height))

    player = pg.Rect(
        screen_width / 4, 4 * screen_height / 5, player_height, player_width
    )
    player_visual = (150, 20, 92)
    player_speed = 5
    player_jump_speed = 6

    jump_threashold = block_height * 4

    # platform
    tmp_platform_img = pg.image.load("./assets/images/platform.png").convert_alpha()
    platform_img = tmp_platform_img.subsurface(tmp_platform_img.get_bounding_rect())

    # floor
    tmp_floor_img = pg.image.load("./assets/images/floor.png").convert_alpha()
    floor_img = tmp_floor_img.subsurface(tmp_floor_img.get_bounding_rect())
