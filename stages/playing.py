import pygame as pg
from config import Config as cf
from objects import player, platform, floor, map


class Playing:
    def __init__(self):
        pass
        self.clock = pg.time.Clock()
        self.player = player.Player()
        # self.floor = floor.Floor(1300, [50, 50])
        self.map = map.Map()
        grid = self.map.create_map(
            cf.screen_width,
            cf.screen_height,
            cf.grid_split_ratio_x,
            cf.grid_split_ratio_y,
            cf.map_block_length
        )
        grid[3][16] = 1  # y,x 9 blocks from the bottom up and 19 blocks from the start
        grid[3][15] = 1
        grid[9][19] = 1
        self.map.populate_map(grid)
        
        self.floor = self.map.get_floor()
        self.platform_list = self.map.get_platforms()

    def play(self):
        if not self.handle_events():
            return False
        self.draw()

        return True

    def draw(self):
        cf.screen.fill((173, 216, 230))

        # platforms that are within the xy of the player
        self.platform = []

        self.map.draw_platforms()

        player_pos = self.player.get_player_pos()

        cur_floor = self.map.check_entity_istop(player_pos.midbottom[0])

        self.platform.append(cur_floor)
        # temporary platforms

        self.platform = [cur_floor]

        #self.floor.draw()

        self.player.movement(self.platform, self.platform_list)
        self.player.draw()

        pg.display.flip()

        self.clock.tick(cf.fps)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        return True
