import pygame as pg
#this is just a very simple map implementation separate from the logic tye rest of the files hold.

class Map:#only holds a method now and cannot be initiated


    def create_map(window_x_length,window_y_height,x_axis_split_ratio, y_axis_split_ratio):#would probably update to the length of the map

        grid_block_height = window_y_height / y_axis_split_ratio
        grid_block_width = window_x_length / x_axis_split_ratio
        rows, cols = y_axis_split_ratio, x_axis_split_ratio
        grid = []

        for _ in range(rows):
            row = [0] * cols
            grid.append(row)

        return grid, grid_block_height, grid_block_width#returns values i thought might be useful
    
        



