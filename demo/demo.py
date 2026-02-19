import pygame as pg

# Initialize and setup
pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
running = True
player = pg.Rect(50, 50, 100, 100)
enemy = pg.Rect(750, 50, 100, 100)

# --- Main Loop ---
while running:
    # 1. Event Handling
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    key = pg.key.get_pressed()
    if key[pg.K_a]:
        player.x -= 5
    if key[pg.K_d]:
        player.x += 5
    if key[pg.K_w]:
        player.y -= 5
    if key[pg.K_s]:
        player.y += 5

    if enemy.x > player.x:
        enemy.x -= 1
    elif enemy.x < player.x:
        enemy.x += 1
    if enemy.y > player.y:
        enemy.y -= 1
    elif enemy.y < player.y:
        enemy.y += 1

    # 2. Logic / State Updates
    # (Update positions, check collisions, etc.)
    if player.colliderect(enemy):
        running = False
    # 3. Rendering
    screen.fill((0, 0, 0))  # Clear screen
    # (Draw your objects here)
    pg.draw.rect(screen, (150, 20, 92), enemy)

    pg.draw.rect(screen, (255, 0, 0), player)

    pg.display.flip()  # Update display

    # 4. Frame Rate Control
    clock.tick(60)  # Limit to 60 FPS

pg.quit()
