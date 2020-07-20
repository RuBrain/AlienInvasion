import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.transform.rotate(pygame.image.load('images/alienspaceship.png'), -90)
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centery)

        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
                
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.top > 0:
            self.center -= self.ai_settings.ship_speed_factor
       
        # Обновление атрибута rect на основании self.center.
        self.rect.centery = self.center
        
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре левой стороны."""
        self.center = self.screen_rect.centery