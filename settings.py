class settings:
    """A class to store the settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        #Bullets settings
        self.bullet_speed = 1.0
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1