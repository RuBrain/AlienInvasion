import pygame
from pygame.sprite import Group
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from rectangle import Rect
from button import Button

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Training Shooting")

    # Создание кнопки
    play_button = Button(ai_settings, screen, "Start!")

    #Создание корабля.
    ship = Ship(ai_settings, screen)

    # Создание прямоугольника
    rectangle = Rect(ai_settings, screen)

    # Создание группы для хранения пуль.
    bullets = Group()

    # Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, play_button, ship, bullets, rectangle)

        if ai_settings.game_active:
            ship.update()
            gf.update_bullets(ai_settings, bullets)
            gf.update_rect(ai_settings, screen, ship, bullets, rectangle)
            
        gf.update_screen(ai_settings, screen, ship, bullets, rectangle, play_button)

run_game()