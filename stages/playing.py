import pygame as pg
import config


class Playing:
    def __init__(self):
        pass
        self.clock = pg.time.Clock()
        self.cf = config.Config()

    def play(self):
        if not self.handle_events():
            return False
        self.draw()

        return True

    def draw(self):
        self.cf.screen.fill((0, 0, 0))

        pg.display.flip()

        self.clock.tick(self.cf.fps)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False

        return True
