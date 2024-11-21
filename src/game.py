import pygame
import sys
import settings
import render

# Create the screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Grid Movement")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player position (grid coordinates)
player_pos = settings.PLAYER_START_POS[:]

def handle_player_movement(keys, player_pos, grid_size):
    """Updates player position based on input keys."""
    if keys[pygame.K_w] and player_pos[1] > 0:  # Move up
        player_pos[1] -= 1
    if keys[pygame.K_s] and player_pos[1] < grid_size - 1:  # Move down
        player_pos[1] += 1
    if keys[pygame.K_a] and player_pos[0] > 0:  # Move left
        player_pos[0] -= 1
    if keys[pygame.K_d] and player_pos[0] < grid_size - 1:  # Move right
        player_pos[0] += 1

def game_loop(player_pos):
    """Main game loop."""
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle movement keys
        keys = pygame.key.get_pressed()
        handle_player_movement(keys, player_pos, settings.GRID_SIZE)

        # Render the frame
        screen.fill(settings.BLACK)  # Clear the screen
        render.draw_grid()
        render.draw_player(player_pos)

        pygame.display.flip()  # Update the display

        # Limit the frame rate
        clock.tick(60)

if __name__ == "__main__":
    game_loop(player_pos)
