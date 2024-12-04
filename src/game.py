import pygame
import settings
import render

# Create the screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("wekomenterugopdenaam")
clock = pygame.time.Clock()
player_pos = settings.PLAYER_START_POS[:]


def handle_player_movement(keys, player_pos):
    """Updates player position based on input keys."""
    speed = 1
    if keys[pygame.K_w] and player_pos[1] > 0:  # Move up
        player_pos[1] -= speed
    if keys[pygame.K_s] and player_pos[1] < settings.SCREEN_HEIGHT:  # Move down
        player_pos[1] += speed
    if keys[pygame.K_a] and player_pos[0] > 0:  # Move left
        player_pos[0] -= speed
    if keys[pygame.K_d] and player_pos[0] < settings.SCREEN_WIDTH:  # Move right
        player_pos[0] += speed

def game_loop():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Render everything
        render.update_screen(screen, settings.PLAYER_START_POS)

        # Limit frame rate
        clock.tick(10)

if __name__ == "__main__":
    game_loop()
