class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""

        # игра запускается в неактивном состоянии
        self.game_active = False

        # параметры экрана:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 66, 33, 66
                
        # параметры пули
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 0, 255, 255
        self.bullets_allowed = 3
        self.permissible_shots = 3

        # параметры прямоугольника
        self.rect_width = 30
        self.rect_height = 90
        self.rect_color = 200, 0, 0
        # rect_direction = 1 обозначает движение вниз; а -1 - вверх.
        self.rect_direction = 1

        # повышение скорости
        self.speedup_scale = 1.2
        self.reset_speed()

    def reset_speed(self):
        self.rect_speed_factor = 1.5
        self.bullet_speed_factor = 8
        self.ship_speed_factor = 3

    def raising_complexity(self):
        self.rect_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale


        