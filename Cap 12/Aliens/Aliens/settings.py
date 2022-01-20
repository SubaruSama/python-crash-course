class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width: int = 1200
        self.screen_height: int = 800
        self.background_color: tuple = (230, 230, 230)
        self.version: str = "0.1"
        self.caption_window = f"Alien Invasion - Version {self.version}"