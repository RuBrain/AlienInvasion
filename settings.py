class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""

        # Настройки экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (66, 33, 66)

        # Настройки корабля
        self.ship_limit = 3

        # Настройки пуль
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 15

        # Темп ускорения игры
        self.speedup_scale = 1.4
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 8
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 2

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale