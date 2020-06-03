class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        
        # параметры экрана:
        self.screen_width = 1700
        self.screen_height = 1000
        self.bg_color = 66, 33, 66
        self.ship_speed_factor = 8
        
        # параметры пули
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 4