import pygame as pg
import config


class Player:
    def __init__(self):
        self.health = None
        self.cf = config.Config()
        self.player = self.cf.player
        self.in_air = False
        self.jump_threashold = 0

    def draw(self):
        self.cf.screen.blit(self.cf.player_img, self.player)

    def movement(self, platform):

        keys = pg.key.get_pressed()  # gravity
        for p in platform:
            if not self.player.bottom >= p.rect.top and not self.in_air:
                self.player.y += self.cf.gravity_pull_speed

        if keys[pg.K_a] and self.player.x > 0:  # left
            self.player.x -= self.cf.player_speed

        if (
            keys[pg.K_d]
            and (self.player.x + self.cf.player_width) < self.cf.screen_width
        ):  # Right
            self.player.x += self.cf.player_speed

        for p in platform:
            if keys[pg.K_SPACE] and (
                (self.player.y + self.player.height) >= p.rect.top
            ):  # start jump if on platform
                self.player.y -= self.cf.player_jump_speed
                self.in_air = True
                self.jump_threashold = p.rect.top - self.cf.jump_threashold

        if self.in_air:  # keep jumping
            self.player.y -= self.cf.player_jump_speed
        # if reached top of jump stop
        if (self.player.y + self.player.height) <= self.jump_threashold:
            self.in_air = False

    def get_player_pos(self):
        return self.player
