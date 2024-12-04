import pygame
import settings

def handle_camera(player_pos, tile_size, screen_width, screen_height):
    """Adjusts the camera position to center the player."""
    camera = pygame.math.Vector2(0, 0)
    # Convert player position from grid to pixel coordinates
    camera.x = player_pos[0] * tile_size - screen_width / 2
    camera.y = player_pos[1] * tile_size - screen_height / 2
    return camera

def draw_grid(screen, grid_size, tile_size, grid_color, camera):
    """Draws the grid, adjusted for the camera."""
    for row in range(grid_size):
        for col in range(grid_size):
            rect_x = col * tile_size - camera.x
            rect_y = row * tile_size - camera.y
            rect = pygame.Rect(rect_x, rect_y, tile_size, tile_size)
            pygame.draw.rect(screen, grid_color, rect, 1)

def draw_player(screen, player_pos, tile_size, player_color, camera):
    """Draws the player at its current position, adjusted for the camera."""
    center_x = player_pos[0] * tile_size + tile_size // 2 - camera.x
    center_y = player_pos[1] * tile_size + tile_size // 2 - camera.y
    pygame.draw.circle(screen, player_color, (int(center_x), int(center_y)), tile_size // 4)

    # Handle player input (movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_pos[1] > 0:  # Move up
        player_pos[1] -= 1
    if keys[pygame.K_s] and player_pos[1] < settings.GRID_SIZE - 1:  # Move down
        player_pos[1] += 1
    if keys[pygame.K_a] and player_pos[0] > 0:  # Move left
        player_pos[0] -= 1
    if keys[pygame.K_d] and player_pos[0] < settings.GRID_SIZE - 1:  # Move right
        player_pos[0] += 1

def update_screen(screen, player_pos):
    """Handles rendering the entire screen."""
    # Clear the screen
    screen.fill(settings.BLACK)

    # Handle camera
    camera = handle_camera(player_pos, settings.TILE_SIZE, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)

    # Draw grid
    draw_grid(screen, settings.GRID_SIZE, settings.TILE_SIZE, settings.GRAY, camera)

    # Draw player
    draw_player(screen, player_pos, settings.TILE_SIZE, settings.BLUE, camera)

    # Update display
    pygame.display.flip()