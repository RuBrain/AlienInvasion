import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        '''Инициализирует атрибуты кнопки.'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Назначение размеров и свойств кнопки
        self.width, self.height = 150, 50
        self.button_color = (0, 250, 154)
        self.text_color = (0, 191, 155)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создается только 1 раз
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_img, self.msg_img_rect)
