class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        
        # параметры экрана:
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = 66, 33, 66
        self.ship_speed_factor = 8
        
        # параметры пули
        self.bullet_speed_factor = 8
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 4

        # настройка пришельцев
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 15
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1