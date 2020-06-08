import pygame
import sys
from pygame.sprite import Sprite
from pygame.sprite import Group

def run():

    pygame.init()

    # Настройки
    screen_width = 1920
    screen_height = 1080

    drop_width = 50
    drop_height = 50

    number_drops_x = int(screen_width / (2 * drop_width))
    number_drops_y = int(screen_height / (2 * drop_height))

    drops = Group()
 
    bg_color = 90, 60, 90
    drop_speed_factor = 2

    # Создание экрана
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Falling drops")

    # Создание класса капли
    class Drop(Sprite):
        # Класс, представляющий одну каплю.

        def __init__(self):
            """Инициализирует каплю и задает её начальную позицию."""
            super(Drop, self).__init__()

            # Загрузка изображения пришельца и назначение атрибута rect.
            self.image = pygame.transform.scale(pygame.image.load("Sprites/drop.png"), (drop_height, drop_width))
            self.rect = self.image.get_rect()

            # Кординаты первого изображения
            self.rect.x = 0
            self.rect.y = 0

            # Сохранение точной позиции капли.
            self.y = float(self.rect.y)

        def update(self):
            """Перемещает капли вниз."""
            self.rect.y += drop_speed_factor
            self.rect.y = self.y

        def blitme(self):
            screen.blit(self.image, self.rect)

                

    def check_events():
        """Обрабатывает закрытие программы."""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.QUIT:
                sys.exit()

    def update_screen():
        """Обновляет изображения на экране и отображает новый экран."""

        # При каждом проходе цикла перерисовывается экран.
        #screen.fill(bg_color)
        drops.draw(screen)
                   
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()

    def create_drop(drop_number):
        # Создает каплю  и размещает ее в ряду
        drop = Drop()
        drop.rect.x = 2 * drop_width * drop_number
        drop.rect.y = 2 * drop.rect.height * row_number - 300
        #screen.blit(drop.image, drop.rect)
        drops.add(drop)
        
    # Создание всех капель
    for row_number in range(number_drops_y):
        for drop_number in range(number_drops_x):
            create_drop(drop_number)
    
    while True:
        check_events()
        drops.update()
        update_screen()

run()