import pygame

# Initialize and setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# --- Main Loop ---
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Logic / State Updates
    # (Update positions, check collisions, etc.)

    # 3. Rendering
    screen.fill((0, 0, 0))  # Clear screen
    # (Draw your objects here)
    pygame.display.flip()  # Update display

    # 4. Frame Rate Control
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()
