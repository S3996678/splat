import pygame as pg
import config
from objects import player, platform, floor


class Playing:
    def __init__(self):
        pass
        self.clock = pg.time.Clock()
        self.cf = config.Config()
        self.player = player.Player()
        # flooring
        self.floor = floor.Floor(1300)

    def play(self):
        if not self.handle_events():
            return False
        self.draw()

        return True

    def draw(self):
        self.cf.screen.fill((173, 216, 230))

        # platforms that are within the xy of the player
        self.platform = []

        player_pos = self.player.get_player_pos()

        cur_floor = self.floor.check_entity_istop(player_pos.midbottom[0])
        self.platform.append(cur_floor)
        # temporary platforms
        self.platform = [cur_floor]

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
