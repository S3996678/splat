import pygame as pg
from stages import playing


class Game:
    def __init__(self):
        self.running = True
        self.playing = playing.Playing()

    def run(self):
        while self.running:
            if not self.playing.play():
                self.running = False


if __name__ == "__main__":
    game = Game()
    game.run()