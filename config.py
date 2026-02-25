import pygame as pg


class Config:

    pg.init()
    pg.mixer.init()
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
    platform_size_xy = 50
    tmp_platform_img = pg.image.load("./assets/images/platform.png").convert_alpha()
    content_rect = tmp_platform_img.get_bounding_rect()
    cropped_img = tmp_platform_img.subsurface(content_rect)
    platform_img = pg.transform.scale(cropped_img, (platform_size_xy, platform_size_xy))

    # floor
    tmp_floor_img = pg.image.load("./assets/images/floor.png").convert_alpha()
    content_rect = tmp_floor_img.get_bounding_rect()
    cropped_img = tmp_floor_img.subsurface(content_rect)
    floor_img = pg.transform.scale(cropped_img, (platform_size_xy, platform_size_xy))

    # bullet
    bullet_size = player_height / 3
    bullet_img = pg.image.load("./assets/images/bullet.png").convert_alpha()
    bullet_img = pg.transform.scale(bullet_img, (bullet_size, bullet_size))
    bullet_speed = 9
    rate_of_fire_delay = 1000  # higher means more delay
    shooting_sound = pg.mixer.Sound("./assets/audio/shooting_sound.mp3")
