import pygame

class Rect():
    # Класс для управляения прямоугольником

    def __init__(self, ai_settings, screen):
        # Инициализация
        self.ai_settings = ai_settings
        self.screen = screen
        
        self.screen_rect = screen.get_rect()

        # Создает прямоугольник у правого края по середине.
        self.rect = pygame.Rect(0, 0, ai_settings.rect_width, ai_settings.rect_height)
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

        # Позиция прямоугольника хранится в вещественном формате.
        self.y = float(self.rect.y)
        
        self.color = ai_settings.rect_color
        self.speed_factor = ai_settings.rect_speed_factor

    def draw_rect(self):
        """Вывод прямоугольника на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def check_edges(self):
        """Возвращает True, если прямоугольник находится у края экрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True

        elif self.rect.top <= 0:
            return True

    def update(self):
        """Перемещает прямоугольник."""
        self.y += (self.ai_settings.rect_speed_factor * self.ai_settings.rect_direction)
        self.rect.y = self.y

    def center_rect(self):
        """Размещает прямоугольник в центре правой стороны."""
        self.center = self.screen_rect.centery