import pygame as pg
import config
from objects import player, platform, floor, map


class Playing:
    def __init__(self):
        pass
        self.clock = pg.time.Clock()
        self.cf = config.Config()
        self.player = player.Player()
        #self.platformm = platform.Platform([200, 200], [50, 50])
        #self.pl2 = platform.Platform([249, 200], [50, 50])
        self.floor = floor.Floor(1300, [50, 50])
        self.map = map.Map()
        grid = self.map.create_map(1000, 500, 20, 10)
        grid[9][2] = 1
        self.map.populate_map(grid)
        

    def play(self):
        if not self.handle_events():
            return False
        self.draw()

        return True

    def draw(self):
        self.cf.screen.fill((173, 216, 230))

        # platforms that are within the xy of the player
        self.platform = []

        self.map.draw_platforms()

        #self.platformm.draw()
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
