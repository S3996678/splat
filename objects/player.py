import pygame as pg
import config


class Player:
    def __init__(self):
        self.health = None
        self.cf = config.Config()
        self.player = self.cf.player

    def draw(self):
        pg.draw.rect(self.cf.screen, self.cf.player_visual, self.player)

    def movement(self, platform):
        keys = pg.key.get_pressed()
        if (self.player.y + self.player.height) < platform:
            self.player.y += self.cf.gravity_pull_speed 
        if keys[pg.K_a]:
            self.player.x -= self.cf.player_speed
        if keys[pg.K_d]:
            self.player.x += self.cf.player_speed

        if keys[pg.K_SPACE] and ((self.player.y + self.player.height) == platform):
            self.player.y -= self.cf.player_jump_height
