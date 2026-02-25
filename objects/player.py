import pygame as pg
import config


class Player:
    def __init__(self):
        self.health = None
        self.cf = config.Config()
        self.player = self.cf.player
        self.in_air = False
        self.jump_threashold = 0
        self.cur_platform = None  # store current platform player is on

    def draw(self):
        self.cf.screen.blit(self.cf.player_img, self.player)

    def movement(self, platform, platforms):
        keys = pg.key.get_pressed()

        # moving left logic
        if keys[pg.K_a] and self.player.left > 0:
            self.player.x -= self.cf.player_speed
            for p in platform:
                if self.player.colliderect(p.rect):
                    self.player.left = p.rect.right

        # moving right logic with barier at the end of map
        if keys[pg.K_d] and self.player.right < (3 *self.cf.screen_width / 5):
            self.player.x += self.cf.player_speed
            for p in platform:
                if self.player.colliderect(p.rect):
                    self.player.right = p.rect.left

        if keys[pg.K_d] and self.player.x >= (2 *self.cf.screen_width / 5):
            for p in platforms:
                p.rect.x -= (self.cf.player_speed * 2)

        # if in air go until reaching threashold else go down
        if self.in_air:
            self.player.y -= self.cf.player_jump_speed
            if self.player.bottom <= self.jump_threashold:
                self.in_air = False
        else:
            self.player.y += self.cf.gravity_pull_speed

        is_supported = False
        # go through all platforms and if collided with an object and in air it's the ceiling else it's the floor
        for p in platform:
            if self.player.colliderect(p.rect):
                if self.in_air:
                    self.player.top = p.rect.bottom
                    self.in_air = False
                else:
                    self.player.bottom = p.rect.top
                    is_supported = True
                    self.cur_platform = p

        # if on ground then jump
        if keys[pg.K_SPACE] and is_supported:
            self.in_air = True
            self.jump_threashold = self.player.bottom - self.cf.jump_threashold
        


    def get_player_pos(self):
        return self.player
