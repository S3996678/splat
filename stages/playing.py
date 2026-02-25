import pygame as pg
from config import Config as cf
from objects import player, platform, floor, bullet


class Playing:
    def __init__(self):
        pass
        self.clock = pg.time.Clock()
        self.cf = cf
        # player
        self.player = player.Player()
        # flooring
        self.floor = floor.Floor(300)

        self.bullet = bullet.Bullet()

        # store last shot time to control fire rate
        self.last_shot = pg.time.get_ticks()

    def play(self):
        if not self.handle_events():
            return False
        self.draw()

        return True

    def draw(self):
        self.cf.screen.fill((173, 216, 230))

        # platforms that are within the xy of the player
        self.platform = []

        self.bullet.update()
        self.bullet.draw()

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

        mouse_button = pg.mouse.get_pressed()
        current_time = pg.time.get_ticks()
        # if player right clicks and it's been long enough since last shot, shoot and update the self.last_shot
        if mouse_button[0] and (current_time - self.last_shot) > cf.rate_of_fire_delay:
            self.last_shot = current_time
            mouse_pos = pg.mouse.get_pos()
            player_pos = self.player.get_player_pos()
            # if the mouse pos is to the right set bullet direction to right and if left vice versa
            bullet_direction = "r" if player_pos.x < mouse_pos[0] else "l"
            # shoot bullet according to the bullet direction
            if bullet_direction == "r":
                self.bullet.shoot(
                    player_pos.right, player_pos.centery, bullet_direction
                )
            else:
                self.bullet.shoot(player_pos.left, player_pos.centery, bullet_direction)

        return True
