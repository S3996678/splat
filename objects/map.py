import pygame as pg
from objects import platform
from config import Config as cf

# this is just a very simple map implementation separate from the logic tye rest of the files hold.


class Map:  # only holds a method now and cannot be initiated
    def create_map(
        self, window_x_length, window_y_height, x_axis_split_ratio, y_axis_split_ratio):  # would probably update to the length of the map

        self.grid_block_height = window_y_height / y_axis_split_ratio
        self.grid_block_width = window_x_length / x_axis_split_ratio
        rows, cols = y_axis_split_ratio, x_axis_split_ratio
        self.grid = []
        #self.platforms = []

        for _ in range(rows):
            row = [0] * cols
            self.grid.append(row)

        return (self.grid)  # returns values i thought might be useful
    


    def populate_map(self, coordinates):
        self.platform_list = []
        for i,row in enumerate(coordinates):
            for j,col in enumerate(row):
                if col == 1:
                    x_position = i * self.grid_block_width
                    y_position = j * self.grid_block_height
                    platform_instance = platform.Platform([x_position, y_position], [self.grid_block_width, self.grid_block_height])
                    self.platform_list.append(platform_instance)


    def draw_platforms(self):
        for p in self.platform_list:
            p.draw()
