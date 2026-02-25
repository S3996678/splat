import pygame as pg
from objects import platform
from config import Config as cf

# this is just a very simple map implementation separate from the logic tye rest of the files hold.


class Map:  # only holds a method now and cannot be initiated
    def create_map(
        self, window_x_length, window_y_height, x_axis_split_ratio, y_axis_split_ratio):  # would probably update to the length of the map

        self.grid_block_height = window_y_height / y_axis_split_ratio
        self.grid_block_width = window_x_length / x_axis_split_ratio
        self.screen_height = window_y_height
        self.screen_width = window_x_length
        self.grid = []

        rows, cols = y_axis_split_ratio, x_axis_split_ratio
        for _ in range(rows):
            row = [0] * cols
            self.grid.append(row)

        return (self.grid)  # returns values i thought might be useful
    


    def populate_map(self, populated_grid):
        self.platform_list = []#store platform instance to later render

        for i,row in enumerate(populated_grid):
            print("row: ",row, ", index: ",i)
            for j,col in enumerate(row):
                if col == 1:
                    row_position = self.screen_height - (i * self.grid_block_height)#this impliments ground up logic
                    col_position = j * self.grid_block_width#impliments start to finish position
                    platform_instance = platform.Platform([col_position, row_position], [self.grid_block_width, self.grid_block_height])
                    self.platform_list.append(platform_instance)


    def draw_platforms(self):#visually render each platform at selected position
        for p in self.platform_list:
            p.draw()
