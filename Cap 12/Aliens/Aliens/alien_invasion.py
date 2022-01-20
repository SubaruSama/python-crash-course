import pygame

from settings import Settings
from ship import Ship
import game_functions

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    background_color = (230, 230, 230)
    pygame.display.set_caption(ai_settings.caption_window)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(ai_settings, screen, ship=ship)

run_game()