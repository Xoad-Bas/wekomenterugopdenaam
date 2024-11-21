import pygame
import settings
import game

# Initialize Pygame
pygame.init()

def main():
    """Initializes game and starts the loop."""
    player_pos = settings.PLAYER_START_POS[:]  # Starting position copied from settings
    game.game_loop(player_pos)

if __name__ == "__main__":
    main()
