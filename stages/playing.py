import pygame as pg
import config
from objects import player, platform, floor


class Playing:
    def __init__(self):
        pass
        self.clock = pg.time.Clock()
        self.cf = config.Config()
        self.player = player.Player()
        self.platformm = platform.Platform([200, 200])
        self.pl2 = platform.Platform([249, 200])
        self.floor = floor.Floor(1300)

    def play(self):
        if not self.handle_events():
            return False
        self.draw()

        return True

    def draw(self):
        self.cf.screen.fill((173, 216, 230))
        self.platform = self.cf.screen_height

        self.platformm.draw()
        self.pl2.draw()
        self.floor.draw()

        self.player.movement(self.platform)
        self.player.draw()

        pg.display.flip()

        self.clock.tick(self.cf.fps)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        return True
