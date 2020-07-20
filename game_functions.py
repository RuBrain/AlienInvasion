import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    # Создание новой пули и включение ее в группу bullets.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet) 

def check_keyup_events(event, ship):
    """Реагирует на отпускание клавиш."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def check_events(ai_settings, screen, play_button, ship, bullets, rectangle):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, play_button, ship, bullets, rectangle, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, play_button, ship, bullets, rectangle, mouse_x, mouse_y):
    """Запускает новую игру при нажатии кнопки Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y):

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)

        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not ai_settings.game_active:

           

            ai_settings.game_active = True

            # Очистка списка пуль.
            bullets.empty()

            #размещение корабля и прямоугольника в центре.
            rectangle.center_rect()
            ship.center_ship()

def update_screen(ai_settings, screen, ship, bullets, rectangle, play_button):
    """Обновляет изображения на экране и отображает новый экран."""

    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    rectangle.draw_rect()

    # Все пули выводятся позади изображений корабля и пришельцев.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Кнопка Play отображается в том случае, если игра неактивна.
    if not ai_settings.game_active:
        play_button.draw_button()

    # Отображение последнего прорисованного экрана.
    pygame.display.flip()
   
def update_bullets(ai_settings, bullets):
    """Обновляет позиции пуль и уничтожает старые пули."""

    # Обновление позиций пуль.
    bullets.update()

    # Удаление пуль, вышедших за край экрана.
    for bullet in bullets.copy():
        if bullet.rect.right > 1200:
            bullets.remove(bullet)
            ai_settings.permissible_shots -= 1

    # Остановка игры после 3 промахов
    if ai_settings.permissible_shots == 0:
        ai_settings.game_active = False
        pygame.mouse.set_visible(True)
        ai_settings.permissible_shots += 3

def check_fleet_edges(ai_settings, rectangle):
    """Реагирует на достижение прямоугольником края экрана."""
    if rectangle.check_edges():
        change_fleet_direction(ai_settings, rectangle)
        
def change_fleet_direction(ai_settings, ractangle):
    """Меняет направление прямоугольника."""
    ai_settings.rect_direction *= -1

def update_rect(ai_settings, screen, ship, bullets, rectangle):
    """Проверяет, достиг ли флот края экрана,
    после чего обновляет позиции всех пришельцев во флоте
    """
    check_fleet_edges(ai_settings, rectangle)
    rectangle.update()

    # Проверка коллизий "прямоугольник-пуля".
    if pygame.sprite.spritecollideany(rectangle, bullets):
        bullets.empty()
        change_fleet_direction(ai_settings, rectangle)
  
            