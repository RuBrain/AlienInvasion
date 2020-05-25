class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        
        # параметры экрана:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 0, 100, 150
        self.ship_speed_factor = 1.5
        
        # параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 0