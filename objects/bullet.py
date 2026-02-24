import pygame as pg
from config import Config as cf


class Bullet:
    def __init__(self):
        # stores all bullets with bullet object aswell as the direction of bullet for example [bullet,'R']
        self.bullets = []

    # create bullet and set a direction
    def shoot(self, pos_x, pos_y, direction):
        bullet = pg.Rect(pos_x, pos_y, cf.bullet_size, cf.bullet_size)
        self.bullets.append([bullet, direction])

    def draw(self):
        for bullet in self.bullets:
            cf.screen.blit(cf.bullet_img, bullet[0])

    def update(self):
        # go through all bullets and update their position them according to the direction
        for bullet in self.bullets:
            if bullet[1] == "r":
                bullet[0].x += cf.bullet_speed
            elif bullet[1] == "l":
                bullet[0].x -= cf.bullet_speed
