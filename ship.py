import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка изображения корабля и получение прямоугольника.
        self.image = pygame.image.load('Sprites/RandomShips1/alienspaceship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # Сохранение вещественной координаты центра корабля.
        self.center = float(self.rect.centerx)
        self.center1 = float(self.rect.centery)
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        if self.moving_up:
            self.center1 -= self.ai_settings.ship_speed_factor

        if self.moving_down:
            self.center1 += self.ai_settings.ship_speed_factor    

        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.center
        self.rect.centery = self.center1

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)