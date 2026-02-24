import pygame as pg
import platform

# this is just a very simple map implementation separate from the logic tye rest of the files hold.


class Map:  # only holds a method now and cannot be initiated
    def create_map(
        self, window_x_length, window_y_height, x_axis_split_ratio, y_axis_split_ratio
    ):  # would probably update to the length of the map

        self.grid_block_height = window_y_height / y_axis_split_ratio
        self.grid_block_width = window_x_length / x_axis_split_ratio
        rows, cols = y_axis_split_ratio, x_axis_split_ratio
        self.grid = []
        self.platforms = []

        for _ in range(rows):
            row = [0] * cols
            self.grid.append(row)

        return (
            self.grid,
            self.grid_block_height,
            self.grid_block_width,
        )  # returns values i thought might be useful

    def populate_map(self, coordinates):
        for c in coordinates:
            pos_x = c[0] * self.grid_block_width
            pos_y = c[1] * self.grid_block_height
            self.platforms.append(
                platform.platform(
                    [pos_x, pos_y], [self.grid_block_width, self.grid_block_height]
                )
            )

    def draw(self):
        for p in self.platforms:
            p.draw()
