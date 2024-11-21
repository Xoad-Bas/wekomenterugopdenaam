import pygame
import settings
import game

def draw_grid():
    """Draws the grid."""
    for row in range(settings.GRID_SIZE):
        for col in range(settings.GRID_SIZE):
            rect = pygame.Rect(col * settings.TILE_SIZE, row * settings.TILE_SIZE, settings.TILE_SIZE, settings.TILE_SIZE)
            pygame.draw.rect(game.screen, settings.WHITE, rect, 1)  # Draw tile borders

def draw_player(player_pos):
    """Draws the player at its current position."""
    center_x = player_pos[0] * settings.TILE_SIZE + settings.TILE_SIZE // 2
    center_y = player_pos[1] * settings.TILE_SIZE + settings.TILE_SIZE // 2
    pygame.draw.circle(game.screen, settings.BLUE, (center_x, center_y), settings.TILE_SIZE // 4)

def update_screen(screen, grid_settings, player_settings):
    """Handles rendering the entire screen."""
    # Clear the screen
    screen.fill(grid_settings['background_color'])
    
    # Draw grid
    draw_grid(
        screen,
        grid_settings['size'],
        grid_settings['cell_size'],
        grid_settings['grid_color']
    )
    
    # Draw player
    draw_player(
        screen,
        player_settings['position'],
        player_settings['color'],
        grid_settings['cell_size']
    )
    
    # Update display
    pygame.display.flip()

def prepare_settings(player_pos):
    return {
        'grid': {
            'size': (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT),
            'cell_size': settings.CELL_SIZE,
            'grid_color': settings.GRAY,
            'background_color': settings.BLACK,
        },
        'player': {
            'position': player_pos,
            'color': settings.RED,
        },
    }